# AI Retrieval Dashboard

This project implements an AI-powered dashboard that allows users to upload a CSV file, search for relevant information online, and extract specific data using OpenAI's GPT model. The dashboard leverages Bing search results and the GPT model to process and retrieve information based on user queries.

## Features
- **CSV File Upload**: Upload a CSV file containing data that needs to be searched.
- **Search Query**: Enter a search query to find relevant information from the web.
- **Column Selection**: Choose which column in the uploaded CSV to perform searches on.
- **AI-powered Data Extraction**: GPT-3.5 turbo model extracts relevant information based on the entered query.
- **Results Display**: View the extracted data in a tabular format.
- **Download Results**: Download the extracted data as a CSV file.

## Requirements
- `streamlit`: For creating the dashboard UI.
- `pandas`: For handling CSV data.
- `openai`: To interact with OpenAI's GPT API for text extraction.
- `requests`: For making HTTP requests to the Bing search engine.
- `beautifulsoup4`: For parsing HTML content from search results.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ai-retrieval-dashboard.git
Navigate to the project directory:

cd ai-retrieval-dashboard
Create and activate a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the required dependencies:

pip install -r requirements.txt
Usage
Start the Streamlit app:

streamlit run app.py
Upload your CSV file through the Streamlit interface.

Select the desired column for search, enter your search query, and click Run Search.

View the results of the AI-powered search and download them as a CSV file if needed.

API Key
You need an OpenAI API key to interact with the GPT model. Make sure to replace the openai.api_key in app.py with your own key.
openai.api_key = "your-openai-api-key"
License
This project is licensed under the MIT License - see the LICENSE file for details.

### How to Use:
- Replace `your-username` with your actual GitHub username in the clone URL.
- Add a `requirements.txt` file with the following contents:
streamlit pandas openai requests beautifulsoup4
