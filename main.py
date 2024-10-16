import streamlit as st
from scrape import scrape, extract_content, clean_body, split_dom_content
from parse import parse;

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

if "dom_content" in st.session_state:
    parse_descrtiption = st.text_area("Describe what you want to parse?")

    if st.button("Parse Content"):
        if parse_descrtiption:
            st.write("Parsing content")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            result = parse(dom_chunks, parse_descrtiption)
            st.write(result)