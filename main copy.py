import customtkinter as ctk

# Appearance
ctk.set_appearance_mode("dark")

# Create main window
app = ctk.CTk()
app.title("ComCalc Pro")
app.geometry("500x400")

# Title
title = ctk.CTkLabel(
    app,
    text="ComCalc Financial Tracker",
    font=("Arial", 24)
)
title.pack(pady=20)

# ------------------------------
# ADD YOUR CODE HERE

def add_collection():

    amount = float(entry.get())

    collections.append(amount)

    result_label.configure(
        text=f"Collection Added: £{amount}"
    )



# ------------------------------

collections = []

entry = ctk.CTkEntry(
    app,
    placeholder_text="Enter Daily Collection (GBP) "
)

entry.pack(pady=10)

add_button = ctk.CTkButton(
    app,
    text="Add Collection",
    command=add_collection
)

add_button.pack(pady=10)

result_label = ctk.CTkLabel(app,text="")
result_label.pack()

# ------------------------------

def calculate_bonus(amount):

    if amount > 2500:
        return 25
    elif amount > 2000:
        return 20
    elif amount > 1500:
        return 15
    elif amount > 1250:
        return 10
    elif amount > 1000:
        return 5
    else:
        return 0

bonus = calculate_bonus(amount)

penalties = 0

if amount < 1000:
    penalties += 10

def calculate_month():

    total_collection = sum(collections)

    total_bonus = sum(calculate_bonus(x) for x in collections)

    commission = total_bonus - penalties

    result_label.configure(
        text=f"""
Total Collection: £{total_collection}
Total Bonus: £{total_bonus}
Penalties: £{penalties}
Commission: £{commission}
"""
    )

    month_button = ctk.CTkButton(
    app,
    text="Calculate Monthly Commission",
    command=calculate_month
)

month_button.pack(pady=10)

# Start application
app.mainloop()