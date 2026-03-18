# **ComCalc Pro – Financial Tracking System**

**Final Year Project Report**



 **1. Project Title**

ComCalc Pro – A Professional Financial Tracking System Using Python**



**2. Author

Luckytben25
Student – Higher Diploma in Software Engineering



3. Introduction

ComCalc Pro is a desktop-based financial tracking application developed in Python. The system is designed to assist organizations and employees in tracking daily collections, calculating bonuses, applying penalties, and generating monthly commission reports efficiently.

Manual tracking of commissions using spreadsheets can lead to errors, time consumption, and lack of real-time insights. ComCalc Pro addresses these challenges by automating calculations and reporting while providing a user-friendly interface.



 **4. Objectives**

 4.1 Main Objective

To develop a professional financial tracking system that automates commission calculations, generates reports, and provides actionable insights.

 4.2 Specific Objectives

* Record and track daily collection amounts.
* Calculate daily bonuses based on predefined thresholds.
* Apply penalties for underperformance.
* Generate a monthly dashboard summarizing financial data.
* Visualize collection data through charts.
* Export reports in Excel and PDF formats.
* Store all data securely in a SQLite database.



 **5. Features**

 **Daily Collection Input:** Allows employees to record daily collections in GBP.
 **Automatic Bonus Calculation:** Bonuses are calculated based on the daily collection amount.
 **Penalty System:** A penalty of £10 is applied if daily collection is below £1000.
 **Dashboard Statistics:** Displays total collection, total bonus, and total penalties.
 **Daily Collection Table:** Tracks all recorded collections throughout the month.
 **Collection Chart:** Line graph visualizing daily collection trends.
 **Database Storage:** Uses SQLite for secure and persistent data storage.
 **Excel Export:** Generate monthly commission reports in Excel.
 **PDF Report:** Create professional PDF commission reports.


 **6. Technology Stack**

| Technology    | Purpose             |
| ------------- | ------------------- |
| Python 3.x    | Core programming    |
| CustomTkinter | GUI development     |
| SQLite        | Database storage    |
| Matplotlib    | Chart visualization |
| Pandas        | Excel export        |
| OpenPyXL      | Excel handling      |
| ReportLab     | PDF generation      |



**7. System Design**
 7.1 Architecture

The system uses a **modular architecture**:

**UI Layer:** CustomTkinter for an interactive GUI
**Business Logic Layer:** Handles commission calculations and penalties
**Data Layer:** SQLite database for persistent storage

7.2 Database Design

Table: collections

| Field  | Type    | Description             |
| ------ | ------- | ----------------------- |
| id     | INTEGER | Primary Key             |
| amount | REAL    | Daily collection amount |

7.3 Workflow

1. Employee enters daily collection.
2. System calculates the daily bonus.
3. Penalty applied if collection < £1000.
4. Data stored in the database.
5. Dashboard updated in real-time.
6. Reports exported to Excel or PDF at month-end.



8. Implementation

Daily Bonus Calculation:

  ```text
  >2500 → £25
  >2000 → £20
  >1500 → £15
  >1250 → £10
  >1000 → £5
  ```
* Penalty Calculation: £10 if daily collection < £1000.
* Dashboard & Chart: Displays summary statistics and visual trends using Matplotlib.
* Report Generation: Exports Excel and PDF reports using Pandas, OpenPyXL, and ReportLab.
* Database Storage: All collections are stored in an SQLite database to ensure persistence.

9. Testing

9.1 Test Cases

| Test Case       | Input      | Expected Output            |
| --------------- | ---------- | -------------------------- |
| Valid Input     | 1500       | Bonus = £15                |
| Low Input       | 800        | Penalty = £10              |
| Multiple Inputs | 1000, 2000 | Correct totals and bonuses |
| Invalid Input   | Text       | Error message              |

9.2 Results

All test cases passed successfully. The system accurately calculated bonuses, applied penalties, stored data, and generated Excel/PDF reports without errors.

---

10. Conclusion

ComCalc Pro provides a complete financial tracking solution by automating bonus calculations, penalty enforcement, and report generation. The system improves accuracy, reduces manual work, and offers a professional interface with real-time insights.

It demonstrates strong understanding and application of:

* Python programming
* GUI development
* Database management
* Financial logic implementation

11. Recommendations

Future enhancements could include:

* Multi-user login system
* Cloud database integration
* Web-based version for remote access
* Advanced analytics dashboard
* Mobile application integration


Sample Output


Daily Collection: £1200
Daily Bonus: £5
Penalty: £0
Total Commission: £5

Monthly Total Collection: £5000
Monthly Bonus: £45
Monthly Penalties: £10
Total Commission: £35

