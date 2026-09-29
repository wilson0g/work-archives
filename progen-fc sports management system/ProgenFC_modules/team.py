from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from progenFCdatabase import database_connection


def team():
    def search_team():
        search_value = search_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT team.teamID, team.teamName, team.teamBracket, team.coachID, coach.coachFName, coach.coachLName "
            "FROM team JOIN coach ON team.coachID = coach.coachID "
            "WHERE team.teamID LIKE %s OR team.teamName LIKE %s OR team.teamBracket LIKE %s OR team.coachID LIKE %s OR coach.coachFName LIKE %s OR coach.coachLName LIKE %s",
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

        for row in team_table.get_children():
            team_table.delete(row)

        for record in records:
            team_table.insert("", END, values=record)

        connection.close()

    def load_teams():
        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT team.teamID, team.teamName, team.teamBracket, team.coachID, coach.coachFName, coach.coachLName "
            "FROM team JOIN coach ON team.coachID = coach.coachID"
        )

        records = cursor.fetchall()

        for row in team_table.get_children():
            team_table.delete(row)

        for record in records:
            team_table.insert("", END, values=record)

        connection.close()

    def add_team():
        team_id = team_id_entry.get().split(" - ")[0]
        team_name = team_name_entry.get()
        team_bracket = team_bracket_entry.get()
        coach_id = coach_id_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO team (teamID, teamName, teamBracket, coachID) VALUES (%s, %s, %s, %s)",
            (
                team_id,
                team_name,
                team_bracket,
                coach_id,
            ),
        )

        connection.commit()

        cursor.execute(
            "SELECT coachFName, coachLName FROM coach WHERE coachID = %s",
            (coach_id,),
        )

        coach_record = cursor.fetchone()

        connection.close()

        team_table.insert(
            "",
            END,
            values=(
                team_id,
                team_name,
                team_bracket,
                coach_id,
                coach_record[0],
                coach_record[1],
            ),
        )

    def clear_team():
        team_id_entry.delete(0, END)
        team_name_entry.delete(0, END)
        team_bracket_entry.delete(0, END)
        coach_id_entry.delete(0, END)

    def delete_team():
        team_id = team_id_entry.get().split(" - ")[0]

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM team WHERE teamID = %s",
            (team_id,),
        )

        connection.commit()
        connection.close()

        for row in team_table.get_children():
            values = team_table.item(row)["values"]

            if str(values[0]) == team_id:
                team_table.delete(row)
                break

    def update_team():
        team_id = team_id_entry.get().split(" - ")[0]
        team_name = team_name_entry.get()
        team_bracket = team_bracket_entry.get()
        coach_id = coach_id_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE team SET teamName = %s, teamBracket = %s, coachID = %s WHERE teamID = %s",
            (
                team_name,
                team_bracket,
                coach_id,
                team_id,
            ),
        )

        connection.commit()

        cursor.execute(
            "SELECT coachFName, coachLName FROM coach WHERE coachID = %s",
            (coach_id,),
        )

        coach_record = cursor.fetchone()

        connection.close()

        for row in team_table.get_children():
            values = team_table.item(row)["values"]

            if str(values[0]) == team_id:
                team_table.item(
                    row,
                    values=(
                        team_id,
                        team_name,
                        team_bracket,
                        coach_id,
                        coach_record[0],
                        coach_record[1],
                    ),
                )
                break

    def view_athletes():
        team_name = team_name_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT teamID FROM team WHERE teamName = %s",
            (team_name,),
        )

        team_record = cursor.fetchone()

        team_id = team_record[0]

        cursor.execute(
            "SELECT athleteID, athleteFName, athleteLName, athleteDOB, athleteGender, athletePhone, athleteEmail, athletePosition FROM athlete WHERE teamID = %s",
            (team_id,),
        )

        records = cursor.fetchall()

        connection.close()

        athlete_window = Toplevel(window)
        athlete_window.geometry("1200x600")
        athlete_window.title("Team Athletes")
        athlete_window.config(background="#0B1F33")

        athlete_heading = Label(
            athlete_window,
            text="Athletes in Team " + team_name,
            font=("Arial", 25, "bold"),
            bg="#0B1F33",
            fg="#4CCB3A",
        )

        athlete_heading.place(x=430, y=40)

        athlete_table = ttk.Treeview(
            athlete_window,
            columns=(
                "athleteID",
                "athleteFName",
                "athleteLName",
                "athleteDOB",
                "athleteGender",
                "athletePhone",
                "athleteEmail",
                "athletePosition",
            ),
            show="headings",
        )

        athlete_table.heading("athleteID", text="Athlete ID")
        athlete_table.heading("athleteFName", text="First Name")
        athlete_table.heading("athleteLName", text="Last Name")
        athlete_table.heading("athleteDOB", text="Date of Birth")
        athlete_table.heading("athleteGender", text="Gender")
        athlete_table.heading("athletePhone", text="Phone")
        athlete_table.heading("athleteEmail", text="Email")
        athlete_table.heading("athletePosition", text="Position")

        athlete_table.column("athleteID", width=100)
        athlete_table.column("athleteFName", width=130)
        athlete_table.column("athleteLName", width=130)
        athlete_table.column("athleteDOB", width=120)
        athlete_table.column("athleteGender", width=100)
        athlete_table.column("athletePhone", width=130)
        athlete_table.column("athleteEmail", width=220)
        athlete_table.column("athletePosition", width=130)

        athlete_table.place(x=40, y=120, width=1120, height=400)

        for record in records:
            athlete_table.insert("", END, values=record)

        # ---------------- ADD ATHLETE ----------------

        def open_add_athlete():
            add_athlete_window = Toplevel(athlete_window)
            add_athlete_window.geometry("600x600")
            add_athlete_window.title("Add Athlete")
            add_athlete_window.config(background="#0B1F33")

            add_heading = Label(
                add_athlete_window,
                text="Add Athlete",
                font=("Arial", 25, "bold"),
                bg="#0B1F33",
                fg="#4CCB3A",
            )

            add_heading.place(x=210, y=25)

            athlete_id_label = Label(
                add_athlete_window,
                text="Athlete ID:",
                font=("Arial", 13, "bold"),
                bg="#0B1F33",
                fg="white",
            )

            athlete_id_label.place(x=60, y=100)

            athlete_id_entry = Entry(
                add_athlete_window,
                font=("Arial", 13),
            )

            athlete_id_entry.place(x=230, y=95, width=280, height=30)

            athlete_fname_label = Label(
                add_athlete_window,
                text="First Name:",
                font=("Arial", 13, "bold"),
                bg="#0B1F33",
                fg="white",
            )

            athlete_fname_label.place(x=60, y=150)

            athlete_fname_entry = Entry(
                add_athlete_window,
                font=("Arial", 13),
            )

            athlete_fname_entry.place(x=230, y=145, width=280, height=30)

            athlete_lname_label = Label(
                add_athlete_window,
                text="Last Name:",
                font=("Arial", 13, "bold"),
                bg="#0B1F33",
                fg="white",
            )

            athlete_lname_label.place(x=60, y=200)

            athlete_lname_entry = Entry(
                add_athlete_window,
                font=("Arial", 13),
            )

            athlete_lname_entry.place(x=230, y=195, width=280, height=30)

            athlete_dob_label = Label(
                add_athlete_window,
                text="Date of Birth:",
                font=("Arial", 13, "bold"),
                bg="#0B1F33",
                fg="white",
            )

            athlete_dob_label.place(x=60, y=250)

            athlete_dob_entry = Entry(
                add_athlete_window,
                font=("Arial", 13),
            )

            athlete_dob_entry.place(x=230, y=245, width=280, height=30)

            athlete_gender_label = Label(
                add_athlete_window,
                text="Gender:",
                font=("Arial", 13, "bold"),
                bg="#0B1F33",
                fg="white",
            )

            athlete_gender_label.place(x=60, y=300)

            athlete_gender_entry = Entry(
                add_athlete_window,
                font=("Arial", 13),
            )
            athlete_gender_entry.place(x=230, y=295, width=280, height=30)

            athlete_phone_label = Label(
                add_athlete_window,
                text="Phone:",
                font=("Arial", 13, "bold"),
                bg="#0B1F33",
                fg="white",
            )
            athlete_phone_label.place(x=60, y=350)

            athlete_phone_entry = Entry(
                add_athlete_window,
                font=("Arial", 13),
            )
            athlete_phone_entry.place(x=230, y=345, width=280, height=30)

            athlete_email_label = Label(
                add_athlete_window,
                text="Email:",
                font=("Arial", 13, "bold"),
                bg="#0B1F33",
                fg="white",
            )
            athlete_email_label.place(x=60, y=400)

            athlete_email_entry = Entry(
                add_athlete_window,
                font=("Arial", 13),
            )
            athlete_email_entry.place(x=230, y=395, width=280, height=30)

            athlete_position_label = Label(
                add_athlete_window,
                text="Position:",
                font=("Arial", 13, "bold"),
                bg="#0B1F33",
                fg="white",
            )
            athlete_position_label.place(x=60, y=450)

            athlete_position_entry = Entry(
                add_athlete_window,
                font=("Arial", 13),
            )
            athlete_position_entry.place(x=230, y=445, width=280, height=30)

            def add_athlete():
                athlete_id = athlete_id_entry.get()
                athlete_fname = athlete_fname_entry.get()
                athlete_lname = athlete_lname_entry.get()
                athlete_dob = athlete_dob_entry.get()
                athlete_gender = athlete_gender_entry.get()
                athlete_phone = athlete_phone_entry.get()
                athlete_email = athlete_email_entry.get()
                athlete_position = athlete_position_entry.get()

                connection = database_connection()
                cursor = connection.cursor()

                # Check if Athlete ID already exists
                cursor.execute(
                    "SELECT athleteID FROM athlete WHERE athleteID = %s",
                    (athlete_id,),
                )

                existing_athlete = cursor.fetchone()

                if existing_athlete is not None:
                    connection.close()

                    messagebox.showerror(
                        "Duplicate Athlete ID",
                        "Athlete ID already exists. Record rejected.",
                    )

                    return

                cursor.execute(
                    "INSERT INTO athlete "
                    "(athleteID, athleteFName, athleteLName, athleteDOB, athleteGender, athletePhone, athleteEmail, teamID, athletePosition) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        athlete_id,
                        athlete_fname,
                        athlete_lname,
                        athlete_dob,
                        athlete_gender,
                        athlete_phone,
                        athlete_email,
                        team_id,
                        athlete_position,
                    ),
                )

                connection.commit()
                connection.close()

                athlete_table.insert(
                    "",
                    END,
                    values=(
                        athlete_id,
                        athlete_fname,
                        athlete_lname,
                        athlete_dob,
                        athlete_gender,
                        athlete_phone,
                        athlete_email,
                        athlete_position,
                    ),
                )

                add_athlete_window.destroy()

            save_athlete_button = Button(
                add_athlete_window,
                text="➕ Add Athlete",
                font=("Arial", 13, "bold"),
                command=add_athlete,
            )

            save_athlete_button.place(
                x=230,
                y=510,
                width=180,
                height=40,
            )

        add_athlete_button = Button(
            athlete_window,
            text="➕ Add Athlete",
            font=("Arial", 13, "bold"),
            command=open_add_athlete,
        )

        add_athlete_button.place(
            x=40,
            y=540,
            width=150,
            height=40,
        )

    def go_to_dashboard():
        from ProgenFC_modules.ProgenFCdashboard import dashboard

        window.destroy()
        dashboard()

    window = Tk()
    window.geometry("1536x1024")
    window.title("Team Management")
    window.config(background="#0B1F33")

    heading = Label(
        window,
        text="Team Management",
        font=("Arial", 28, "bold"),
        bg="#0B1F33",
        fg="#4CCB3A",
    )

    heading.place(x=600, y=20)

    team_id_label = Label(
        window,
        text="Team ID:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    team_id_label.place(x=170, y=140)

    connection = database_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT teamID, teamName FROM team")

    teams = cursor.fetchall()

    connection.close()

    team_options = []

    for team_record in teams:
        team_options.append(team_record[0] + " - " + team_record[1])

    team_id_entry = ttk.Combobox(
        window,
        font=("Arial", 14),
        values=team_options,
    )

    team_id_entry.place(x=370, y=135, width=300, height=35)

    team_name_label = Label(
        window,
        text="Team Name:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    team_name_label.place(x=170, y=200)

    team_name_options = []

    for team_record in teams:
        team_name_options.append(team_record[1])

    team_name_entry = ttk.Combobox(
        window,
        font=("Arial", 14),
        values=team_name_options,
    )

    team_name_entry.place(x=370, y=195, width=300, height=35)

    team_bracket_label = Label(
        window,
        text="Team Bracket:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    team_bracket_label.place(x=170, y=260)

    team_bracket_entry = Entry(window, font=("Arial", 14))

    team_bracket_entry.place(x=370, y=255, width=300, height=35)

    coach_id_label = Label(
        window,
        text="Coach ID:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    coach_id_label.place(x=170, y=320)

    coach_id_entry = Entry(window, font=("Arial", 14))

    coach_id_entry.place(x=370, y=315, width=300, height=35)

    search_entry = Entry(window, font=("Arial", 13))

    search_entry.place(x=200, y=593, width=940, height=35)

    search_button = Button(
        window,
        text="🔍    Search",
        font=("Arial", 13, "bold"),
        command=search_team,
    )

    search_button.place(x=1160, y=593, width=120, height=35)

    add_button = Button(
        window,
        text=" ➕ Add",
        font=("Arial", 13, "bold"),
        command=add_team,
    )

    add_button.place(x=170, y=505, width=120, height=40)

    update_button = Button(
        window,
        text="✏️ Update",
        font=("Arial", 13, "bold"),
        command=update_team,
    )

    update_button.place(x=310, y=505, width=120, height=40)

    delete_button = Button(
        window,
        text=" 🗑️ Delete",
        font=("Arial", 13, "bold"),
        command=delete_team,
    )

    delete_button.place(x=450, y=505, width=120, height=40)

    clear_button = Button(
        window,
        text=" ♻️ Clear",
        font=("Arial", 13, "bold"),
        command=clear_team,
    )

    clear_button.place(x=590, y=505, width=120, height=40)

    view_athletes_button = Button(
        window,
        text="👥 View Athletes",
        font=("Arial", 13, "bold"),
        command=view_athletes,
    )

    view_athletes_button.place(x=730, y=505, width=150, height=40)

    team_table = ttk.Treeview(
        window,
        columns=(
            "teamID",
            "teamName",
            "teamBracket",
            "coachID",
            "coachFName",
            "coachLName",
        ),
        show="headings",
    )

    team_table.heading("teamID", text="Team ID")
    team_table.heading("teamName", text="Team Name")
    team_table.heading("teamBracket", text="Team Bracket")
    team_table.heading("coachID", text="Coach ID")
    team_table.heading("coachFName", text="Coach First Name")
    team_table.heading("coachLName", text="Coach Last Name")

    team_table.column("teamID", width=120)
    team_table.column("teamName", width=250)
    team_table.column("teamBracket", width=200)
    team_table.column("coachID", width=120)
    team_table.column("coachFName", width=160)
    team_table.column("coachLName", width=160)

    team_table.place(x=80, y=640, width=1350, height=300)

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

    load_teams()

    window.mainloop()


if __name__ == "__main__":
    team()
