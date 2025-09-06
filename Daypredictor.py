import tkinter as tk
import random
import time
import threading

def predict_next_day():
    result_label.config(text=" Calculating next day...", fg="black")
    predict_button.config(state="disabled", text="⏳ Loading...", bg="gray")

    def process():
        # Funny loading animations
        animations = [
            " Checking your calendar...",
            " Hacking Nasa for data...",
            " Analysing chrome search history...",
            " Dhoni Announced to play one more ipl...",
            " Predicting tomorrow..."
        ]

        for text in animations:
            result_label.config(text=text)
            time.sleep(2.0)

        # List of days
        days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        # Get selected day
        current_day = day_var.get()
        if current_day in days:
            next_day = days[(days.index(current_day) + 1) % 7]
            funny_outputs = [
                f" Your next day will be: {next_day}!"
               
            ]
            result_label.config(text=random.choice(funny_outputs))
        else:
            result_label.config(text="⚠️ Please select a valid day!")

        # Reset button back to green
        predict_button.config(state="normal", text="Predict Next Day", bg="green", fg="white")

    threading.Thread(target=process, daemon=True).start()


# Main Window
root = tk.Tk()
root.title("Next Day Predictor")
root.geometry("400x300")

title = tk.Label(root, text=" Next Day Predictor ", font=("Arial", 16, "bold"))
title.pack(pady=20)

# Dropdown for selecting day
day_var = tk.StringVar()
day_var.set("Select a day")
days_menu = tk.OptionMenu(root, day_var, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
days_menu.pack(pady=10)

# Green Predict button
predict_button = tk.Button(root, text="Predict Next Day", font=("Arial", 14), command=predict_next_day, bg="green", fg="white")
predict_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()
