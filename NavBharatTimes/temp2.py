import os
import requests
import pdfplumber
from datetime import datetime, timedelta

def download_pdfs(start_date, end_date, page_count):
    base_url = "https://image.mepaper.navbharattimes.com/epaperimages/"
    
    # Ensure the output directories exist
    output_dir = "pdffolder"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    text_output_dir = "textfolder"
    if not os.path.exists(text_output_dir):
        os.makedirs(text_output_dir)

    # Convert date to string for iteration
    current_date = start_date
    while current_date <= end_date:
        date_str = convert_date_format(current_date)

        for page_number in range(0, page_count + 1):
            page_url = f"{base_url}{date_str}/{date_str}-md-de-{page_number}.pdf"
            print(f"Attempting to download: {page_url}")
            
            try:
                response = requests.get(page_url)
                if response.status_code == 200:
                    temp_pdf_path = f"{output_dir}/{date_str}_{page_number}.pdf"
                    with open(temp_pdf_path, 'wb') as f:
                        f.write(response.content)
                    print(f"Successfully downloaded {temp_pdf_path}")

                    # Extract text from the downloaded PDF
                    extract_text_from_pdf(temp_pdf_path, text_output_dir, date_str, page_number)
                else:
                    print(f"Failed to download page {page_number} for date {date_str} with status code {response.status_code}")
            except Exception as e:
                print(f"Exception occurred while downloading page {page_number} for date {date_str}: {e}")

        # Increment the date
        current_date = increment_date(current_date)

    print("All PDFs downloaded and processed successfully!")

def convert_date_format(date):
    date_format = "%Y%m%d"
    date_obj = datetime.strptime(str(date), date_format)
    return date_obj.strftime("%d%m%Y")

def increment_date(date):
    date_format = "%Y%m%d"
    date_obj = datetime.strptime(str(date), date_format)
    next_date_obj = date_obj + timedelta(days=1)
    return int(next_date_obj.strftime(date_format))

def extract_text_from_pdf(pdf_path, output_dir, date_str, page_number):
    with pdfplumber.open(pdf_path) as pdf:
        for page_index, page in enumerate(pdf.pages):
            article_texts = extract_articles(page)
            for i, article in enumerate(article_texts):
                article_filename = f"{output_dir}/{date_str}_{page_number}_article_{page_index}_{i}.txt"
                with open(article_filename, 'w', encoding='utf-8') as f:
                    f.write(article)
                print(f"Article extracted and saved to {article_filename}")

def extract_articles(page):
    # This is a naive implementation and needs to be adapted based on the structure of your newspaper
    articles = []
    text = page.extract_text()
    if text:
        # Assuming each article starts with a heading, followed by the content
        # This split might not work perfectly and might need regex or more advanced parsing
        potential_articles = text.split('\n\n')  # Split by double newlines
        current_article = ''
        for part in potential_articles:
            if part.isupper():  # This condition can be adjusted
                if current_article:
                    articles.append(current_article.strip())
                current_article = part + '\n'
            else:
                current_article += part + '\n'
        if current_article:
            articles.append(current_article.strip())
    return articles

# Example usage
start_date = 20240101
end_date = 20240102  # Changed to a smaller range for testing
page_count = 18
download_pdfs(start_date, end_date, page_count)
