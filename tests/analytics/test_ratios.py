import pytest
from src.analytics.ratios import compute_pe_ratio, compute_pb_ratio, compute_roe


def test_compute_pe_ratio():
    assert compute_pe_ratio(100.0, 5.0) == 20.0
    assert compute_pe_ratio(100.0, 0.0) is None
    assert compute_pe_ratio(100.0, -2.0) is None
    assert compute_pe_ratio(None, 5.0) is None


def test_compute_pb_ratio():
    assert compute_pb_ratio(100.0, 25.0) == 4.0
    assert compute_pb_ratio(100.0, 0.0) is None
    assert compute_pb_ratio(100.0, -10.0) is None
    assert compute_pb_ratio(100.0, None) is None


def test_compute_roe():
    assert compute_roe(50.0, 200.0) == 25.0
    assert compute_roe(50.0, 0.0) is None
    assert compute_roe(50.0, -100.0) is None
    assert compute_roe(None, 200.0) is None
