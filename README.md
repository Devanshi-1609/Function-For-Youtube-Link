# Function For Youtube Link

**Author**: Devanshi Modak
**Date**: August 27, 2025

## Description
Function For Youtube Link is a Python script that retrieves YouTube video links based on a user-provided search query. It uses the `youtubesearchpython` library to perform the search and returns a list of up to five video URLs. This project is designed for simplicity and ease of use, suitable for integration into larger applications or standalone use.

## Installation

### Using Python Virtual Environment
1. Clone or download the project.
2. Navigate to the project directory:
    ```bash
    cd youtube-link-function
    ```
3. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Using Conda
1. Clone or download the project.
2. Navigate to the project directory:
    ```bash
    cd youtube-link-function
    ```
3. Create and activate a Conda environment:
    ```bash
    conda env create -f environment.yml
    conda activate youtube-link-function
    ```

## Usage
1. Run the script:
    ```bash
    python youtube_search.py
    ```
2. Enter a search query when prompted (e.g., "Python tutorials").
3. The script will display up to five YouTube video links related to the query.

## Dependencies
- Python 3.8+
- youtubesearchpython

## Project Structure
```
FunctionForYoutubeLink/
├── src/
│   └── main.py
├── README.md
├── environment.yml
└── requirements.txt

```

## Notes
- Ensure an active internet connection, as the script fetches results from YouTube.
- The `youtubesearchpython` library may have rate limits or depend on YouTube's API availability.
- For production use, consider adding error handling for network issues or invalid queries.
