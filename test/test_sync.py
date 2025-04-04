import pytest
import os
import subprocess
from test.utils import count_of_files

def test_1(file_gen_and_dell):
    subprocess.run([
    "python", "sync_hash.py",
    "source", "replica", "test_log.log", "1", 
    "--once"
    ], timeout=5)
    
    source_count = count_of_files("source")
    replica_count =count_of_files("replica")
    assert source_count == replica_count
    print("Test commplit!")