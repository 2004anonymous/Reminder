import pandas as pd
import os

FILE_NAME = "diet_schedule.xlsx"

def createDietScheduleFile():
    try:
        # Delete existing file if it exists
        if os.path.exists(FILE_NAME):
            os.remove(FILE_NAME)
            print(f"🗑️ Existing file '{FILE_NAME}' deleted.")

        # Sample diet schedule
        data = {
            "Time": ["07:30 AM", "10:00 AM", "01:00 PM", "03:30 PM", "06:00 PM", "08:30 PM"],
            "Meal": ["Breakfast", "Mid-Morning Snack", "Lunch", "Afternoon Snack", "Pre-Workout Snack", "Dinner"],
            "Message": [
                "Good morning! This is Rahul, your personal assistant. It’s time for breakfast — enjoy a wholesome bowl of oats porridge with milk, banana, and peanut butter 🍌🥛🥜, along with one boiled egg 🥚 to start your day strong.",
                "Hey there! Rahul here. It’s time for your mid-morning snack — have a handful of mixed nuts (almonds and walnuts) 🥜 and a glass of fresh fruit juice 🍊 to keep your energy up.",
                "Hi! Rahul checking in. It’s lunchtime — enjoy some brown rice with homemade chicken curry 🍗, spinach or broccoli 🥦, and a refreshing cucumber salad 🥒 for a balanced meal.",
                "Hello again! Rahul here. Time for your afternoon snack — treat yourself to some Greek yogurt or curd with a drizzle of honey 🍯 and a few seasonal fruits 🍎🍓.",
                "Hey! Rahul reminding you — it’s time for your pre-workout snack. Have a banana or apple 🍌🍎 with one scoop of whey protein, or a slice of peanut butter toast 🍞 for a quick energy boost.",
                "Good evening! Rahul here. Dinner time — enjoy grilled fish or paneer, quinoa or whole wheat chapati 🌾, sautéed veggies 🥦🥕, and finish with a glass of milk 🥛 for recovery and rest."
            ]
        }


        # Create DataFrame and save to Excel
        pd.DataFrame(data).to_excel(FILE_NAME, index=False)

        print(f"✅ '{FILE_NAME}' created successfully!")
        return True

    except Exception as e:
        print(f"❌ Failed to create '{FILE_NAME}': {e}")
        return False

