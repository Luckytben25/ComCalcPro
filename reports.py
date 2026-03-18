from openpyxl import Workbook
from database import fetch_data
from datetime import datetime

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


# ✅ Excel Export (Improved)
def export_excel():
    data = fetch_data()

    if not data:
        print("No data to export")
        return

    wb = Workbook()
    ws = wb.active
    ws.title = "ComCalc Report"

    # Header
    ws.append(["ID", "Amount (£)", "Bonus (£)", "Penalty (£)"])

    # Data
    for row in data:
        ws.append(row)

    # Totals
    total = sum([row[1] for row in data])
    bonus = sum([row[2] for row in data])
    penalty = sum([row[3] for row in data])

    ws.append([])
    ws.append(["TOTAL", total, bonus, penalty])

    # Auto filename with date
    filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    wb.save(filename)

    print(f"Excel saved as {filename}")


# ✅ PDF Export (Professional Table)
def export_pdf():
    data = fetch_data()

    if not data:
        print("No data to export")
        return

    filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()
    content = []

    # Title
    content.append(Paragraph("ComCalc Pro Financial Report", styles["Title"]))
    content.append(Spacer(1, 20))

    # Table Data
    table_data = [["ID", "Amount (£)", "Bonus (£)", "Penalty (£)"]]

    for row in data:
        table_data.append([
            row[0],
            f"£{row[1]}",
            f"£{row[2]}",
            f"£{row[3]}"
        ])

    # Totals
    total = sum([row[1] for row in data])
    bonus = sum([row[2] for row in data])
    penalty = sum([row[3] for row in data])

    table_data.append(["TOTAL", f"£{total}", f"£{bonus}", f"£{penalty}"])

    # Create Table
    table = Table(table_data)

    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ]))

    content.append(table)

    doc.build(content)

    print(f"PDF saved as {filename}")