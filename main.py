import streamlit as st
import pandas as pd
import openai
import requests
from bs4 import BeautifulSoup

openai.api_key = "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"

def search(query):
    url = f"https://www.bing.com/search?q={query}"
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    return [r.get_text() for r in soup.find_all('p')][:5]

def parse(content, query):
    prompt = f"Extract info based on '{query}' from the following content:\n\n{content}"
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return res['choices'][0]['message']['content'].strip()

st.title("AI Retrieval Dashboard")

file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.write("Uploaded Data", df)
    
    col = st.selectbox("Select column for search:", df.columns)
    query = st.text_input("Enter search query")

    if st.button("Run Search"):
        res = []
        for item in df[col]:
            search_res = search(f"{item} {query}")
            info = parse(" ".join(search_res), query)
            res.append({"Entity": item, "Extracted Info": info})
        
        res_df = pd.DataFrame(res)
        st.write("Search Results", res_df)
        st.download_button("Download Results as CSV", res_df.to_csv(index=False), "results.csv")
