import requests

TELEGRAM_TOKEN = "8455203007:AAGJFfVHQaVTh5oxFUe4BHqfMacpEEyjOnc"
TELEGRAM_CHAT_ID = "6015392896"

message = "✅ Hello Rahul! Your diet reminder bot is working 🥗"

requests.post(
    f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage",
    data={"chat_id": TELEGRAM_CHAT_ID, "text": message}
)
