

from langgraph.graph import StateGraph
from agents import (
    preprocessing_agent,
    sentiment_agent,
    market_impact_agent,
    entity_risk_agent,
    aggregator_agent,
)
from pydantic import BaseModel
from typing import Dict, Any, List

# ✅ Define schema to represent the state passed between agents
class NewsState(BaseModel):
    news: Dict[str, Any]
    cleaned_content: str = ""
    tickers: List[str] = []
    sentiment: str = ""
    market_impact: str = ""
    risks: List[str] = []
    final_analysis: Dict[str, Any] = {}

def build_graph():
    graph = StateGraph(state_schema=NewsState)  # 👈 REQUIRED

    graph.add_node("PreprocessingAgent", preprocessing_agent.run)
    graph.add_node("SentimentAnalysisAgent", sentiment_agent.run)
    graph.add_node("MarketImpactAgent", market_impact_agent.run)
    graph.add_node("EntityRiskAgent", entity_risk_agent.run)
    graph.add_node("AggregatorAgent", aggregator_agent.run)

    graph.set_entry_point("PreprocessingAgent")
    graph.add_edge("PreprocessingAgent", "SentimentAnalysisAgent")
    graph.add_edge("SentimentAnalysisAgent", "MarketImpactAgent")
    graph.add_edge("MarketImpactAgent", "EntityRiskAgent")
    graph.add_edge("EntityRiskAgent", "AggregatorAgent")
    graph.set_finish_point("AggregatorAgent")
    return graph.compile()


import streamlit as st
from main import build_graph
from utils.serper_client import fetch_financial_news
from utils.id_generator import generate_user_id

st.set_page_config(page_title="📰 Financial News Analyzer", layout="centered")
st.title("📈 Finance Insight Analyzer (LangGraph Multi-Agent)")



if topic:= st.chat_input("Enter a financial topic you'd like to analyze (e.g., 'Tesla earnings'):"):
    st.info(f"Looking up financial news related to: `{topic}`")
    with st.spinner("🛰️ Fetching news from Google via Serper API..."):
        articles = fetch_financial_news(topic)

    if articles:

            

        for article in articles:
            article_id = generate_user_id(article['headline'])

        news_data = {
                "article_id": article_id,
                "headline": article["headline"],
                "content": article["content"],
                "published_at": article["published_at"]
            }

        st.subheader("📰 Top Article")
        st.write(f"**Title**: {news_data['headline']}")
        st.write(f"**Content**: {news_data['content']}")
        st.caption(f"🆔 Article ID (SSID-style): `{article_id}`")

        st.subheader("🧠 Analyzing using LangGraph agents...")
        graph = build_graph()
        result = graph.invoke({"news": news_data})

        st.success("✅ Analysis Complete")
        if "final_analysis" in result:
            st.json(result["final_analysis"])
        else:
            st.warning("final_analysis not found in result")
    else:
        st.error("❌ No relevant news found. Please try another topic.")
