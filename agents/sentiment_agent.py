from utils.llm_client import llama_prompt

def run(state: dict) -> dict:
    content = state.cleaned_content
    prompt = f'''Analyze the financial sentiment of the following article content. Respond with only 'positive', 'negative', or 'neutral'.

Content:
\"\"\"
{content}
\"\"\"
Sentiment:'''
    sentiment = llama_prompt(prompt).lower()
    state.sentiment = sentiment
    return state
