import time
import logging
from sync_tool.cashe_utils import Cache
from sync_tool.logger import setup_logging
from sync_tool.sync_logic import sync_folders
from sync_tool.arg_parse import parse_arguments

def main():
    args = parse_arguments()
    setup_logging(args.log_file)
    logging.info("Starting folder synchronization...")
    cache = Cache()

    try:
        if args.once:
            sync_folders(args.source, args.replica, args.algo, cache)
            cache.clean_cache()
            cache.save_cache()
            logging.info("Synchronization complete (once).")
        else:
            while True:
                sync_folders(args.source, args.replica, args.algo, cache)
                cache.clean_cache()
                cache.save_cache()
                logging.info("Synchronization complete. Waiting for next interval...")
                time.sleep(args.interval)
    except KeyboardInterrupt:
            logging.info("Synchronization stopped by user.")
            cache.save_cache()

if __name__ == "__main__":
    main()