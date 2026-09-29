from tkinter import *
from tkinter import ttk

from progenFCdatabase import database_connection


def coach():
    def search_coach():
        search_value = search_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT coachID, coachFName, coachLName, coachPhone, coachEmail FROM coach WHERE coachID LIKE %s OR coachFName LIKE %s OR coachLName LIKE %s OR coachPhone LIKE %s OR coachEmail LIKE %s",
            (
                "%" + search_value + "%",
                "%" + search_value + "%",
                "%" + search_value + "%",
                "%" + search_value + "%",
                "%" + search_value + "%",
            ),
        )

        records = cursor.fetchall()

        for row in coach_table.get_children():
            coach_table.delete(row)

        for record in records:
            coach_table.insert("", END, values=record)

        connection.close()

    def load_coaches():
        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT coachID, coachFName, coachLName, coachPhone, coachEmail FROM coach"
        )

        records = cursor.fetchall()

        for row in coach_table.get_children():
            coach_table.delete(row)

        for record in records:
            coach_table.insert("", END, values=record)

        connection.close()

    def add_coach():
        coach_id = coach_id_entry.get()
        coach_fname = coach_fname_entry.get()
        coach_lname = coach_lname_entry.get()
        coach_phone = coach_phone_entry.get()
        coach_email = coach_email_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO coach (coachID, coachFName, coachLName, coachPhone, coachEmail) VALUES (%s, %s, %s, %s, %s)",
            (
                coach_id,
                coach_fname,
                coach_lname,
                coach_phone,
                coach_email,
            ),
        )

        connection.commit()
        connection.close()

        coach_table.insert(
            "",
            END,
            values=(
                coach_id,
                coach_fname,
                coach_lname,
                coach_phone,
                coach_email,
            ),
        )

    def clear_coach():
        coach_id_entry.delete(0, END)
        coach_fname_entry.delete(0, END)
        coach_lname_entry.delete(0, END)
        coach_phone_entry.delete(0, END)
        coach_email_entry.delete(0, END)

    def delete_coach():
        coach_id = coach_id_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM coach WHERE coachID = %s",
            (coach_id,),
        )

        connection.commit()
        connection.close()

        for row in coach_table.get_children():
            values = coach_table.item(row)["values"]

            if str(values[0]) == coach_id:
                coach_table.delete(row)
                break

    def update_coach():
        coach_id = coach_id_entry.get()
        coach_fname = coach_fname_entry.get()
        coach_lname = coach_lname_entry.get()
        coach_phone = coach_phone_entry.get()
        coach_email = coach_email_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE coach SET coachFName = %s, coachLName = %s, coachPhone = %s, coachEmail = %s WHERE coachID = %s",
            (
                coach_fname,
                coach_lname,
                coach_phone,
                coach_email,
                coach_id,
            ),
        )

        connection.commit()
        connection.close()

        for row in coach_table.get_children():
            values = coach_table.item(row)["values"]

            if str(values[0]) == coach_id:
                coach_table.item(
                    row,
                    values=(
                        coach_id,
                        coach_fname,
                        coach_lname,
                        coach_phone,
                        coach_email,
                    ),
                )
                break

    def go_to_dashboard():
        from ProgenFC_modules.ProgenFCdashboard import dashboard

        window.destroy()
        dashboard()

    window = Tk()
    window.geometry("1536x1024")
    window.title("Coach Management")
    window.config(background="#0B1F33")

    heading = Label(
        window,
        text="Coach Management",
        font=("Arial", 28, "bold"),
        bg="#0B1F33",
        fg="#4CCB3A",
    )

    heading.place(x=600, y=20)

    coach_id_label = Label(
        window,
        text="Coach ID:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    coach_id_label.place(x=170, y=140)

    coach_id_entry = Entry(window, font=("Arial", 14))

    coach_id_entry.place(x=370, y=135, width=300, height=35)

    coach_fname_label = Label(
        window,
        text="First Name:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    coach_fname_label.place(x=170, y=200)

    coach_fname_entry = Entry(window, font=("Arial", 14))

    coach_fname_entry.place(x=370, y=195, width=300, height=35)

    coach_lname_label = Label(
        window,
        text="Last Name:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    coach_lname_label.place(x=170, y=260)

    coach_lname_entry = Entry(window, font=("Arial", 14))

    coach_lname_entry.place(x=370, y=255, width=300, height=35)

    coach_phone_label = Label(
        window,
        text="Phone:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    coach_phone_label.place(x=170, y=320)

    coach_phone_entry = Entry(window, font=("Arial", 14))

    coach_phone_entry.place(x=370, y=315, width=300, height=35)

    coach_email_label = Label(
        window,
        text="Email:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    coach_email_label.place(x=170, y=380)

    coach_email_entry = Entry(window, font=("Arial", 14))

    coach_email_entry.place(x=370, y=375, width=300, height=35)

    search_entry = Entry(window, font=("Arial", 13))

    search_entry.place(x=200, y=593, width=940, height=35)

    search_button = Button(
        window,
        text="🔍    Search",
        font=("Arial", 13, "bold"),
        command=search_coach,
    )

    search_button.place(x=1160, y=593, width=120, height=35)

    add_button = Button(
        window,
        text=" ➕ Add",
        font=("Arial", 13, "bold"),
        command=add_coach,
    )

    add_button.place(x=170, y=505, width=120, height=40)

    update_button = Button(
        window,
        text="✏️ Update",
        font=("Arial", 13, "bold"),
        command=update_coach,
    )

    update_button.place(x=310, y=505, width=120, height=40)

    delete_button = Button(
        window,
        text=" 🗑️ Delete",
        font=("Arial", 13, "bold"),
        command=delete_coach,
    )

    delete_button.place(x=450, y=505, width=120, height=40)

    clear_button = Button(
        window,
        text=" ♻️ Clear",
        font=("Arial", 13, "bold"),
        command=clear_coach,
    )

    clear_button.place(x=590, y=505, width=120, height=40)

    coach_table = ttk.Treeview(
        window,
        columns=(
            "coachID",
            "coachFName",
            "coachLName",
            "coachPhone",
            "coachEmail",
        ),
        show="headings",
    )

    coach_table.heading("coachID", text="Coach ID")
    coach_table.heading("coachFName", text="First Name")
    coach_table.heading("coachLName", text="Last Name")
    coach_table.heading("coachPhone", text="Phone")
    coach_table.heading("coachEmail", text="Email")

    coach_table.column("coachID", width=120)
    coach_table.column("coachFName", width=160)
    coach_table.column("coachLName", width=160)
    coach_table.column("coachPhone", width=160)
    coach_table.column("coachEmail", width=250)

    coach_table.place(x=80, y=640, width=1350, height=300)

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

    load_coaches()

    window.mainloop()


if __name__ == "__main__":
    coach()
