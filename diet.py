#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import StringVar, Entry, OptionMenu, Label, Button

# Dictionary mapping diseases to diet recommendations
disease_diets = {
    "Diabetes": "Low-carb diet, avoid sugary foods",
    "Hypertension": "Low-sodium diet, reduce salt intake",
    "Obesity": "Calorie-controlled diet, regular exercise",
    # Add more diseases and corresponding diets as needed
}

# Dictionary mapping diseases to descriptions
disease_descriptions = {
    "Diabetes": "Diabetes is a chronic condition that affects how your body regulates blood sugar levels.",
    "Hypertension": "Hypertension, or high blood pressure, is a common condition in which the force of blood against the artery walls is too high.",
    "Obesity": "Obesity is a medical condition characterized by excess body fat.",
    # Add more diseases and descriptions as needed
}

# Function to predict diet based on selected disease
def predict_diet():
    selected_disease = selected_disease_var.get()  # Get the selected disease from the dropdown menu
    search_text = search_var.get()  # Get the text from the search box
    if selected_disease == "Select Disease" and search_text in disease_diets:  # Check if the search box input matches a disease
        selected_disease = search_text

    if selected_disease in disease_diets:
        diet_recommendation = disease_diets[selected_disease]
        disease_description = disease_descriptions[selected_disease]
        diet_text.set(f"Recommended diet for {selected_disease}: {diet_recommendation}")
        description_text.set(f"Description of {selected_disease}: {disease_description}")
    else:
        diet_text.set("Diet recommendation not available for this disease.")
        description_text.set("Description not available for this disease.")

# Create the main window
root = tk.Tk()
root.title("Diet Prediction")

# Search box for diseases
search_label = Label(root, text="Search Disease:")
search_label.grid(row=0, column=0, padx=5, pady=5)

search_var = StringVar()
search_entry = Entry(root, textvariable=search_var)
search_entry.grid(row=0, column=1, padx=5, pady=5)

# Dropdown menu for selecting disease
selected_disease_var = StringVar(root)
selected_disease_var.set("Select Disease")  # Default value
disease_options = list(disease_diets.keys())
disease_menu = OptionMenu(root, selected_disease_var, *disease_options)
disease_menu.grid(row=1, column=1, padx=5, pady=5)

# Label for displaying diet recommendation
diet_text = StringVar()
diet_label = Label(root, textvariable=diet_text, wraplength=300, justify="center", font=("Arial", 12))
diet_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Label for displaying disease description
description_text = StringVar()
description_label = Label(root, textvariable=description_text, wraplength=300, justify="center", font=("Arial", 12))
description_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Button to predict diet
predict_button = Button(root, text="Predict Diet", command=predict_diet, bg="#4CAF50", fg="white", padx=10, pady=5)
predict_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Footer
footer_label = Label(root, text="Developed by Your Name", fg="gray")
footer_label.grid(row=5, column=0, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()


# In[ ]:




