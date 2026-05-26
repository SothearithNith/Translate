import pandas as pd
import tkinter as tk

# Load the data from CSV
df = pd.read_csv('Data/Koko.txt')

# Get the English and Khmer columns
english = df['English'].tolist()
khmer = df['Khmer'].tolist()

# Initialize user input
user_input = ""

# Define the GUI function
def translate_sentence():
    # Get the user's input from the entry widget and convert to lowercase
    user_input = entry.get().lower()

    # Check if the user's input is in the list of English sentences (also converted to lowercase)
    if user_input in [x.lower() for x in english]:
        # Get the index of the user's input in the list of English sentences
        index = [x.lower() for x in english].index(user_input)

        # Display the corresponding Khmer sentence in the label widget (also converted to lowercase)
        output_label.config(text=khmer[index].lower(), fg="green", font=("Khmer OS Siemreap", 12))
    else:
        # Display an error message in the label widget
        output_label.config(text="That sentence is not in the list. Please try again.", fg="red", font=("Arial", 12))

def reset_input():
    # Clear the text in the entry widget and the output label
    entry.delete(0, tk.END)
    output_label.config(text="", font=("Arial", 12))

# Create the main window
window = tk.Tk()
window.config(bg="Aqua")
window.title("English-Khmer Translator")
window.iconbitmap('img/DragonLogo.ico') # Set custom window icon

# Create the label and entry widgets
label = tk.Label(window, text="Please enter a sentence in English to translate into Khmer:", font=("Arial", 12))
label.config(bg="Aqua")
label.pack(pady=10)
entry = tk.Entry(window, justify=tk.CENTER, font=("Arial", 12), width=40)
entry.pack()

# Create the output label widget
output_label = tk.Label(window, text="", font=("Arial", 12))
output_label.config(bg= "Aqua")
output_label.pack(pady=10)

button_frame = tk.Frame(window)
button_frame.pack()
translate_button = tk.Button(button_frame, text="Translate", command=translate_sentence, fg="White", font=("Arial", 12), bg="green")
translate_button.pack(side=tk.LEFT, padx=5)
reset_button = tk.Button(button_frame, text="Reset", command=reset_input, font=("Arial", 12), bg="yellow")
reset_button.pack(side=tk.LEFT, padx=5)

# Add some spacing between the entry widget and buttons
spacing_label = tk.Label(window, text="", font=("Arial", 12))
spacing_label.pack(pady=10)

# Bind the Enter key to the translate_sentence function
entry.bind("<Return>", lambda event: translate_sentence())

# Run the main loop
window.mainloop()