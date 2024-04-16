import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
    BASE_URL = "https://interaction24.ixda.org/"
    TOKEN_PICKLE_FILENAME = "token"
    GOOGLE_SHEET_RANGE = "List 1!A1:H50"
