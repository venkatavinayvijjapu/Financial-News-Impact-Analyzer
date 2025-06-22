def run(state: dict) -> dict:
    summary = {
        "sentiment": state.sentiment,
        "impact_level": state.market_impact,
        "risks": state.risks,
        "tickers": state.tickers,
    }
    if summary["sentiment"] == "positive" and summary["impact_level"] == "high":
        decision = "Buy Signal / Strong Upside"
    elif summary["sentiment"] == "negative":
        decision = "Potential Downturn / Monitor"
    else:
        decision = "Low Impact / No Action"
    summary["decision"] = decision
    state.final_analysis = summary
    return state
