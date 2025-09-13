import tkinter as tk
import time
import threading
import random
import os

def start_scan():
    result_label.config(text="Starting scan...", fg="black")
    scan_button.config(state="disabled")
    
    def process():
        animations = [
            " Scanning for aliens...",
            " Checking Swiggy discounts...",
            " Doing 69 position with Aliens...",
            " Dhoni announced to play one more ipl...",
            " Calibrating quantum mechanics..."
        ]

        # Show each funny animation
        for text in animations:
            result_label.config(text=text)
            time.sleep(1.5)

        # Final random alien message
        # messages = [
            
        #     " UFO detected above your house!",
           
        # ]
        # result_label.config(text=random.choice(messages))

        # Show alien video
        video_path = "alien.mp4.mp4"  # keep file in same folder
        try:
            os.startfile(video_path)  # works on Windows
        except Exception as e:
            result_label.config(text=f"Error: {e}")

        scan_button.config(state="normal")

    threading.Thread(target=process, daemon=True).start()

# Main window
root = tk.Tk()
root.title("Alien Detector")
root.geometry("400x300")

title = tk.Label(root, text=" Alien Detector 69 ", font=("Arial", 16, "bold"))
title.pack(pady=20)

scan_button = tk.Button(root, text="Start Scan", font=("Arial", 14), command=start_scan)
scan_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()
