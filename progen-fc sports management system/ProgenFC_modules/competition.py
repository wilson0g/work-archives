from tkinter import *
from tkinter import ttk

from progenFCdatabase import database_connection


def competition():
    def search_competition():
        search_value = search_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT competitionID, competitionName, compStartDate, compEndDate, compLocation, compFee FROM competition WHERE competitionID LIKE %s OR competitionName LIKE %s OR compStartDate LIKE %s OR compEndDate LIKE %s OR compLocation LIKE %s OR compFee LIKE %s",
            (
                "%" + search_value + "%",
                "%" + search_value + "%",
                "%" + search_value + "%",
                "%" + search_value + "%",
                "%" + search_value + "%",
                "%" + search_value + "%",
            ),
        )

        records = cursor.fetchall()

        for row in competition_table.get_children():
            competition_table.delete(row)

        for record in records:
            competition_table.insert("", END, values=record)

        connection.close()

    def load_competitions():
        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT competitionID, competitionName, compStartDate, compEndDate, compLocation, compFee FROM competition"
        )

        records = cursor.fetchall()

        for row in competition_table.get_children():
            competition_table.delete(row)

        for record in records:
            competition_table.insert("", END, values=record)

        connection.close()

    def add_competition():
        competition_id = competition_id_entry.get()
        competition_name = competition_name_entry.get()
        start_date = start_date_entry.get()
        end_date = end_date_entry.get()
        competition_location = competition_location_entry.get()
        competition_fee = competition_fee_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO competition (competitionID, competitionName, compStartDate, compEndDate, compLocation, compFee) VALUES (%s, %s, %s, %s, %s, %s)",
            (
                competition_id,
                competition_name,
                start_date,
                end_date,
                competition_location,
                competition_fee,
            ),
        )

        connection.commit()
        connection.close()

        competition_table.insert(
            "",
            END,
            values=(
                competition_id,
                competition_name,
                start_date,
                end_date,
                competition_location,
                competition_fee,
            ),
        )

    def clear_competition():
        competition_id_entry.delete(0, END)
        competition_name_entry.delete(0, END)
        start_date_entry.delete(0, END)
        end_date_entry.delete(0, END)
        competition_location_entry.delete(0, END)
        competition_fee_entry.delete(0, END)

    def delete_competition():
        competition_id = competition_id_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM competition WHERE competitionID = %s",
            (competition_id,),
        )
        connection.commit()
        connection.close()

        for row in competition_table.get_children():
            values = competition_table.item(row)["values"]

            if str(values[0]) == competition_id:
                competition_table.delete(row)
                break

    def update_competition():
        competition_id = competition_id_entry.get()
        competition_name = competition_name_entry.get()
        start_date = start_date_entry.get()
        end_date = end_date_entry.get()
        competition_location = competition_location_entry.get()
        competition_fee = competition_fee_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE competition SET competitionName = %s, compStartDate = %s, compEndDate = %s, compLocation = %s, compFee = %s WHERE competitionID = %s",
            (
                competition_name,
                start_date,
                end_date,
                competition_location,
                competition_fee,
                competition_id,
            ),
        )

        connection.commit()
        connection.close()

        for row in competition_table.get_children():
            values = competition_table.item(row)["values"]

            if str(values[0]) == competition_id:
                competition_table.item(
                    row,
                    values=(
                        competition_id,
                        competition_name,
                        start_date,
                        end_date,
                        competition_location,
                        competition_fee,
                    ),
                )
                break

    def go_to_dashboard():
        from ProgenFC_modules.ProgenFCdashboard import dashboard

        window.destroy()
        dashboard()

    window = Tk()
    window.geometry("1536x1024")
    window.title("Competition Management")
    window.config(background="#0B1F33")

    heading = Label(
        window,
        text="Competition Management",
        font=("Arial", 28, "bold"),
        bg="#0B1F33",
        fg="#4CCB3A",
    )

    heading.place(x=600, y=20)

    competition_id_label = Label(
        window,
        text="Competition ID:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    competition_id_label.place(x=170, y=80)

    competition_id_entry = Entry(window, font=("Arial", 14))

    competition_id_entry.place(x=370, y=75, width=300, height=35)

    competition_name_label = Label(
        window,
        text="Competition Name:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    competition_name_label.place(x=170, y=140)

    competition_name_entry = Entry(window, font=("Arial", 14))

    competition_name_entry.place(x=370, y=135, width=300, height=35)

    start_date_label = Label(
        window,
        text="Start Date:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    start_date_label.place(x=170, y=200)

    start_date_entry = Entry(window, font=("Arial", 14))

    start_date_entry.place(x=370, y=195, width=300, height=35)

    end_date_label = Label(
        window,
        text="End Date:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    end_date_label.place(x=170, y=260)

    end_date_entry = Entry(window, font=("Arial", 14))

    end_date_entry.place(x=370, y=255, width=300, height=35)

    competition_location_label = Label(
        window,
        text="Location:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    competition_location_label.place(x=170, y=320)

    competition_location_entry = Entry(window, font=("Arial", 14))

    competition_location_entry.place(x=370, y=315, width=300, height=35)

    competition_fee_label = Label(
        window,
        text="Competition Fee:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    competition_fee_label.place(x=170, y=380)

    competition_fee_entry = Entry(window, font=("Arial", 14))

    competition_fee_entry.place(x=370, y=375, width=300, height=35)

    search_entry = Entry(window, font=("Arial", 13))

    search_entry.place(x=200, y=593, width=940, height=35)

    search_button = Button(
        window,
        text="🔍    Search",
        font=("Arial", 13, "bold"),
        command=search_competition,
    )

    search_button.place(x=1160, y=593, width=120, height=35)

    add_button = Button(
        window,
        text=" ➕ Add",
        font=("Arial", 13, "bold"),
        command=add_competition,
    )

    add_button.place(x=170, y=505, width=120, height=40)

    update_button = Button(
        window,
        text="✏️ Update",
        font=("Arial", 13, "bold"),
        command=update_competition,
    )

    update_button.place(x=310, y=505, width=120, height=40)

    delete_button = Button(
        window,
        text=" 🗑️ Delete",
        font=("Arial", 13, "bold"),
        command=delete_competition,
    )

    delete_button.place(x=450, y=505, width=120, height=40)

    clear_button = Button(
        window,
        text=" ♻️ Clear",
        font=("Arial", 13, "bold"),
        command=clear_competition,
    )

    clear_button.place(x=590, y=505, width=120, height=40)

    competition_table = ttk.Treeview(
        window,
        columns=(
            "competitionID",
            "competitionName",
            "compStartDate",
            "compEndDate",
            "compLocation",
            "compFee",
        ),
        show="headings",
    )

    competition_table.heading("competitionID", text="Competition ID")
    competition_table.heading("competitionName", text="Competition Name")
    competition_table.heading("compStartDate", text="Start Date")
    competition_table.heading("compEndDate", text="End Date")
    competition_table.heading("compLocation", text="Location")
    competition_table.heading("compFee", text="Competition Fee")

    competition_table.column("competitionID", width=130)
    competition_table.column("competitionName", width=220)
    competition_table.column("compStartDate", width=130)
    competition_table.column("compEndDate", width=130)
    competition_table.column("compLocation", width=200)
    competition_table.column("compFee", width=130)

    competition_table.place(x=80, y=640, width=1350, height=300)

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

    load_competitions()

    window.mainloop()


if __name__ == "__main__":
    competition()
