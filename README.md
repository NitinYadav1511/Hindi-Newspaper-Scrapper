# Newspaper Dataset Generator for OCR Training

This project is part of an internship at IIT Bombay, aimed at building a newspaper dataset for training and testing OCR (Optical Character Recognition) models for Indic scripts. The project scrapes NavBharatTimes newspaper PDFs and extracts text to create a comprehensive dataset.

## Project Overview

The Newspaper Dataset Generator is designed to:
1. Download PDF versions of NavBharatTimes newspaper for specified date ranges.
2. Extract text from the downloaded PDFs.
3. Save both PDFs and extracted text in organized folders.

This dataset contributes to the development of OCR models for Indic scripts, a collaborative effort between IIT Bombay and IIIT Hyderabad.

## Features

- Scrape NavBharatTimes newspaper PDFs for given date ranges
- Extract text from PDFs and save as separate text files
- Organize data into PDF and text folders
- Customizable date range and page count for scraping

## Prerequisites

- Python 3.x
- `requests` library
- `pdfplumber` library

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/newspaper-dataset-generator.git
   cd newspaper-dataset-generator
   ```

2. Install the required dependencies:
   ```
   pip install requests pdfplumber
   ```

## Usage

1. Open the `temp2.py` file.
2. Modify the following parameters at the bottom of the file:
   ```python
   start_date = 20240101  # Format: YYYYMMDD
   end_date = 20240102    # Format: YYYYMMDD
   page_count = 18        # Number of pages to scrape per issue
   ```
3. Run the script:
   ```
   python temp2.py
   ```

The script will download PDFs to the `pdffolder` and extract text to the `textfolder`.

## Project Structure

- `temp2.py`: Main script for scraping and processing newspaper data
- `pdffolder/`: Directory where downloaded PDF files are stored
- `textfolder/`: Directory where extracted text files are stored

## Contributing

This project is part of an internship at IIT Bombay. For major changes or suggestions, please open an issue first to discuss what you would like to change.

## Contributor

This repository is maintained by [Nitin Yadav](https://github.com/NitinYadav1511).

## License

[MIT License](https://choosealicense.com/licenses/mit/)

## Acknowledgments

- IIT Bombay and IIIT Hyderabad for the opportunity to contribute to OCR development for Indic scripts
- NavBharatTimes for providing the source material

## Disclaimer

This project is for educational and research purposes only. Ensure you have the right to scrape and use the data from NavBharatTimes before deploying this script for any purpose other than personal research.
