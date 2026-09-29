from tkinter import *
from tkinter import ttk

from progenFCdatabase import database_connection


def membership():
    def search_membership():
        search_value = search_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            " SELECT membership.membershipID, membership.athleteID, athlete.athleteFName,athlete.athleteLName, membership.membershipPlan,membership.dateOfStart, membership.dateOfEnd, membership.membershipFee, membership.membershipStatus FROM membership JOIN athlete ON membership.athleteID = athlete.athleteID WHERE membership.membershipID LIKE %s OR membership.athleteID LIKE %s OR athlete.athleteFName LIKE %s OR athlete.athleteLName LIKE %s OR membership.membershipPlan LIKE %s OR membership.membershipStatus LIKE %s",
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

        for row in membership_table.get_children():
            membership_table.delete(row)

        for record in records:
            membership_table.insert("", END, values=record)

        connection.close()

    def load_memberships():
        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT membership.membershipID, membership.athleteID, athlete.athleteFName, athlete.athleteLName,membership.membershipPlan,membership.dateOfStart,membership.dateOfEnd,membership.membershipFee,membership.membershipStatus from membership Join athlete on membership.athleteID = athlete.athleteID"
        )

        records = cursor.fetchall()

        for row in membership_table.get_children():
            membership_table.delete(row)

        for record in records:
            membership_table.insert("", END, values=record)

        connection.close()

    def add_membership():
        membership_id = membership_id_entry.get()
        membership_type = membership_type_entry.get()
        start_date = start_date_entry.get()
        end_date = end_date_entry.get()
        membership_fee = membership_fee_entry.get()
        membership_status = membership_status_entry.get()
        athlete_id = athlete_id_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO membership (membershipID,athleteID, membershipPlan ,dateOfStart, dateOfEnd, membershipFee, membershipStatus) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (
                membership_id,
                athlete_id,
                membership_type,
                start_date,
                end_date,
                membership_fee,
                membership_status,
            ),
        )

        connection.commit()

        cursor.execute(
            "SELECT athleteFName, athleteLName FROM athlete WHERE athleteID = %s",
            (athlete_id,),
        )

        athlete_record = cursor.fetchone()

        connection.close()

        membership_table.insert(
            "",
            END,
            values=(
                membership_id,
                athlete_id,
                athlete_record[0],
                athlete_record[1],
                membership_type,
                start_date,
                end_date,
                membership_fee,
                membership_status,
            ),
        )

    def clear_membership():
        membership_id_entry.delete(0, END)
        membership_type_entry.delete(0, END)
        start_date_entry.delete(0, END)
        end_date_entry.delete(0, END)
        membership_fee_entry.delete(0, END)
        membership_status_entry.delete(0, END)
        athlete_id_entry.delete(0, END)

    def delete_membership():
        membership_id = membership_id_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM membership WHERE membershipID = %s",
            (membership_id,),
        )

        connection.commit()
        connection.close()

        for row in membership_table.get_children():
            values = membership_table.item(row)["values"]

            if str(values[0]) == membership_id:
                membership_table.delete(row)
                break

    def update_membership():
        membership_id = membership_id_entry.get()
        athlete_id = athlete_id_entry.get()
        membership_type = membership_type_entry.get()
        start_date = start_date_entry.get()
        end_date = end_date_entry.get()
        membership_fee = membership_fee_entry.get()
        membership_status = membership_status_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "update membership set athleteID = %s, membershipPlan = %s, dateOfStart = %s, dateOfEnd = %s, membershipFee = %s, membershipStatus = %s where membershipID = %s",
            (
                athlete_id,
                membership_type,
                start_date,
                end_date,
                membership_fee,
                membership_status,
                membership_id,
            ),
        )

        connection.commit()

        cursor.execute(
            "SELECT athleteFName, athleteLName FROM athlete WHERE athleteID = %s",
            (athlete_id,),
        )

        athlete_record = cursor.fetchone()

        connection.close()

        for row in membership_table.get_children():
            values = membership_table.item(row)["values"]

            if str(values[0]) == membership_id:
                membership_table.item(
                    row,
                    values=(
                        membership_id,
                        athlete_id,
                        athlete_record[0],
                        athlete_record[1],
                        membership_type,
                        start_date,
                        end_date,
                        membership_fee,
                        membership_status,
                    ),
                )
                break

    def go_to_dashboard():
        from ProgenFC_modules.ProgenFCdashboard import dashboard

        window.destroy()
        dashboard()

    window = Tk()
    window.geometry("1536x1024")
    window.title("Membership Management")
    window.config(background="#0B1F33")

    heading = Label(
        window,
        text="Membership Management",
        font=("Arial", 28, "bold"),
        bg="#0B1F33",
        fg="#4CCB3A",
    )

    heading.place(x=600, y=20)

    membership_id_label = Label(
        window,
        text="Membership ID:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    athlete_id_label = Label(
        window,
        text="Athlete ID:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    athlete_id_label.place(x=170, y=80)

    athlete_id_entry = Entry(window, font=("Arial", 14))
    athlete_id_entry.place(x=370, y=75, width=300, height=35)

    membership_id_label.place(x=170, y=140)

    membership_id_entry = Entry(window, font=("Arial", 14))

    membership_id_entry.place(x=370, y=135, width=300, height=35)

    membership_type_label = Label(
        window,
        text="Membership Type:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    membership_type_label.place(x=170, y=200)

    membership_type_entry = Entry(window, font=("Arial", 14))

    membership_type_entry.place(x=370, y=195, width=300, height=35)

    start_date_label = Label(
        window,
        text="Date of Start:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    start_date_label.place(x=170, y=260)

    start_date_entry = Entry(window, font=("Arial", 14))

    start_date_entry.place(x=370, y=255, width=300, height=35)

    end_date_label = Label(
        window,
        text="Date of End:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    end_date_label.place(x=170, y=320)

    end_date_entry = Entry(window, font=("Arial", 14))

    end_date_entry.place(x=370, y=315, width=300, height=35)

    membership_fee_label = Label(
        window,
        text="Membership Fee:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    membership_fee_label.place(x=170, y=380)

    membership_fee_entry = Entry(window, font=("Arial", 14))

    membership_fee_entry.place(x=370, y=375, width=300, height=35)

    membership_status_label = Label(
        window,
        text="Membership Status:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    membership_status_label.place(x=170, y=440)

    membership_status_entry = Entry(window, font=("Arial", 14))

    membership_status_entry.place(x=370, y=435, width=300, height=35)

    search_entry = Entry(window, font=("Arial", 13))

    search_entry.place(x=200, y=593, width=940, height=35)

    search_button = Button(
        window,
        text="🔍    Search",
        font=("Arial", 13, "bold"),
        command=search_membership,
    )

    search_button.place(x=1160, y=593, width=120, height=35)

    add_button = Button(
        window,
        text=" ➕ Add",
        font=("Arial", 13, "bold"),
        command=add_membership,
    )

    add_button.place(x=170, y=505, width=120, height=40)

    update_button = Button(
        window,
        text="✏️ Update",
        font=("Arial", 13, "bold"),
        command=update_membership,
    )

    update_button.place(x=310, y=505, width=120, height=40)

    delete_button = Button(
        window,
        text=" 🗑️ Delete",
        font=("Arial", 13, "bold"),
        command=delete_membership,
    )

    delete_button.place(x=450, y=505, width=120, height=40)

    clear_button = Button(
        window,
        text=" ♻️ Clear",
        font=("Arial", 13, "bold"),
        command=clear_membership,
    )

    clear_button.place(x=590, y=505, width=120, height=40)

    membership_table = ttk.Treeview(
        window,
        columns=(
            "membershipID",
            "athleteID",
            "athleteFName",
            "athleteLName",
            "membershipType",
            "dateOfStart",
            "dateOfEnd",
            "membershipFee",
            "membershipStatus",
        ),
        show="headings",
    )

    membership_table.heading("membershipID", text="Membership ID")
    membership_table.heading("athleteID", text="Athlete ID")
    membership_table.heading("athleteFName", text="First Name")
    membership_table.heading("athleteLName", text="Last Name")
    membership_table.heading("membershipType", text="Membership Plan")
    membership_table.heading("dateOfStart", text="Date of Start")
    membership_table.heading("dateOfEnd", text="Date of End")
    membership_table.heading("membershipFee", text="Membership Fee")
    membership_table.heading("membershipStatus", text="Status")

    membership_table.column("membershipID", width=120)
    membership_table.column("membershipType", width=130)
    membership_table.column("athleteID", width=100)
    membership_table.column("athleteFName", width=120)
    membership_table.column("athleteLName", width=120)
    membership_table.column("dateOfStart", width=120)
    membership_table.column("dateOfEnd", width=120)
    membership_table.column("membershipFee", width=120)
    membership_table.column("membershipStatus", width=100)

    membership_table.place(x=80, y=640, width=1350, height=300)

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

    load_memberships()

    window.mainloop()


if __name__ == "__main__":
    membership()
