import tkinter as tk
from tkinter import messagebox

def start_countdown():
    try:
        time_left = int(entry.get())
        countdown(time_left)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer.")

def countdown(seconds):
    if seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_display.config(text=f'{mins:02d}:{secs:02d}')
        root.after(1000, countdown, seconds - 1)
    else:
        timer_display.config(text="00:00")
        messagebox.showinfo("Time's Up", "The countdown has finished!")

root = tk.Tk()
root.title("Countdown Timer")

entry = tk.Entry(root, width=5, font=("Helvetica", 24))
entry.pack(pady=20)

start_button = tk.Button(root, text="Start Countdown", command=start_countdown)
start_button.pack(pady=20)

timer_display = tk.Label(root, text="00:00", font=("Helvetica", 48))
timer_display.pack(pady=20)

root.mainloop()
