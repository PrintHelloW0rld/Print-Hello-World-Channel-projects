import tkinter as tk
import time
import threading
import random
from tkVideoPlayer import TkinterVideo  # pip install tkVideoPlayer

def start_scan():
    result_label.config(text="🔍 Scanning for aliens...", fg="blue")
    scan_button.config(state="disabled")
    
    def process():
        # Fake scanning animation
        for i in range(5):
            result_label.config(text=f"🔍 Scanning... {'.' * (i % 3 + 1)}")
            time.sleep(0.7)
        
        # Fake signal received
        result_label.config(text="📡 Signal received...", fg="green")
        time.sleep(1.5)

        # Show funny message
        messages = [
            "👽 Alien found in your room!",
            "🛸 UFO detected above your house!",
            "👾 Alien hacked your WiFi!",
            "🛰️ NASA is tracking your PC...",
            "⚠️ Alien invasion in progress!"
        ]
        result = random.choice(messages)
        result_label.config(text=result, fg="red")

        # Play video (passport size under the button)
        video_label.pack(pady=10)
        videoplayer.load("alien.mp4.mp4")  # your uploaded video file
        videoplayer.play()

        scan_button.config(state="normal")

    threading.Thread(target=process).start()

# Main window
root = tk.Tk()
root.title("Alien Detector")
root.geometry("500x500")
root.config(bg="black")

# Heading
title = tk.Label(root, text="🛸 Alien Detector 3000 🛸", font=("Arial", 16, "bold"), fg="lime", bg="black")
title.pack(pady=20)

# Scan Button
scan_button = tk.Button(root, text="Start Scan", font=("Arial", 14), command=start_scan, bg="lime", fg="black")
scan_button.pack(pady=20)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14), fg="white", bg="black")
result_label.pack(pady=20)

# Video player (hidden until scan ends)
video_label = tk.Frame(root, bg="black")
videoplayer = TkinterVideo(video_label, scaled=True, width=200, height=150)
videoplayer.pack()

root.mainloop()
