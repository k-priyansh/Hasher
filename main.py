import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
from tkinter import font
from tkinter import ttk
# from core import encrypt_text
# from core import decrypt_text
from cryptography.fernet import Fernet
import csv
import os

## Load Widgets
app = ctk.CTk()
app.title("App.py")
# app.geometry("1280x720")  # 16:9 ratio dimensions
app.geometry("700x768")  

# Heading
heading_font = ("Poppins", 24, "bold")
heading_label = ctk.CTkLabel(app, text="App.py", font=heading_font)
heading_label.pack(pady=20)

# Define and place widgets
# Input Text
label_font = ("Poppins", 16)
input_label = ctk.CTkLabel(app, text="Input Text", font=label_font)
input_label.pack(pady=10)
input_entry = ctk.CTkEntry(app, placeholder_text="Enter Token", width=630, height=40, font=label_font)
input_entry.pack(pady=10)

# Key
key_label = ctk.CTkLabel(app, text="Key", font=label_font)
key_entry = ctk.CTkEntry(app, placeholder_text="Enter Key", width=630, height=40, font=label_font)
key_label.pack(pady=10)  # Show the Key label
key_entry.pack(pady=10)  # Show the Key entry field

# Some functions
# Encryptbutton
# encrypter function
def main_app_encrypt(encrypt_text):
    # Retrieve the input from the entry widget
    input_text = input_entry.get()
    # key_text = key_entry.get()  # Get the key from the key entry

    defaultkey = Fernet.generate_key()
    # Check if the key is empty and assign a default key if it is
    # if not key_text:  # If key_text is empty
    key_text = defaultkey  # Assign a default key

    encrypted_text = encrypt_text(input_text, key_text)
    # Dynamically create a variable (e.g., `dynamic_variable`) and assign the input value
    dynamic_variable = encrypted_text
    header = ["Input Text", "Key", "Output", "Message"]
    new_data = [input_text , key_text, dynamic_variable, "Encryption took place"]
    with open('log.csv', mode='r') as file:
        existing_data = list(csv.reader(file))

    # Write data back with new row at the top
    with open('log.csv', mode='w', newline='') as file:
        
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerow(new_data)  # Write the new row
        writer.writerows(existing_data)  # Write the rest of the data
    
    # Display the created variable in a label (or use it for other purposes)
    result_label.configure(text=f"Created Variable: {dynamic_variable}")
    encrypt_key_result_label.configure(text=f"Key Used: {key_text}")
    
def encrypt_text(input_text,key_text):
    f = Fernet(key_text)
    token = f.encrypt(input_text.encode())
    return token


# Generate Button
generate_button1 = ctk.CTkButton(app, text="Encrypt", font=label_font, width=630,height=40,command=lambda: main_app_encrypt(encrypt_text))
generate_button1.pack(pady=10)

