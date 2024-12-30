from typing import Dict, Any
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Google Sheets Configuration
SHEET_ID = os.getenv('SHEET_ID')
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Sheet Configuration
SHEET_CONFIG: Dict[str, Any] = {
    'range_name': 'Sheet1!A:E',  # Using columns A through E
    'value_input_option': 'USER_ENTERED',
    'insert_data_option': 'INSERT_ROWS',
}

# Credentials Configuration
CREDENTIALS_FILE = 'credentials.json'
TOKEN_FILE = 'token.json'

# Logging Configuration
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
LOG_FILE = 'sheets_automation.log'

# Column mapping for form data
COLUMN_MAPPING = {
    'timestamp': 'A',    # Submission timestamp
    'name': 'B',         # 이름
    'blog_link': 'C',    # 블로그링크
    'til_date': 'D',     # TIL 작성 일자
    'weather': 'E',      # 오늘의 날씨
}

# Weather options mapping
WEATHER_OPTIONS = {
    'sunny': '맑음 (기분 좋아요)',
    'cloudy': '흐림 (그냥 그래요)',
    'rainy': '비 (힘들어요)',
    'snowy': '천둥/번개 (궂일이에요)'
}