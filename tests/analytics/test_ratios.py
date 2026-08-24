import pytest
from src.analytics.ratios import (
    compute_pe_ratio,
    compute_pb_ratio,
    compute_roe,
    calculate_debt_to_equity,
    calculate_quick_ratio
)

def test_compute_pe_ratio_valid():
    assert compute_pe_ratio(100.0, 5.0) == 20.0

def test_compute_pe_ratio_zero_or_negative_eps():
    with pytest.raises(ValueError, match="EPS must be greater than zero"):
        compute_pe_ratio(100.0, 0.0)

def test_compute_pb_ratio_valid():
    assert compute_pb_ratio(50.0, 10.0) == 5.0

def test_compute_pb_ratio_zero_or_negative_book_value():
    with pytest.raises(ValueError, match="Book value per share must be greater than zero"):
        compute_pb_ratio(50.0, 0.0)

def test_compute_roe_valid():
    assert compute_roe(15000.0, 100000.0) == 15.0

def test_compute_roe_zero_or_negative_equity():
    with pytest.raises(ValueError, match="Shareholder equity must be greater than zero"):
        compute_roe(15000.0, 0.0)

def test_calculate_debt_to_equity_standard():
    assert calculate_debt_to_equity(total_debt=50000, total_equity=100000) == 0.5

def test_calculate_debt_to_equity_zero_equity():
    with pytest.raises(ValueError, match="Total equity cannot be zero"):
        calculate_debt_to_equity(total_debt=50000, total_equity=0)

def test_calculate_quick_ratio_standard():
    assert calculate_quick_ratio(
        cash=20000,
        marketable_securities=10000,
        receivables=15000,
        current_liabilities=30000
    ) == 1.5

def test_calculate_quick_ratio_zero_liabilities():
    with pytest.raises(ValueError, match="Current liabilities cannot be zero"):
        calculate_quick_ratio(
            cash=10000,
            marketable_securities=0,
            receivables=5000,
            current_liabilities=0
        )
