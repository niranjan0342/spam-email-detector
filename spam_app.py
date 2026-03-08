import tkinter as tk
import joblib

# Load trained model and vectorizer
model = joblib.load("spam_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Function to check spam
def check_spam():
    message = entry.get()
    
    if message == "":
        result_label.config(text="Please enter a message")
        return
    
    vector = vectorizer.transform([message])
    prediction = model.predict(vector)
    
    if prediction[0] == 1:
        result_label.config(text="Spam Message", fg="red")
    else:
        result_label.config(text="Not Spam Message", fg="green")

# Create window
root = tk.Tk()
root.title("Spam Message Detector")
root.geometry("400x250")

# Title
title = tk.Label(root, text="Spam Detection App", font=("Arial", 16))
title.pack(pady=10)

# Input label
label = tk.Label(root, text="Enter Message:")
label.pack()

# Text input
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Check button
check_button = tk.Button(root, text="Check Message", command=check_spam)
check_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run app
root.mainloop()