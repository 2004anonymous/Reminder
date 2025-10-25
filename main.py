import pandas as pd
import schedule
import time
from datetime import datetime
import requests
from createFile import createDietScheduleFile


# ============ CONFIG ============
TELEGRAM_TOKEN = "8455203007:AAGJFfVHQaVTh5oxFUe4BHqfMacpEEyjOnc"
TELEGRAM_CHAT_ID = "6015392896"
FILE_PATH = "diet_schedule.xlsx"
# ================================

def send_telegram(meal, message):
    """Send a Telegram message."""
    text = f"🍽️ *{meal} Reminder!*\n{message}\n⏰ {datetime.now().strftime('%I:%M %p')}"
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    try:
        requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": text, "parse_mode": "Markdown"})
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Sent: {meal}")
    except Exception as e:
        print(f"❌ Telegram error: {e}")

def schedule_jobs():
    """Load Excel and schedule reminders."""
    df = pd.read_excel(FILE_PATH)
    for _, row in df.iterrows():
        try:
            t = datetime.strptime(row["Time"].strip(), "%I:%M %p").strftime("%H:%M")
            schedule.every().day.at(t).do(send_telegram, meal=row["Meal"], message=row["Message"])
            print(f"✅ Scheduled {row['Meal']} at {row['Time']}")
        except Exception as e:
            print(f"⚠️ Skipped {row['Meal']}: {e}")

if __name__ == "__main__":
    # Create the diet schedule Excel file
    if createDietScheduleFile():
        print("File created successfully. Proceeding with scheduling...")
        print("🚀 Diet Reminder Bot Started...")
        schedule_jobs()

        while True:
            schedule.run_pending()
            time.sleep(10)
    else:
        print("File creation failed. Exiting.")
