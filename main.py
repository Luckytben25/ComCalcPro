import customtkinter as ctk
from calculations import calculate_bonus, calculate_penalty
from database import insert_data, fetch_data
import matplotlib.pyplot as plt
from reports import export_excel, export_pdf

ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("ComCalc Pro")
app.geometry("500x550")  # slightly bigger

# ---------------- INPUT ----------------
entry = ctk.CTkEntry(app, placeholder_text="Enter Collection Amount")
entry.pack(pady=20)

result_label = ctk.CTkLabel(app, text="")
result_label.pack(pady=10)


# ---------------- FUNCTIONS ----------------
def add_data():
    try:
        amount = float(entry.get())

        bonus = calculate_bonus(amount)
        penalty = calculate_penalty(amount)

        insert_data(amount, bonus, penalty)

        result_label.configure(
            text=f"Bonus: £{bonus} | Penalty: £{penalty}"
        )

        entry.delete(0, "end")  # ✅ clear input after adding

        update_dashboard()

    except ValueError:  # ✅ better error handling
        result_label.configure(text="Invalid Input")


def update_dashboard():
    data = fetch_data()

    if not data:
        dashboard_label.configure(text="No Data Yet")
        return

    total = sum([row[1] for row in data])
    bonus = sum([row[2] for row in data])
    penalty = sum([row[3] for row in data])

    dashboard_label.configure(
        text=f"Total: £{total}\nBonus: £{bonus}\nPenalty: £{penalty}"
    )


def show_chart():
    data = fetch_data()

    if not data:
        result_label.configure(text="No data to display")
        return

    amounts = [row[1] for row in data]

    plt.figure()
    plt.plot(amounts)
    plt.title("Daily Collections")
    plt.xlabel("Entries")
    plt.ylabel("Amount (£)")
    plt.grid()
    plt.show()


# ---------------- BUTTONS ----------------
btn = ctk.CTkButton(app, text="Add Collection", command=add_data)
btn.pack(pady=10)

chart_btn = ctk.CTkButton(app, text="Show Chart", command=show_chart)
chart_btn.pack(pady=10)

excel_btn = ctk.CTkButton(app, text="Export Excel", command=export_excel)
excel_btn.pack(pady=10)

pdf_btn = ctk.CTkButton(app, text="Export PDF", command=export_pdf)
pdf_btn.pack(pady=10)

# ---------------- DASHBOARD ----------------
dashboard_label = ctk.CTkLabel(app, text="")
dashboard_label.pack(pady=20)

update_dashboard()

app.mainloop()