# Web Scraper with Language Model Parsing

This project is a web scraping tool built with Python, Selenium, BeautifulSoup, and Streamlit, integrated with OllamaLLM to parse specific content from scraped websites based on user descriptions. The tool allows users to input a URL, scrape the content, clean the DOM, and parse meaningful information using natural language instructions.

## Features

- **Scrape Web Content**: Automatically scrape any website using Selenium.
- **Clean DOM Content**: Extract and clean the body content of a web page, removing unnecessary scripts and styles.
- **Parse Content**: Utilize the Ollama language model (LLM) to extract specific information from the scraped content based on user queries.
- **Streamlit Interface**: Simple and interactive web interface to input URLs, view DOM content, and parse the required information.

## Project Structure

```bash
.
├── main.py              # Streamlit front-end for interacting with the scraper and parser
├── scrape.py            # Functions for scraping and cleaning the web content
├── parse.py             # Parsing the DOM chunks using the Ollama LLM
├── requirements.txt     # Python dependencies for the project
└── README.md            # Project description and usage instructions
```

## Installation

1. Clone the repository:
2. Install dependencies:
3. Install and Configure Selenium:
4. CUDA and GPU Setup:

    If you plan to use a GPU for faster model inference, ensure that you have CUDA and cuDNN properly installed. Follow the [CUDA Installation Guide](https://developer.nvidia.com/cuda-downloads) if necessary.
