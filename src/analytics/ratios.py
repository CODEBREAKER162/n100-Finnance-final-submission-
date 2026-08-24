def compute_pe_ratio(price: float, eps: float) -> float | None:
    """Calculates Price-to-Earnings (P/E) ratio."""
    if price is None or eps is None or eps <= 0:
        return None
    return price / eps


def compute_pb_ratio(price: float, book_value: float) -> float | None:
    """Calculates Price-to-Book (P/B) ratio."""
    if price is None or book_value is None or book_value <= 0:
        return None
    return price / book_value


def compute_roe(net_income: float, shareholder_equity: float) -> float | None:
    """Calculates Return on Equity (ROE) as a percentage."""
    if net_income is None or shareholder_equity is None or shareholder_equity <= 0:
        return None
    return (net_income / shareholder_equity) * 100.0
