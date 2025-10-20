import os
import re
import sys
import logging
from telegram import Bot
from telegram.error import TelegramError

# === Validate Environment Variables ===
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

if not BOT_TOKEN:
    print("❌ ERROR: BOT_TOKEN environment variable is not set.")
    sys.exit(1)

if not re.match(r'^\d+:[A-Za-z0-9_-]{20,}$', BOT_TOKEN):
    print("❌ ERROR: BOT_TOKEN does not match expected format. Check your secret value in GitHub → Settings → Secrets → Actions.")
    sys.exit(1)

if not CHAT_ID:
    print("❌ ERROR: CHAT_ID environment variable is not set.")
    sys.exit(1)

# === Initialize Logging ===
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# === Initialize Bot ===
try:
    bot = Bot(token=BOT_TOKEN)
    logging.info("✅ Telegram Bot initialized successfully.")
except TelegramError as e:
    logging.error(f"❌ Failed to initialize Telegram Bot: {e}")
    sys.exit(1)

# === Example Bot Logic ===
def main():
    try:
        # Example message — replace this with your actual logic
        bot.send_message(chat_id=CHAT_ID, text="✅ Bilira Bot is running successfully!")
        logging.info("Message sent successfully.")
    except TelegramError as e:
        logging.error(f"❌ Telegram error while sending message: {e}")
        sys.exit(1)
    except Exception as e:
        logging.error(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
