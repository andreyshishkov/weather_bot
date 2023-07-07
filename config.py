import os
from dotenv import load_dotenv
load_dotenv()

WEATHER_TOKEN = os.environ.get('WEATHER_TOKEN')
TELEGRAM_TOKEN = os.environ.get('TELEGRAM_TOKEN')
