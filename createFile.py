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
            "Time": ["07:30 AM", "10:00 AM", "01:00 PM", "03:30 PM", "06:30 PM", "08:30 PM"],
            "Meal": ["Breakfast", "Mid-Morning Snack", "Lunch", "Afternoon Snack", "Pre-Workout Snack", "Dinner"],
            "Message": [
                "Oats porridge with milk, banana, peanut butter 🍌🥛🥜 + 1 boiled egg 🥚",
                "Handful of mixed nuts (almonds, walnuts) 🥜 and 1 glass fresh fruit juice 🍊",
                "Brown rice, homemade chicken curry 🍗, spinach or broccoli 🥦, cucumber salad 🥒",
                "Greek yogurt or curd with honey 🍯 and seasonal fruits 🍎🍓",
                "Banana or apple + 1 scoop whey protein or peanut butter toast 🍌🍞",
                "Grilled fish or paneer, quinoa or whole wheat chapati 🌾, sautéed veggies 🥦🥕, 1 glass milk 🥛"
            ]
        }


        # Create DataFrame and save to Excel
        pd.DataFrame(data).to_excel(FILE_NAME, index=False)

        print(f"✅ '{FILE_NAME}' created successfully!")
        return True

    except Exception as e:
        print(f"❌ Failed to create '{FILE_NAME}': {e}")
        return False

