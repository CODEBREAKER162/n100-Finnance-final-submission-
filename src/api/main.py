from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.analytics.ratios import calculate_debt_to_equity, calculate_quick_ratio

app = FastAPI(title="N100 Financial Analytics API", version="1.0.0")

class DebtToEquityRequest(BaseModel):
    total_debt: float
    total_equity: float

class QuickRatioRequest(BaseModel):
    cash: float
    marketable_securities: float
    receivables: float
    current_liabilities: float

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/analytics/debt-to-equity")
def get_debt_to_equity(data: DebtToEquityRequest):
    try:
        ratio = calculate_debt_to_equity(data.total_debt, data.total_equity)
        return {"ratio": ratio}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/analytics/quick-ratio")
def get_quick_ratio(data: QuickRatioRequest):
    try:
        ratio = calculate_quick_ratio(
            data.cash,
            data.marketable_securities,
            data.receivables,
            data.current_liabilities
        )
        return {"ratio": ratio}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
