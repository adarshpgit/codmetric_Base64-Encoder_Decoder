import tkinter as tk
from tkinter import messagebox, scrolledtext
import base64

# Encoding function
def encode_text():
    user_input = input_text.get("1.0", tk.END).strip()
    if not user_input:
        messagebox.showwarning("Warning", "Input text cannot be empty!")
        return
    try:
        encoded_bytes = base64.b64encode(user_input.encode("utf-8"))
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, encoded_bytes.decode("utf-8"))
    except Exception as e:
        messagebox.showerror("Error", f"Encoding failed: {str(e)}")

# Decoding function
def decode_text():
    user_input = input_text.get("1.0", tk.END).strip()
    if not user_input:
        messagebox.showwarning("Warning", "Input text cannot be empty!")
        return
    try:
        decoded_bytes = base64.b64decode(user_input.encode("utf-8"))
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, decoded_bytes.decode("utf-8"))
    except Exception as e:
        messagebox.showerror("Error", f"Decoding failed: {str(e)}")

# Clear both text areas
def clear_all():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

# GUI setup
window = tk.Tk()
window.title("🔐 Base64 Encoder/Decoder - CodMetric")
window.geometry("600x500")
window.config(bg="#1e1e1e")

title_label = tk.Label(window, text="Base64 Encoder/Decoder", font=("Arial", 18, "bold"), bg="#1e1e1e", fg="#00ff88")
title_label.pack(pady=10)

# Input box
tk.Label(window, text="Enter text:", bg="#1e1e1e", fg="#ffffff", font=("Arial", 12)).pack()
input_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=5, font=("Arial", 10))
input_text.pack(pady=5)

# Buttons
button_frame = tk.Frame(window, bg="#1e1e1e")
button_frame.pack(pady=10)

encode_btn = tk.Button(button_frame, text="Encode", command=encode_text, bg="#00ff88", fg="#000000", width=10, font=("Arial", 10, "bold"))
encode_btn.grid(row=0, column=0, padx=10)

decode_btn = tk.Button(button_frame, text="Decode", command=decode_text, bg="#00ff88", fg="#000000", width=10, font=("Arial", 10, "bold"))
decode_btn.grid(row=0, column=1, padx=10)

clear_btn = tk.Button(button_frame, text="Clear", command=clear_all, bg="#ff5555", fg="#ffffff", width=10, font=("Arial", 10, "bold"))
clear_btn.grid(row=0, column=2, padx=10)

# Output box
tk.Label(window, text="Result:", bg="#1e1e1e", fg="#ffffff", font=("Arial", 12)).pack()
output_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=60, height=5, font=("Arial", 10))
output_text.pack(pady=5)

# Run the GUI
window.mainloop()
