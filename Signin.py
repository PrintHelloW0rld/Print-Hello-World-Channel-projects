import tkinter as tk
import random
import time
import threading

def open_signup_page():
    welcome_window.destroy()

    root = tk.Tk()
    root.title("Funny Sign Up")
    root.geometry("400x350")

    title = tk.Label(root, text=" Enter Your Phone Number", font=("Arial", 14, "bold"))
    title.pack(pady=20)

    phone_entry = tk.Entry(root, font=("Arial", 14), justify="center")
    phone_entry.pack(pady=20)

    slider_label = tk.Label(root, text=" Drag slider to type your number", font=("Arial", 10))
    slider_label.pack()

    slider = tk.Scale(root, from_=0, to=100, orient="horizontal", length=250)
    slider.pack(pady=10)

    def generate_number(event):
        random_number = "".join(str(random.randint(0, 9)) for _ in range(10))
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, random_number)

    slider.bind("<B1-Motion>", generate_number)

    result_label = tk.Label(root, text="", font=("Arial", 12))
    result_label.pack(pady=10)

    def submit_signup():
        submit_btn.config(state="disabled", text=" Loading...", bg="gray")

        def process():
            time.sleep(2)
            result_label.config(text="Verificatin is successful", fg="green")
            submit_btn.config(state="normal", text="Submit", bg="green", fg="white")

        threading.Thread(target=process, daemon=True).start()

    submit_btn = tk.Button(root, text="Submit", font=("Arial", 14), bg="green", fg="white", command=submit_signup)
    submit_btn.pack(pady=20)

    root.mainloop()


# First Welcome Window
welcome_window = tk.Tk()
welcome_window.title("Welcome")
welcome_window.geometry("300x200")

welcome_label = tk.Label(welcome_window, text="Click the signin button to continue", font=("Arial", 14))
welcome_label.pack(pady=30)

signup_button = tk.Button(welcome_window, text="Sign Up", font=("Arial", 14), command=open_signup_page, bg="green", fg="white")
signup_button.pack(pady=20)

welcome_window.mainloop()
