import requests
import re
from telegram import Bot
import datetime

import os 

BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"

def fetch_price():
    url = "https://kripto.bilira.co/market/BMMF_TRYB"
    html = requests.get(url).text
    # crude regex extraction for the quote value
    match = re.search(r'(\d+,\d+)\s*TRYB', html)
    return match.group(1) if match else "N/A"

def main():
    price = fetch_price()
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    text = f"📈 BMMF/TRYB quote at {now}: {price}"
    Bot(token=BOT_TOKEN).send_message(chat_id=CHAT_ID, text=text)

if __name__ == "__main__":
    main()
