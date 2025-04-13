import pytest
import os
from test.utils import Fake_data
from sync_tool.logger import setup_logging
import logging
import shutil
setup_logging("test_log.log")


@pytest.fixture
def setup_test_data():

   source = "source_test"
   replica = "replica_test"
   
   for path in( source, replica):
      if os.path.exists(path):
         shutil.rmtree(path)
         logging.info(f"Removed existing directory: {path}")
      os.makedirs(path)
      logging.info(f"Created directory: {path}")

   a = Fake_data()
   a.fake_data_create("source_test", 5)
   a.feke_folder_create("source_test",3,4)

   yield source, replica
   
   a.fake_data_delete("source_test")
   a.fake_data_delete("replica_test")

   for path in (source,replica):
      shutil.rmtree(path)
  
