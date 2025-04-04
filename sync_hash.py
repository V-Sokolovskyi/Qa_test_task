import os
import shutil
import time
import argparse
import logging
from hash import hash_file
import json



CACHE_FILE = "hash_cache.json"

# Завантаження кешу з файлу
if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, 'r') as f:
        hash_cache = json.load(f)
        print("Loaded hash cache from file.")
else:
    hash_cache = {}
    print("Initialized empty hash cache.")

def save_cache():
    with open(CACHE_FILE, 'w') as f:
        json.dump(hash_cache, f, indent = 4)
        print("Saved hash cache to file.")


def clean_cash():
    keys_to_delete = [path for path in hash_cache if not os.path.exists(path)]
    for key in keys_to_delete:
        del hash_cache[key]
        logging.info(f"Removed stale cache entry: {key}")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Folder Synchronizer with Hash Check")
    parser.add_argument("source", help="Path to the source folder")
    parser.add_argument("replica", help="Path to the replica folder")
    parser.add_argument("log_file", help="Path to the log file")
    parser.add_argument("interval", type=int, help="Synchronization interval in seconds")
    parser.add_argument("--algo", default="blake2b", help="Hash algorithm to use (default: blake2b)")
    parser.add_argument("--once", action="store_true", help="Run sync only once and exit")
    return parser.parse_args()

def setup_logging(log_file_path):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file_path),
            logging.StreamHandler()
        ]
    )


def file_changed(source_file, replica_file, algo):
    if not os.path.exists(replica_file):
        return True
    source_hash =  hash_cache.get(source_file)
    if not source_hash:

        source_hash = hash_file(source_file, algo)
        hash_cache[source_file]= source_hash

    replica_hash = hash_file(replica_file, algo)
    if source_hash != replica_hash:
        
        return True
    return False


def sync_folders(source, replica, algo):
    for root, dirs, files in os.walk(source):
        rel_path = os.path.relpath(root, source)
        replica_root = os.path.join(replica, rel_path)
        if not os.path.exists(replica_root):
            os.makedirs(replica_root)
            logging.info(f"Created directory: {replica_root}")

        for file in files:
            source_file = os.path.join(root, file)
            replica_file = os.path.join(replica_root, file)
            if file_changed(source_file, replica_file, algo):
                shutil.copy2(source_file, replica_file)
                hash_cache[source_file] = hash_file(source_file, algo)
                logging.info(f"Copied file: {source_file} -> {replica_file}")

    for root, dirs, files in os.walk(replica, topdown=False):
        rel_path = os.path.relpath(root, replica)
        source_root = os.path.join(source, rel_path)

        for file in files:
            replica_file = os.path.join(root, file)
            source_file = os.path.join(source_root, file)
            if not os.path.exists(source_file):
                os.remove(replica_file)
                logging.info(f"Removed file: {replica_file}")

        for dir in dirs:
            replica_dir = os.path.join(root, dir)
            source_dir = os.path.join(source_root, dir)
            if not os.path.exists(source_dir):
                shutil.rmtree(replica_dir)
                logging.info(f"Removed directory: {replica_dir}")

def main():
    args = parse_arguments()
    setup_logging(args.log_file)
    logging.info("Starting folder synchronization...")

    try:
        if args.once:
            sync_folders(args.source, args.replica, args.algo)
            clean_cash()
            save_cache()
            logging.info("Synchronization complete (once).")
        else:
            while True:
                sync_folders(args.source, args.replica, args.algo)
                clean_cash()
                save_cache()
                logging.info("Synchronization complete. Waiting for next interval...")
                time.sleep(args.interval)
    except KeyboardInterrupt:
            logging.info("Synchronization stopped by user.")
            save_cache()

if __name__ == "__main__":
    main()