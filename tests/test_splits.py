import pandas as pd
import pytest
from noc.data.splits import make_group_split, assert_no_leakage


@pytest.mark.skip(reason="TODO: bỏ skip sau khi cài splits")
def test_no_group_leakage():
    meta = pd.DataFrame({"sample_id": range(100), "noc": [1, 2, 3, 4] * 25,
                         "genotype_set": [f"g{i % 20}" for i in range(100)]})
    sp = make_group_split(meta, "genotype_set")
    assert_no_leakage(meta, sp, "genotype_set")
