import requests

def fetch_google_news(query):
    url = "https://google.serper.dev/news"
    headers = {
        "X-API-KEY": "9312835884bbc58d3a12b82ef1d30ec9929e9b3d",  # 🛑 Replace this
        "Content-Type": "application/json"
    }
    payload = {
        "q": query
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        data = response.json()
        results = data.get("news", [])
        parsed = []
        for article in results:
            parsed.append({
                "headline": article.get("title"),
                "content": article.get("snippet"),
                "published_at": article.get("date", "")
            })
        return parsed
    else:
        print("Error:", response.status_code, response.text)
        return []

# Test
articles = fetch_google_news("Tesla earnings")
print(articles)
