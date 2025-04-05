import os
import shutil
import logging
from sync_tool.cashe_utils import Cache
from sync_tool.hash_utils import hash_file

def file_changed(source_file, replica_file, algo, cache:Cache):
    if not os.path.exists(replica_file):
        return True
    source_hash =  cache.hash_cache.get(source_file)
    if not source_hash:

        source_hash = hash_file(source_file, algo)
        cache.hash_cache[source_file]= source_hash

    replica_hash = hash_file(replica_file, algo)
    if source_hash != replica_hash:
        
        return True
    return False

def sync_folders(source, replica, algo, cache:Cache):
    for root, dirs, files in os.walk(source):
        rel_path = os.path.relpath(root, source)
        replica_root = os.path.join(replica, rel_path)
        if not os.path.exists(replica_root):
            os.makedirs(replica_root)
            logging.info(f"Created directory: {replica_root}")

        for file in files:
            source_file = os.path.join(root, file)
            replica_file = os.path.join(replica_root, file)
            if file_changed(source_file, replica_file, algo, cache):
                shutil.copy2(source_file, replica_file)
                cache.hash_cache[source_file] = hash_file(source_file, algo)
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