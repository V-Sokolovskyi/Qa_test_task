import argparse
def parse_arguments():
    parser = argparse.ArgumentParser(description="Folder Synchronizer with Hash Check")
    parser.add_argument("source", help="Path to the source folder")
    parser.add_argument("replica", help="Path to the replica folder")
    parser.add_argument("log_file", help="Path to the log file")
    parser.add_argument("interval", type=int, help="Synchronization interval in seconds")
    parser.add_argument("--algo", default="blake2b", help="Hash algorithm to use (default: blake2b)")
    parser.add_argument("--once", action="store_true", help="Run sync only once and exit")
    return parser.parse_args()