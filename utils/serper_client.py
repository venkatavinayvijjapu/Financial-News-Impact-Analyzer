# import os
# import requests

# API_KEY = os.getenv("SERPER_API_KEY")  # Set this in your .env or system env

# def fetch_financial_news(topic: str):
#     url = "https://google.serper.dev/news"
#     headers = {"X-API-KEY": API_KEY}
#     data = {"q": topic}

#     response = requests.post(url, json=data, headers=headers)
#     articles = response.json().get("news", [])

#     # Choose first article with meaningful content
#     for article in articles:
#         if article.get("title") and article.get("snippet"):
#             return {
#                 "article_id": article["link"].split("/")[-1][:20],
#                 "headline": article["title"],
#                 "content": article["snippet"],
#                 "published_at": article.get("date", "")
#             }
#     return None


# import os
# import requests
# from langchain_community.utilities import GoogleSerperAPIWrapper


# API_KEY = "ea6786617d5200739025a4cec1f15116664957b0e34e7d61c23ad959f09232cd"

# search = GoogleSerperAPIWrapper(api_key=API_KEY)

# def fetch_financial_news(topic: str):
#     url = "https://google.serper.dev/news"
#     headers = {"X-API-KEY": API_KEY}
#     data = {"q": topic}
#     print(data)
#     response = requests.post(url, json=data, headers=headers)
#     articles = response.json().get("news", [])
#     print(articles)

#     for article in articles:

#         title = article.get("title")
#         snippet = article.get("snippet", article.get("description", ""))
#         if title and snippet:
#             return {
#                 "headline": title,
#                 "content": snippet,
#                 "published_at": article.get("date", "")
#             }
#     return None


# # def fetch_financial_news(topic: str):
# #     url = "https://google.serper.dev/news"
# #     headers = {"X-API-KEY": API_KEY}
# #     data = {"q": topic}

# #     response = requests.post(url, json=data, headers=headers)
# #     articles = response.json().get("news", [])

# #     for article in articles:
# #         if article.get("title") and article.get("snippet"):
# #             return {
# #                 "headline": article["title"],
# #                 "content": article["snippet"],
# #                 "published_at": article.get("date", "")
# #             }
# #     return None


from langchain_community.utilities import GoogleSerperAPIWrapper
import requests
API_KEY = "9312835884bbc58d3a12b82ef1d30ec9929e9b3d"
import os
os.environ["SERPER_API_KEY"] = API_KEY

# search = GoogleSerperAPIWrapper(api_key=API_KEY)

def fetch_financial_news(query):
    url = "https://google.serper.dev/news"
    headers = {
        "X-API-KEY": os.getenv("SERPER_API_KEY"),  # 🛑 Replace this
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

# def fetch_financial_news(topic: str):
#     search = GoogleSerperAPIWrapper(
#         # type="search",  # 👈 this is critical to get news results,
#         serper_api_key=API_KEY
#     )
#     results = search.results(topic)

#     for article in results.get("news", []):
#         if article.get("title") and article.get("snippet"):
#             return {
#                 "headline": article["title"],
#                 "content": article["snippet"],
#                 "published_at": article.get("date", "")
#             }

#     return None
