import streamlit as st
import requests

st.set_page_config(page_title="AI News Dashboard", layout="wide")

st.title("🤖 AI News Dashboard")

API_KEY = st.secrets["NEWS_API_KEY"]

company = st.sidebar.selectbox(
    "Select Topic",
    [
        "artificial intelligence",
        "OpenAI",
        "Google AI",
        "Anthropic",
        "NVIDIA AI",
        "Microsoft AI"
    ]
)

search_term = company

url = (
    f"https://newsapi.org/v2/everything?"
    f"q={search_term}&"
    f"language=en&"
    f"sortBy=publishedAt&"
    f"pageSize=10&"
    f"apiKey={API_KEY}"
)

response = requests.get(url)

data = response.json()

if data["status"] == "ok":

    articles = data["articles"]

    for article in articles:

        st.subheader(article["title"])

        st.write(
            f"📰 Source: {article['source']['name']}"
        )

        st.write(
            article.get(
                "description",
                "No description available."
            )
        )

        
        st.markdown(
            f"[Read Full Article]({article['url']})"
        )

        st.divider()

else:
    st.error("Failed to fetch news")