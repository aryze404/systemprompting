import tkinter as tk

def submit_evaluation():
    evaluation = entry_evaluation.get()
    if evaluation.lower() == "okay":
        update_rating(1)
    elif evaluation.lower() == "no":
        update_rating(-1)

def update_rating(rating):
    global total_ratings, okay, no
    if rating == 1:
        okay += 1
    elif rating == -1:
        no += 1

    total_ratings += 1
    update_display()

def update_display():
    okay_percentage = (okay / total_ratings) * 100
    no_percentage = (no / total_ratings) * 100

    label_okay.config(text=f"Okay: {okay}")
    label_no.config(text=f"No: {no}")
    label_rated.config(text=f"Rated: {total_ratings}")
    label_okay_rate.config(text=f"Okay Rate: {okay_percentage:.2f}%")
    label_no_rate.config(text=f"No Rate: {no_percentage:.2f}%")

def close_app():
    root.destroy()

# Initialize variables
total_ratings = 0
okay = 0
no = 0
total_data = 3

# Create the main window
root = tk.Tk()
root.title("AI Manual Evaluation System")

# Create Table for Input, Expected Response, Output, Okay, No
label_titles = tk.Label(root, text="Input", borderwidth=1, relief="solid")
label_titles.grid(row=3, column=0)
label_titles = tk.Label(root, text="Expected Response", borderwidth=1, relief="solid")
label_titles.grid(row=3, column=1)
label_titles = tk.Label(root, text="Output", borderwidth=1, relief="solid")
label_titles.grid(row=3, column=2)
label_titles = tk.Label(root, text="Okay/No", borderwidth=1, relief="solid")
label_titles.grid(row=3, column=3)

entry_input = tk.Entry(root, borderwidth=1, relief="solid")
entry_input.grid(row=4, column=0, padx=5, pady=5)
entry_input2 = tk.Entry(root, borderwidth=1, relief="solid")
entry_input2.grid(row=5, column=0, padx=5, pady=5)
entry_input3 = tk.Entry(root, borderwidth=1, relief="solid")
entry_input3.grid(row=6, column=0, padx=5, pady=5)

entry_expected_response = tk.Entry(root, borderwidth=1, relief="solid")
entry_expected_response.grid(row=4, column=1)
entry_expected_response2 = tk.Entry(root, borderwidth=1, relief="solid")
entry_expected_response2.grid(row=5, column=1)
entry_expected_response3 = tk.Entry(root, borderwidth=1, relief="solid")
entry_expected_response3.grid(row=6, column=1)

entry_output = tk.Entry(root, borderwidth=1, relief="solid")
entry_output.grid(row=4, column=2)
entry_output2 = tk.Entry(root, borderwidth=1, relief="solid")
entry_output2.grid(row=5, column=2)
entry_output3 = tk.Entry(root, borderwidth=1, relief="solid")
entry_output3.grid(row=6, column=2)

button_okay = tk.Button(root, text="Okay", command=lambda: update_rating(1))
button_okay.grid(row=4, column=3, padx=5, pady=5)
button_no = tk.Button(root, text="No", command=lambda: update_rating(-1))
button_no.grid(row=4, column=4, padx=5, pady=5)

button_okay = tk.Button(root, text="Okay", command=lambda: update_rating(1))
button_okay.grid(row=5, column=3)
button_no = tk.Button(root, text="No", command=lambda: update_rating(-1))
button_no.grid(row=5, column=4)

button_okay = tk.Button(root, text="Okay", command=lambda: update_rating(1))
button_okay.grid(row=6, column=3)
button_no = tk.Button(root, text="No", command=lambda: update_rating(-1))
button_no.grid(row=6, column=4)

# Create Table for Rated Percentage, Okay, No
label_titles = tk.Label(root, text="Rated %", borderwidth=1, relief="solid")
label_titles.grid(row=0, column=0, padx=5, pady=5)
label_titles = tk.Label(root, text="Okay", borderwidth=1, relief="solid")
label_titles.grid(row=0, column=1, padx=5, pady=5)
label_titles = tk.Label(root, text="No", borderwidth=1, relief="solid")
label_titles.grid(row=0, column=2, padx=5, pady=5)

label_rated = tk.Label(root, text="Rated: 0", borderwidth=1, relief="solid")
label_rated.grid(row=1, column=0, padx=5, pady=5)
label_okay = tk.Label(root, text="Okay: 0", borderwidth=1, relief="solid")
label_okay.grid(row=1, column=1, padx=5, pady=5)
label_no = tk.Label(root, text="No: 0", borderwidth=1, relief="solid")
label_no.grid(row=1, column=2, padx=5, pady=5)

label_okay_rate = tk.Label(root, text="Okay Rate: 0.00%", borderwidth=1, relief="solid")
label_okay_rate.grid(row=2, column=1, padx=5, pady=5)
label_no_rate = tk.Label(root, text="No Rate: 0.00%", borderwidth=1, relief="solid")
label_no_rate.grid(row=2, column=2, padx=5, pady=5)

label_rated = tk.Label(root, text="Rated: 0/{total_data}", borderwidth=1, relief="solid")
label_rated.grid(row=1, column=0, padx=5, pady=5)

button_save = tk.Button(root, text="Save", command=close_app)
button_save.grid(row=7, column=0, padx=5, pady=5)

root.mainloop()