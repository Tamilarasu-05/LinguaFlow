import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

def translate_text():
    try:
        input_text = input_text_box.get("1.0", tk.END).strip()
        src_lang = source_language_combo.get()
        dest_lang = target_language_combo.get()

        if not input_text:
            messagebox.showwarning("Input Error", "Please enter text to translate.")
            return

        translator = Translator()
        translated = translator.translate(input_text, src=src_lang, dest=dest_lang)

        output_text_box.delete("1.0", tk.END)
        output_text_box.insert(tk.END, translated.text)

    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred: {e}")

# Create main window
root = tk.Tk()
root.title("Language Translator")
root.geometry("600x600")
root.resizable(False, False)

# Title label
tk.Label(root, text="Language Translator", font=("Arial", 20, "bold")).pack(pady=10)

# Input text frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

tk.Label(input_frame, text="Input Text:", font=("Arial", 12)).pack(anchor="w")
input_text_box = tk.Text(input_frame, height=8, width=60)
input_text_box.pack()

# Language selection frame
language_frame = tk.Frame(root)
language_frame.pack(pady=10)

# Source language
source_language_label = tk.Label(language_frame, text="Source Language:", font=("Arial", 12))
source_language_label.grid(row=0, column=0, padx=10, pady=5)

source_language_combo = ttk.Combobox(language_frame, width=30, state="readonly")
source_language_combo['values'] = list(LANGUAGES.values())
source_language_combo.set("english")  # Default value
source_language_combo.grid(row=0, column=1, padx=10, pady=5)

# Target language
target_language_label = tk.Label(language_frame, text="Target Language:", font=("Arial", 12))
target_language_label.grid(row=1, column=0, padx=10, pady=5)

target_language_combo = ttk.Combobox(language_frame, width=30, state="readonly")
target_language_combo['values'] = list(LANGUAGES.values())
target_language_combo.set("hindi")  # Default value
target_language_combo.grid(row=1, column=1, padx=10, pady=5)

# Translate button
translate_button = tk.Button(root, text="Translate", font=("Arial", 12, "bold"), bg="blue", fg="white", command=translate_text)
translate_button.pack(pady=10)

# Output text frame
output_frame = tk.Frame(root)
output_frame.pack(pady=10)

tk.Label(output_frame, text="Translated Text:", font=("Arial", 12)).pack(anchor="w")
output_text_box = tk.Text(output_frame, height=8, width=60)
output_text_box.pack()

# Run the application
root.mainloop()
