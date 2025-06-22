def run(state: dict) -> dict:
    news=state.news
    # news = news["cone"]
    content = news["content"]
    tickers = []
    if "(NASDAQ:" in content:
        tickers.append(content.split("(NASDAQ:")[1].split(")")[0])
    state.tickers = tickers
    state.cleaned_content = content.lower().strip()
    return state
