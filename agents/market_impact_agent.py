from utils.llm_client import llama_prompt

def run(state: dict) -> dict:
    content = state.cleaned_content
    prompt = f'''Evaluate the following financial news content and estimate its impact on the market. Respond with only 'high', 'medium', or 'low'.

Content:
\"\"\"
{content}
\"\"\"
Market Impact:'''
    impact = llama_prompt(prompt).lower()
    state.market_impact = impact
    return state
