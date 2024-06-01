import tkinter as tk
from tkinter import filedialog
import pyttsx3

# Function to generate voice from text and save it to a file
def generate_and_save_voice():
    text = text_entry.get()
    if text.strip() == "":
        status_label.config(text="Please enter some text.", fg="red")
        return
    
    # Open file dialog to save the audio file
    file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if not file_path:
        status_label.config(text="Save cancelled.", fg="red")
        return
    
    status_label.config(text="Generating voice...", fg="black")
    app.update()
    
    # Initialize the pyttsx3 engine
    engine = pyttsx3.init()
    
    # Set properties for the voice
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'male' in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break
    
    # Save the voice to the specified file
    engine.save_to_file(text, file_path)
    engine.runAndWait()
    
    status_label.config(text=f"Voice saved to {file_path}", fg="green")

# Create the main application window
app = tk.Tk()
app.title("AI Voice Assistant")

# Set the window icon
photo = tk.PhotoImage(file='icon.png')
app.wm_iconphoto(False, photo)

# Create and place the text entry box
tk.Label(app, text="Enter text:").pack()
text_entry = tk.Entry(app, width=50)
text_entry.pack()

# Create and place the generate and save button
generate_button = tk.Button(app, text="Generate and Save Voice", command=generate_and_save_voice)
generate_button.pack()

# Create and place the status label
status_label = tk.Label(app, text="")
status_label.pack()

# Run the Tkinter event loop
app.mainloop()
