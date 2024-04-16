import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from config import Config


class GoogleSheet:
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    service = None

    def __init__(self):
        creds = None
        if os.path.exists(Config.TOKEN_PICKLE_FILENAME + '.pickle'):
            with open(Config.TOKEN_PICKLE_FILENAME + '.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open(Config.TOKEN_PICKLE_FILENAME + '.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('sheets', 'v4', credentials=creds)

    def update_range_values(self, spreadsheet_id: str, google_sheet_range: str, values: list[tuple[str]]):
        data = [{
            'range': google_sheet_range,
            'values': values
        }]
        body = {
            'valueInputOption': 'USER_ENTERED',
            'data': data
        }
        self.service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheet_id, body=body).execute()


def write_to_google_sheets(spreadsheet_id: str, field_names: tuple[str], values: list[tuple[str]]):
    gs = GoogleSheet()
    gs.update_range_values(spreadsheet_id, Config.GOOGLE_SHEET_RANGE, [field_names] + values)
