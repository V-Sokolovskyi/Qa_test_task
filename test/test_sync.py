import pytest
import subprocess
from test.utils import count_of_files

@pytest.mark.sync
def test_sync_basic(setup_test_data):
    subprocess.run([
    "python", "main.py",
    "source", "replica", "test_log.log", "1", 
    "--once"
    ], timeout=5)
    
    source_count = count_of_files("source")
    replica_count =count_of_files("replica")
    assert source_count == replica_count, f"Test failed, Source and replica file count do not match!  source= {source_count}, replica = {replica_count}"
    print("Test complete!")