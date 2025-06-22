from together import Together
import os

client = Together(api_key=os.getenv("TOGETHER_API_KEY"))

def llama_prompt(prompt: str) -> str:
    response = client.chat.completions.create(
        model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=500,
    )
    return response.choices[0].message.content.strip()
