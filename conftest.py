import pytest
import os
from test.utils import Fake_data



@pytest.fixture
def file_gen_and_dell():
   a = Fake_data()
   a.fake_data_create("source", 5)
   a.feke_folder_create("source",3,4)
   yield
   a.fake_data_delete("source")
   a.fake_data_delete("replica")
  
