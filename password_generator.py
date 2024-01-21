#importing all the necessary packages

import tkinter as tk
import random
import string
from tkinter import messagebox
from tkinter import filedialog

#defining the password generator

def generate_password(length, count, custom_sets):
    uppercase_set = string.ascii_uppercase if custom_sets["uppercase"] else ""
    lowercase_set = string.ascii_lowercase if custom_sets["lowercase"] else ""
    digits_set = string.digits if custom_sets["digits"] else ""
    punctuation_set = string.punctuation if custom_sets["punctuation"] else ""

    char_set = uppercase_set + lowercase_set + digits_set + punctuation_set

    if not char_set:
        messagebox.showerror("Error", "Select at least one character set.")
        return []

    passwords = []
    for _ in range(count):
        password = ''.join(random.choice(char_set) for _ in range(length))
        passwords.append(password)
    return passwords

#defining the passphrase generator

def generate_passphrase(words_count):
    word_list = ["apple", "banana", "cherry", "dog", "elephant", "friday", "giraffe", "happiness", "icecream", "jazz"]
    passphrase = ' '.join(random.choice(word_list) for _ in range(words_count))
    return passphrase

#setting the password strength

def check_password_strength(password):
    if len(password) < 8:
        return "Weak"
    elif any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
        return "Strong"
    else:
        return "Medium"

#defining strength level
    
def update_strength_indicator(event=None):
    generated_password = result_text.get(1.0, tk.END).strip()
    strength = check_password_strength(generated_password)
    
    if strength == "Weak":
        strength_label.config(text="Strength: Weak", fg="red")
    elif strength == "Medium":
        strength_label.config(text="Strength: Medium", fg="orange")
    else:
        strength_label.config(text="Strength: Strong", fg="green")

#logic behind password generation along with error handling
        
def generate_passwords_clicked():
    try:
        length = int(length_entry.get())
        count = int(count_entry.get())
        if length <= 0 or count <= 0:
            messagebox.showerror("Error", "Length and count should be greater than 0")
        else:
            custom_sets = {
                "uppercase": bool(uppercase_var.get()),
                "lowercase": bool(lowercase_var.get()),
                "digits": bool(digits_var.get()),
                "punctuation": bool(punctuation_var.get())
            }

            # custom_sets dictionary
            for key in custom_sets.keys():
                if key not in custom_sets:
                    custom_sets[key] = False

            passwords = generate_password(length, count, custom_sets)
            result_text.delete(1.0, tk.END)  # Clear previous results
            for password in passwords:
                result_text.insert(tk.END, password + "\n")
            update_strength_indicator()
    except ValueError:
        messagebox.showerror("Error", "Please enter valid length and count")

#logic for passphrase along with error handling
        
def generate_passphrase_clicked():
    try:
        words_count = int(passphrase_entry.get())
        if words_count <= 0:
            messagebox.showerror("Error", "Words count should be greater than 0")
        else:
            passphrase = generate_passphrase(words_count)
            result_text.delete(1.0, tk.END)  # Clear previous results
            result_text.insert(tk.END, passphrase + "\n")
            strength_label.config(text="Strength: Strong", fg="green")  # Passphrases are considered strong
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid words count")

#creating txt file to save passwords
        
def save_passwords():
    passwords_to_save = result_text.get(1.0, tk.END).strip()
    
    if not passwords_to_save:
        messagebox.showinfo("Information", "No passwords to save.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

    if file_path:
        with open(file_path, 'w') as file:
            file.write(passwords_to_save)
        messagebox.showinfo("Save Successful", "Passwords saved successfully.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.configure(bg='paleturquoise')

# Left side window frame
left_frame = tk.Frame(root, bg='paleturquoise')
left_frame.pack(side=tk.LEFT, padx=20, pady=20)

welcome_label = tk.Label(left_frame, text="Welcome to Password Generator \n", font=("Arial", 16,"underline"), bg='paleturquoise')
welcome_label.pack(pady=10)

length_label = tk.Label(left_frame, text="Password Length:", font=("Arial", 12), bg='paleturquoise')
length_label.pack()
length_entry = tk.Entry(left_frame, font=("Arial", 12), bg='white')
length_entry.pack()

count_label = tk.Label(left_frame, text="\n \n Number of Passwords to Generate:", font=("Arial", 12), bg='paleturquoise')
count_label.pack()
count_entry = tk.Entry(left_frame, font=("Arial", 12), bg='white')
count_entry.pack()

generate_button = tk.Button(left_frame, text="Generate Passwords", font=("Arial", 12), command=generate_passwords_clicked, bg='#f0f0f0')
generate_button.pack(pady=40)

# Checkbox frame
checkbox_frame = tk.Frame(left_frame, bg='paleturquoise')
checkbox_frame.pack()

uppercase_var = tk.IntVar()
lowercase_var = tk.IntVar()
digits_var = tk.IntVar()
punctuation_var = tk.IntVar()

uppercase_check = tk.Checkbutton(checkbox_frame, text="Uppercase Letters", variable=uppercase_var, font=("Arial", 12), bg='paleturquoise')
uppercase_check.pack(anchor='w')

lowercase_check = tk.Checkbutton(checkbox_frame, text="Lowercase Letters", variable=lowercase_var, font=("Arial", 12), bg='paleturquoise')
lowercase_check.pack(anchor='w')

digits_check = tk.Checkbutton(checkbox_frame, text="Digits", variable=digits_var, font=("Arial", 12), bg='paleturquoise')
digits_check.pack(anchor='w')

punctuation_check = tk.Checkbutton(checkbox_frame, text="Special Characters", variable=punctuation_var, font=("Arial", 12), bg='paleturquoise')
punctuation_check.pack(anchor='w')

# Right side window frame
right_frame = tk.Frame(root, bg='paleturquoise')
right_frame.pack(side=tk.RIGHT, padx=20, pady=20)

passphrase_label = tk.Label(right_frame, text="Passphrase Words Count:", font=("Arial", 12), bg='paleturquoise')
passphrase_label.pack()
passphrase_entry = tk.Entry(right_frame, font=("Arial", 12), bg='white')
passphrase_entry.pack()

generate_passphrase_button = tk.Button(right_frame, text="Generate Passphrase", font=("Arial", 12), command=generate_passphrase_clicked, bg='#f0f0f0')
generate_passphrase_button.pack(pady=10)

result_label = tk.Label(right_frame, text="\n\nGenerated Passwords:", font=("Arial", 12), bg='paleturquoise')
result_label.pack()

result_text = tk.Text(right_frame, height=10, width=50, font=("Arial", 12), bg='white')
result_text.pack()

strength_label = tk.Label(right_frame, text="Strength:", font=("Arial", 12), bg='paleturquoise')
strength_label.pack(pady=10)

result_text.bind("<KeyRelease>", update_strength_indicator)

# Save Passwords button
save_button = tk.Button(right_frame, text="Save Passwords", font=("Arial", 12), command=save_passwords, bg='#f0f0f0')
save_button.pack(pady=10)

# Run the application
root.mainloop()
