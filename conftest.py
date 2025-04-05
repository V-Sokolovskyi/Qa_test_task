import pytest
import os
from test.utils import Fake_data
from sync_tool.logger import setup_logging
setup_logging("test_log.log")


@pytest.fixture
def setup_test_data():
   a = Fake_data()
   a.fake_data_create("source", 5)
   a.feke_folder_create("source",3,4)
   yield
   a.fake_data_delete("source")
   a.fake_data_delete("replica")
  
