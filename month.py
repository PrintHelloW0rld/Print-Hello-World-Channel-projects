import tkinter as tk
from tkinter import ttk
import time
import threading

# List of months
months = ["Select current Month","January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]

funny_texts = [
    "Consulting astrologers...",
    "Missed call received from aliens...",
    "Going Physical with code...",
    "Hacking NASA for data...",
    "Checking Zomato discounts...",
    "Loading next month..."
]

# Function to predict next month
def predict_next_month():
    selected_month = month_combo.get()
    if selected_month == "":
        result_label.config(text="Please select a month first!")
        return
    
    # Show fake loading with funny messages
    def loading():
        for text in funny_texts:
            result_label.config(text=text)
            time.sleep(2)
        # Get next month
        next_index = (months.index(selected_month) + 1) % 12
        result_label.config(text=f" Next Month will be: {months[next_index]}")

    # Run loading in a separate thread (so GUI doesn’t freeze)
    threading.Thread(target=loading).start()

# GUI setup
root = tk.Tk()
root.title("Predict Your Next Month")
root.geometry("350x250")

title_label = tk.Label(root, text="Predict Your Next Month", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

month_combo = ttk.Combobox(root, values=months, state="readonly", font=("Arial", 12))
month_combo.pack(pady=5)

predict_button = tk.Button(root, text="Predict Next Month", command=predict_next_month,
                           bg="blue", fg="white", font=("Arial", 12, "bold"))
predict_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()
