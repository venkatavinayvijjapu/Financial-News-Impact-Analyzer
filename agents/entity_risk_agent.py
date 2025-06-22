from utils.llm_client import llama_prompt

def run(state: dict) -> dict:
    content = state.cleaned_content
    prompt = f'''Identify any risks in the following financial news. Respond with a list such as ['regulatory', 'geopolitical', 'financial', 'none'].

Content:
\"\"\"
{content}
\"\"\"
Risks:'''
    risks_raw = llama_prompt(prompt).lower()
    try:
        risks = eval(risks_raw) if isinstance(risks_raw, str) else ["none"]
    except:
        risks = ["none"]
    state.risks = risks
    return state
