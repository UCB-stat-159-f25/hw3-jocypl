import os
import pytest
from ligotools import readligo as rl

# Path to small H1 file
fn_H1 = os.path.join(os.path.dirname(__file__), "../../data/H-H1_LOSC_4_V2-1126259446-32.hdf5")

def test_loaddata_H1_exists():
    # Check that file exists
    assert os.path.isfile(fn_H1), f"{fn_H1} does not exist"
    
    # Load data
    strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, "H1")
    
    # Check types
    assert isinstance(strain_H1, list) or hasattr(strain_H1, "__len__")
    assert isinstance(time_H1, list) or hasattr(time_H1, "__len__")
    assert isinstance(chan_dict_H1, dict)
def test_loaddata_channels():
    strain_H1, time_H1, chan_dict_H1 = rl.loaddata(fn_H1, "H1")
    # Check that some expected key exists
    assert "H1:STRAIN" in chan_dict_H1 or len(chan_dict_H1) > 0