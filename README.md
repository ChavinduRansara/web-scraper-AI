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
   ```
   git clone https://github.com/ChavinduRansara/web-scraper-AI.git
   cd web-scraper-AI
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Install and Configure Selenium:
   
   Download the appropriate WebDriver for your browser and place it in the project directory. For example, you can download the ChromeDriver from [here](https://googlechromelabs.github.io/chrome-for-testing/#stable).

   Ensure that the path to the driver is correctly set in the scrape.py file:

   ```
   chrome_driver_path = "./chromedriver.exe"

   ```

5. CUDA and GPU Setup:

    If you plan to use a GPU for faster model inference, ensure that you have CUDA and cuDNN properly installed. Follow the [CUDA Installation Guide](https://developer.nvidia.com/cuda-downloads) if necessary.

## Start the Streamlit Application

```
streamlit run main.py

```
## Dependencies

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [Selenium](https://www.selenium.dev/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [OllamaLLM](https://ollama.ai/)

## Troubleshooting

- **CUDA Errors**: If you encounter CUDA errors, ensure you have installed the correct version of CUDA and that it is added to your system's PATH. You can also switch to CPU-based processing if GPU resources are unavailable or insufficient.
    
- **Selenium WebDriver Issues**: Ensure that the correct WebDriver (e.g., ChromeDriver) is installed and compatible with your browser version.

