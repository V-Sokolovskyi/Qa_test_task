import os
import shutil
import time
import argparse
import logging
from filecmp import cmp

def parse_arguments():
    parser = argparse.ArgumentParser(description="Folder Synchronizer")
    parser.add_argument("source", help="Path to the source folder")
    parser.add_argument("replica", help="Path to the replica folder")
    parser.add_argument("log_file", help="Path to the log file")
    parser.add_argument("interval", type=int, help="Synchronization interval in seconds")
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

def sync_folders(source, replica):
    
    for root, dirs, files in os.walk(source):
        rel_path = os.path.relpath(root, source)
        replica_root = os.path.join(replica, rel_path)
        if not os.path.exists(replica_root):
            os.makedirs(replica_root)
            logging.info(f"Created directory: {replica_root}")

        for file in files:
            source_file = os.path.join(root, file)
            replica_file = os.path.join(replica_root, file)
            if not os.path.exists(replica_file) or not cmp(source_file, replica_file, shallow=False):
                shutil.copy2(source_file, replica_file)
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

    while True:
        sync_folders(args.source, args.replica)
        logging.info("Synchronization complete. Waiting for next interval...")
        time.sleep(args.interval)

if __name__ == "__main__":
    main()