# Decrypt
def main_app_decrypt(decrypt_text):
    # Retrieve the input from the entry widget
    input_text = input_entry.get()
    key_text = key_entry.get()  # Get the key from the key entry

    # Check if the key is empty
    if not key_text:
        messagebox.showerror("Error", "Key is required for Decryption.")
        return

    try:
        # Attempt to decrypt the text
        decrypted_text = decrypt_text(input_text.encode(), key_text.encode())
        result_label.configure(text=f"Decrypted Text: {decrypted_text}")
        encrypt_key_result_label.configure(text=f"Key Used: {key_text}")
    except Exception as e:
        # Show an error message if decryption fails
        messagebox.showerror("Decryption Error", str(e))
        
    new_data = [input_text , key_text, decrypted_text, "Decryption took place"]
    header = ["Input Text", "Key", "Output", "Message"]
    with open('log.csv', mode='r') as file:
        existing_data = list(csv.reader(file))

    # Write data back with new row at the top
    with open('log.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerow(new_data)  # Write the new row
        writer.writerows(existing_data)  # Write the rest of the data
    
def decrypt_text(input_text,key_text):
    f = Fernet(key_text) 
    decrypted_text = f.decrypt(input_text).decode()
    print("Decrypted text:", decrypted_text)
    return decrypted_text


generate_button2 = ctk.CTkButton(app, text="Decrypt", font=label_font, width=630,height=40,command=lambda: main_app_decrypt(decrypt_text))
generate_button2.pack(pady=5)

# Output Text
output_label = ctk.CTkLabel(app, text="Output Text", font=label_font, width=630,height=40)
output_label.pack(pady=10)
# output_entry = ctk.CTkEntry(app, placeholder_text="Output Token", font=label_font, width=630,height=40)
# output_entry.pack(pady=10)
# Label to display the result

# key_result_label = ctk.CTkLabel(app, text="fernet_key_encrypt", font=label_font)
# key_result_label.pack(pady=10)

result_label = ctk.CTkLabel(app, text="", font=label_font)
result_label.pack(pady=5)
# Function to copy text to clipboard
def copyoutput_to_clipboard():
    # Get the text from the result label
    text_to_copy = result_label.cget("text")
    # Clear the clipboard and append the new text
    app.clipboard_clear()  # Clear the clipboard
    app.clipboard_append(text_to_copy)  # Append the text to the clipboard
    # Optionally, show a message to the user
    # messagebox.showinfo("Copied", "Text copied to clipboard!")

# Copy Button
copy_output = ctk.CTkButton(app, text="Copy", command=copyoutput_to_clipboard)
copy_output.pack(pady=5)


encrypt_key_result_label = ctk.CTkLabel(app, text="", font=label_font)
encrypt_key_result_label.pack(pady=5)
def copykey_to_clipboard():
    # Get the text from the result label
    text_to_copy = encrypt_key_result_label.cget("text")
    # Clear the clipboard and append the new text
    app.clipboard_clear()  # Clear the clipboard
    app.clipboard_append(text_to_copy)  # Append the text to the clipboard
    # Optionally, show a message to the user
    # messagebox.showinfo("Copied", "Text copied to clipboard!")

# Copy Button
copy_key = ctk.CTkButton(app, text="Copy", command=copykey_to_clipboard)
copy_key.pack(pady=5)


def view_log():
    logapp = ctk.CTk()
    logapp.title("Log File")
    logapp.geometry("1920x1080")

    # Path to the CSV file
    csv_file_path = "log.csv"  # Replace with your CSV file path
    try:
        create_zebra_table(logapp, csv_file_path)
    except FileNotFoundError:
        error_label = ctk.CTkLabel(logapp, text="Error: File not found.", fg_color="#000000", padx=10, pady=10)
        error_label.pack(padx=10, pady=10)
    except Exception as e:
        error_label = ctk.CTkLabel(logapp, text=f"Error: {e}", fg_color="#ffcccc", padx=10, pady=10)
        error_label.pack(padx=10, pady=10)

    logapp.mainloop()

def create_zebra_table(logapp, file_path):
    # Create a scrollable table frame
    table_frame = ctk.CTkScrollableFrame(logapp, width=580, height=350, corner_radius=0)
    table_frame.pack(padx=10, pady=10, fill="both", expand=True)

    # Read and display the CSV file content
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    for i, row in enumerate(rows):
        for j, value in enumerate(row):
            # Apply zebra striping
            bg_color = "#f0f0f0" if i % 2 == 0 else "#ffffff"
            label = ctk.CTkLabel(table_frame, text=value, fg_color=bg_color,text_color="black", padx=10, pady=5)
            label.grid(row=i, column=j, sticky="nsew")

    # Configure column weights for proper resizing
    for col in range(len(rows[0])):
        table_frame.grid_columnconfigure(col, weight=1)

# View Logs Button
view_logs_button = ctk.CTkButton(app, text="View Logs", font=label_font, width=630, height=40, command=view_log)
view_logs_button.pack(pady=20)

# Start the application
app.mainloop()
