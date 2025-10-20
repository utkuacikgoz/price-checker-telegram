import os
import asyncio
from telegram import Bot
from telegram.error import TelegramError
from pyppeteer import launch

# === Config ===
BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
URL = "https://kripto.bilira.co/market/BMMF_TRYB"

async def take_screenshot(url, filename="screenshot.png"):
    """Launch a headless browser, capture a screenshot, and return filename."""
    browser = await launch(
        headless=True,
        args=["--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage"],
    )
    page = await browser.newPage()
    await page.setViewport({"width": 1366, "height": 768})
    print(f"📸 Loading {url} ...")
    await page.goto(url, {"waitUntil": "networkidle2", "timeout": 60000})
    await page.screenshot({"path": filename, "fullPage": True})
    await browser.close()
    print("✅ Screenshot captured.")
    return filename

async def main():
    if not BOT_TOKEN or not CHAT_ID:
        print("❌ Missing BOT_TOKEN or CHAT_ID environment variable.")
        return

    bot = Bot(BOT_TOKEN)

    try:
        filename = await take_screenshot(URL)
        with open(filename, "rb") as f:
            await bot.send_photo(
                chat_id=CHAT_ID,
                photo=f,
                caption=f"📊 Bilira Market Snapshot\n{URL}"
            )
        print("✅ Screenshot sent successfully to Telegram.")
    except TelegramError as e:
        print(f"❌ Telegram error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
