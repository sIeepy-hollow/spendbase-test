# Scrapping data project
#### This project is designed to scrape data about speakers from the https://interaction24.ixda.org/, process this data, and then write it to a local JSON file,
#### CSV file, and a Google Sheet. The data includes names, roles, image URLs, and social media links of the speakers.
####
## Architecture:
- main.py - This script scrapes the data, processes it, and calls the function to write data to Google Sheets.
- google_api.py - Contains the class GoogleSheet for handling operations to Google Sheets.
- config.py - Contains configuration constants.

## Technologies Used:
- requests. Lib for requesting urls from internet.
- BeautifulSoup4. Best lib for parsing HTML.
- pandas. Pandas was used to avoid writing custom code for formatting data and saving it to CSV and JSON files, as well as to save time.
- google-auth, google-auth-oauthlib, google-api-python-client. Was used for updating google spreadsheet.

## You need: 
- Python 3.11
- credentials.json file from google API
- .env file like: SPREADSHEET_ID=Your ID of Spreadsheet


## Run app:
- create and activate virtual environment
- pip install -r requirements.txt
- python main.py