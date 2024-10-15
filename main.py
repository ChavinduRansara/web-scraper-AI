import streamlit as st
from scrape import scrape, extract_content, clean_body, split_dom_content

st.title("Web Scraper")
url = st.text_input("Enter a Website URL: ")

if st.button("Scrape Site"):
    st.write("Scraping the website")
    result = scrape(url)
    
    body_content = extract_content(result)

    clean_content = clean_body(body_content)

    st.session_state.dom_content = clean_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", clean_content, height=300)