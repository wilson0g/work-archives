from tkinter import *
from tkinter import ttk

from progenFCdatabase import database_connection


def transaction():
    def search_transaction():
        search_value = search_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT transaction.transactionID, transaction.athleteID, athlete.athleteFName, athlete.athleteLName, "
            "transaction.transactionDate, transaction.transactionAmount, transaction.transactionReference, "
            "transaction.transactionMedium, transaction.transactionStatus "
            "FROM transaction JOIN athlete ON transaction.athleteID = athlete.athleteID "
            "WHERE transaction.transactionID LIKE %s OR transaction.athleteID LIKE %s "
            "OR athlete.athleteFName LIKE %s OR athlete.athleteLName LIKE %s "
            "OR transaction.transactionDate LIKE %s OR transaction.transactionReference LIKE %s "
            "OR transaction.transactionMedium LIKE %s OR transaction.transactionStatus LIKE %s",
            (
                "%" + search_value + "%",
                "%" + search_value + "%",
                "%" + search_value + "%",
                "%" + search_value + "%",
                "%" + search_value + "%",
                "%" + search_value + "%",
                "%" + search_value + "%",
                "%" + search_value + "%",
            ),
        )

        records = cursor.fetchall()

        for row in transaction_table.get_children():
            transaction_table.delete(row)

        for record in records:
            transaction_table.insert("", END, values=record)

        connection.close()

    def load_transactions():
        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT transaction.transactionID, transaction.athleteID, athlete.athleteFName, athlete.athleteLName, "
            "transaction.transactionDate, transaction.transactionAmount, transaction.transactionReference, "
            "transaction.transactionMedium, transaction.transactionStatus "
            "FROM transaction JOIN athlete ON transaction.athleteID = athlete.athleteID"
        )

        records = cursor.fetchall()

        for row in transaction_table.get_children():
            transaction_table.delete(row)

        for record in records:
            transaction_table.insert("", END, values=record)

        connection.close()

    def add_transaction():
        transaction_id = transaction_id_entry.get()
        athlete_id = athlete_id_entry.get().split(" - ")[0]
        transaction_date = transaction_date_entry.get()
        transaction_amount = transaction_amount_entry.get()
        transaction_reference = transaction_reference_entry.get()
        transaction_medium = transaction_medium_entry.get()
        transaction_status = transaction_status_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO transaction "
            "(transactionID, athleteID, transactionDate, transactionAmount, transactionReference, transactionMedium, transactionStatus) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (
                transaction_id,
                athlete_id,
                transaction_date,
                transaction_amount,
                transaction_reference,
                transaction_medium,
                transaction_status,
            ),
        )

        connection.commit()

        cursor.execute(
            "SELECT athleteFName, athleteLName FROM athlete WHERE athleteID = %s",
            (athlete_id,),
        )

        athlete_record = cursor.fetchone()

        connection.close()

        transaction_table.insert(
            "",
            END,
            values=(
                transaction_id,
                athlete_id,
                athlete_record[0],
                athlete_record[1],
                transaction_date,
                transaction_amount,
                transaction_reference,
                transaction_medium,
                transaction_status,
            ),
        )

    def clear_transaction():
        transaction_id_entry.delete(0, END)
        athlete_id_entry.delete(0, END)
        transaction_date_entry.delete(0, END)
        transaction_amount_entry.delete(0, END)
        transaction_reference_entry.delete(0, END)
        transaction_medium_entry.delete(0, END)
        transaction_status_entry.delete(0, END)

    def delete_transaction():
        transaction_id = transaction_id_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM transaction WHERE transactionID = %s",
            (transaction_id,),
        )

        connection.commit()
        connection.close()

        for row in transaction_table.get_children():
            values = transaction_table.item(row)["values"]

            if str(values[0]) == transaction_id:
                transaction_table.delete(row)
                break

    def update_transaction():
        transaction_id = transaction_id_entry.get()
        athlete_id = athlete_id_entry.get().split(" - ")[0]
        transaction_date = transaction_date_entry.get()
        transaction_amount = transaction_amount_entry.get()
        transaction_reference = transaction_reference_entry.get()
        transaction_medium = transaction_medium_entry.get()
        transaction_status = transaction_status_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE transaction SET athleteID = %s, transactionDate = %s, transactionAmount = %s, "
            "transactionReference = %s, transactionMedium = %s, transactionStatus = %s "
            "WHERE transactionID = %s",
            (
                athlete_id,
                transaction_date,
                transaction_amount,
                transaction_reference,
                transaction_medium,
                transaction_status,
                transaction_id,
            ),
        )

        connection.commit()

        cursor.execute(
            "SELECT athleteFName, athleteLName FROM athlete WHERE athleteID = %s",
            (athlete_id,),
        )

        athlete_record = cursor.fetchone()

        connection.close()

        for row in transaction_table.get_children():
            values = transaction_table.item(row)["values"]

            if str(values[0]) == transaction_id:
                transaction_table.item(
                    row,
                    values=(
                        transaction_id,
                        athlete_id,
                        athlete_record[0],
                        athlete_record[1],
                        transaction_date,
                        transaction_amount,
                        transaction_reference,
                        transaction_medium,
                        transaction_status,
                    ),
                )
                break

    def go_to_dashboard():
        from ProgenFC_modules.ProgenFCdashboard import dashboard

        window.destroy()
        dashboard()

    window = Tk()
    window.geometry("1536x1024")
    window.title("Payments / Transactions Management")
    window.config(background="#0B1F33")

    heading = Label(
        window,
        text="Payments / Transactions Management",
        font=("Arial", 28, "bold"),
        bg="#0B1F33",
        fg="#4CCB3A",
    )

    heading.place(x=500, y=20)

    transaction_id_label = Label(
        window,
        text="Transaction ID:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    transaction_id_label.place(x=170, y=80)

    transaction_id_entry = Entry(window, font=("Arial", 14))

    transaction_id_entry.place(x=370, y=75, width=300, height=35)

    athlete_id_label = Label(
        window,
        text="Athlete:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    athlete_id_label.place(x=170, y=140)

    connection = database_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT athleteID, athleteFName, athleteLName FROM athlete")

    athletes = cursor.fetchall()

    connection.close()

    athlete_options = []

    for athlete_record in athletes:
        athlete_options.append(
            athlete_record[0] + " - " + athlete_record[1] + " " + athlete_record[2]
        )

    athlete_id_entry = ttk.Combobox(
        window,
        font=("Arial", 14),
        values=athlete_options,
    )

    athlete_id_entry.place(x=370, y=135, width=300, height=35)

    transaction_date_label = Label(
        window,
        text="Transaction Date:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    transaction_date_label.place(x=170, y=200)

    transaction_date_entry = Entry(window, font=("Arial", 14))

    transaction_date_entry.place(x=370, y=195, width=300, height=35)

    transaction_amount_label = Label(
        window,
        text="Transaction Amount:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    transaction_amount_label.place(x=170, y=260)

    transaction_amount_entry = Entry(window, font=("Arial", 14))

    transaction_amount_entry.place(x=370, y=255, width=300, height=35)

    transaction_reference_label = Label(
        window,
        text="Transaction Reference:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    transaction_reference_label.place(x=170, y=320)

    transaction_reference_entry = Entry(window, font=("Arial", 14))

    transaction_reference_entry.place(x=370, y=315, width=300, height=35)

    transaction_medium_label = Label(
        window,
        text="Transaction Medium:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    transaction_medium_label.place(x=170, y=380)

    transaction_medium_entry = ttk.Combobox(
        window,
        font=("Arial", 14),
        values=("Bank Transfer",),
        state="readonly",
    )

    transaction_medium_entry.set("Bank Transfer")

    transaction_medium_entry.place(x=370, y=375, width=300, height=35)

    transaction_status_label = Label(
        window,
        text="Transaction Status:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    transaction_status_label.place(x=170, y=440)

    transaction_status_entry = ttk.Combobox(
        window,
        font=("Arial", 14),
        values=(
            "Completed",
            "Pending",
            "Failed",
        ),
    )

    transaction_status_entry.place(x=370, y=435, width=300, height=35)

    search_entry = Entry(window, font=("Arial", 13))

    search_entry.place(x=200, y=593, width=940, height=35)

    search_button = Button(
        window,
        text="🔍    Search",
        font=("Arial", 13, "bold"),
        command=search_transaction,
    )

    search_button.place(x=1160, y=593, width=120, height=35)

    add_button = Button(
        window,
        text=" ➕ Add",
        font=("Arial", 13, "bold"),
        command=add_transaction,
    )

    add_button.place(x=170, y=505, width=120, height=40)

    update_button = Button(
        window,
        text="✏️ Update",
        font=("Arial", 13, "bold"),
        command=update_transaction,
    )

    update_button.place(x=310, y=505, width=120, height=40)

    delete_button = Button(
        window,
        text=" 🗑️ Delete",
        font=("Arial", 13, "bold"),
        command=delete_transaction,
    )

    delete_button.place(x=450, y=505, width=120, height=40)

    clear_button = Button(
        window,
        text=" ♻️ Clear",
        font=("Arial", 13, "bold"),
        command=clear_transaction,
    )

    clear_button.place(x=590, y=505, width=120, height=40)

    transaction_table = ttk.Treeview(
        window,
        columns=(
            "transactionID",
            "athleteID",
            "athleteFName",
            "athleteLName",
            "transactionDate",
            "transactionAmount",
            "transactionReference",
            "transactionMedium",
            "transactionStatus",
        ),
        show="headings",
    )

    transaction_table.heading("transactionID", text="Transaction ID")
    transaction_table.heading("athleteID", text="Athlete ID")
    transaction_table.heading("athleteFName", text="First Name")
    transaction_table.heading("athleteLName", text="Last Name")
    transaction_table.heading("transactionDate", text="Transaction Date")
    transaction_table.heading("transactionAmount", text="Amount")
    transaction_table.heading("transactionReference", text="Reference")
    transaction_table.heading("transactionMedium", text="Medium")
    transaction_table.heading("transactionStatus", text="Status")

    transaction_table.column("transactionID", width=120)
    transaction_table.column("athleteID", width=100)
    transaction_table.column("athleteFName", width=130)
    transaction_table.column("athleteLName", width=130)
    transaction_table.column("transactionDate", width=130)
    transaction_table.column("transactionAmount", width=120)
    transaction_table.column("transactionReference", width=180)
    transaction_table.column("transactionMedium", width=150)
    transaction_table.column("transactionStatus", width=120)

    transaction_table.place(x=80, y=640, width=1350, height=300)

    dashboard_button = Button(
        window,
        text="← Dashboard",
        font=("Arial", 13, "bold"),
        command=go_to_dashboard,
    )

    dashboard_button.place(x=30, y=25, width=130, height=40)

    progen_logo = PhotoImage(file="ProgenFC_small_150.png")

    progen_logo_label = Label(
        window,
        image=progen_logo,
        bg="#0B1F33",
    )

    progen_logo_label.place(x=1400, y=95, anchor="center")

    load_transactions()

    window.mainloop()


if __name__ == "__main__":
    transaction()
