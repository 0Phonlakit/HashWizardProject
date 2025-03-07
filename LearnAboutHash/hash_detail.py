import tkinter as tk
from tkinter import ttk
import json

with open("hash_data.json", "r", encoding="utf-8") as file:
    hash_descriptions = json.load(file)

current_language = "th"

def switch_language():
    global current_language
    current_language = "en" if current_language == "th" else "th"
    lang_button.config(text="Thai" if current_language == "en" else "English")

def show_info():
    selected_algo = algorithmCombo.get()
    data = hash_descriptions.get(selected_algo, {"th": {"description": "No data", "hash-mode": "N/A", 
                                                        "bit-length": "N/A", "security" : "N/A", "usage": "N/A"}})
    
    info_window = tk.Toplevel(root)
    info_window.title(f"Data: {selected_algo}")
    info_window.geometry("550x350")

    label = tk.Label(info_window, text=f"{selected_algo} Algorithm", font=("Arial", 12, "bold"))
    label.pack(pady=5)

    text_area = tk.Text(info_window, wrap="word", height=15, width=60, font=("Arial", 10))
    text_area.pack(padx=10, pady=5)

    text_area.insert(tk.END, f"Hash Mode: {data[current_language]['hash-mode']}\n\n")
    text_area.insert(tk.END, f"Bit-Length : {data[current_language]['bit-length']} Bit\n\n")
    text_area.insert(tk.END, f"Security : {data[current_language]['security']}\n\n")
    text_area.insert(tk.END, f"Usage :{data[current_language]['usage']}\n\n")
    text_area.insert(tk.END, f"Description: {data[current_language]['description']}\n\n")
    text_area.config(state="disabled")

    btn_close = tk.Button(info_window, text="Close", command=info_window.destroy)
    btn_close.pack(pady=5)

root = tk.Tk()
root.title("Hash Algorithm Data")
root.geometry("350x200")

title = tk.Label(root, text="Select Hash Algorithm", font=("Arial", 12, "bold"))
title.pack(pady=5)

algorithmCombo = ttk.Combobox(root, values=list(hash_descriptions.keys()))
algorithmCombo.pack(pady=5)
algorithmCombo.current(0)

btnInfo = tk.Button(root, text="Algorithm Data", command=show_info)
btnInfo.pack(pady=10)

lang_button = tk.Button(root, text="English", command=switch_language)
lang_button.pack(pady=5)

root.mainloop()
