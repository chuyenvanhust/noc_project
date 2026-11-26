import pytest
from noc.models.mac import predict_mac


@pytest.mark.skip(reason="TODO: bỏ skip sau khi cài predict_mac")
def test_mac_basic():
    assert predict_mac([2, 2, 3]) == 2   # max 3 allele -> ceil(3/2) = 2
    assert predict_mac([1, 2, 2]) == 1
    assert predict_mac([5, 4]) == 3
