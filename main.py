import tkinter as tk
from tkinter import ttk, messagebox
from hash_utils import EncryptText, DecryptText

def process():
    text = textEntry.get().strip()
    algorithm = algorithmCombo.get()
    salt = saltEntry.get().strip() if algorithm == "HMAC-SHA1" else None
    
    try:
        if mode.get() == "Encrypt":
            result = EncryptText(text, algorithm, salt)
        else:
            result = DecryptText(text, algorithm, salt)
        
        outputEntry.config(state="normal")
        outputEntry.delete(1.0, tk.END)  
        outputEntry.insert(tk.END, result)  
        outputEntry.config(state="disabled") 
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI
root = tk.Tk()
root.title("Hash Wizard 🪄")
root.geometry("400x350")

# Title
title = tk.Label(root, text="Hash Wizard", font=("Comic Sans MS", 15, "bold"))
title.pack()

# Select mode (Encrypt / Decrypt)
mode = tk.StringVar(value="Encrypt")
frame = tk.Frame(root)
frame.pack(pady=5)
tk.Radiobutton(frame, text="Encrypt", variable=mode, value="Encrypt").pack(side=tk.LEFT, padx=10)
tk.Radiobutton(frame, text="Decrypt", variable=mode, value="Decrypt").pack(side=tk.LEFT, padx=10)

# Select Algorithm
tk.Label(root, text="Algorithm:").pack()
algorithmCombo = ttk.Combobox(root, values=["MD5", "SHA1", "SHA2_224", "SHA2-256", "SHA2-512", "HMAC-SHA1"])
algorithmCombo.pack()
algorithmCombo.current(0)

# Input Text
tk.Label(root, text="Text / Hash:").pack()
textEntry = tk.Entry(root, width=50)
textEntry.pack()

# Salt (HMAC-SHA1 Only) Entry 
tk.Label(root, text="Salt (HMAC-SHA1 Only):").pack()
saltEntry = tk.Entry(root, width=50)
saltEntry.pack()

# Process Button
btnProcess = tk.Button(root, text="Process", command=process)
btnProcess.pack(pady=10)

#  Output
outputText = tk.StringVar()
tk.Label(root, text="Output:").pack()
readonlyBG = root.cget("bg")
outputEntry = tk.Text(root, width=42, height=3, state="disabled", font=("Arial", 9), bg=readonlyBG) 
outputEntry.pack()

# Enter to run process
root.bind('<Return>', lambda event: process())

root.mainloop()
