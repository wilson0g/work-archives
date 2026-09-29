from tkinter import *
from tkinter import ttk

from progenFCdatabase import database_connection


def statistics():
    def load_statistics():
        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT PlayerPerformance.performanceID, athlete.athleteID, athlete.athleteFName, "
            "athlete.athleteLName, team.teamName, athlete.athletePosition, "
            "PlayerPerformance.goals, PlayerPerformance.assists, "
            "PlayerPerformance.cleanSheets, PlayerPerformance.overallScore "
            "FROM PlayerPerformance "
            "JOIN athlete ON PlayerPerformance.athleteID = athlete.athleteID "
            "JOIN team ON athlete.teamID = team.teamID "
            "ORDER BY PlayerPerformance.overallScore DESC"
        )

        records = cursor.fetchall()

        for row in statistics_table.get_children():
            statistics_table.delete(row)

        for record in records:
            statistics_table.insert("", END, values=record)

        connection.close()

    def view_statistics():
        view_mode = view_mode_entry.get()
        team_name = team_name_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        if view_mode == "By Team":
            cursor.execute(
                "SELECT PlayerPerformance.performanceID, athlete.athleteID, athlete.athleteFName, "
                "athlete.athleteLName, team.teamName, athlete.athletePosition, "
                "PlayerPerformance.goals, PlayerPerformance.assists, "
                "PlayerPerformance.cleanSheets, PlayerPerformance.overallScore "
                "FROM PlayerPerformance "
                "JOIN athlete ON PlayerPerformance.athleteID = athlete.athleteID "
                "JOIN team ON athlete.teamID = team.teamID "
                "WHERE team.teamName = %s "
                "ORDER BY PlayerPerformance.overallScore DESC",
                (team_name,),
            )

        else:
            cursor.execute(
                "SELECT PlayerPerformance.performanceID, athlete.athleteID, athlete.athleteFName, "
                "athlete.athleteLName, team.teamName, athlete.athletePosition, "
                "PlayerPerformance.goals, PlayerPerformance.assists, "
                "PlayerPerformance.cleanSheets, PlayerPerformance.overallScore "
                "FROM PlayerPerformance "
                "JOIN athlete ON PlayerPerformance.athleteID = athlete.athleteID "
                "JOIN team ON athlete.teamID = team.teamID "
                "ORDER BY PlayerPerformance.overallScore DESC"
            )

        records = cursor.fetchall()

        for row in statistics_table.get_children():
            statistics_table.delete(row)

        for record in records:
            statistics_table.insert("", END, values=record)

        connection.close()

    def top_10():
        view_mode = view_mode_entry.get()
        team_name = team_name_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        if view_mode == "By Team":
            cursor.execute(
                "SELECT PlayerPerformance.performanceID, athlete.athleteID, athlete.athleteFName, "
                "athlete.athleteLName, team.teamName, athlete.athletePosition, "
                "PlayerPerformance.goals, PlayerPerformance.assists, "
                "PlayerPerformance.cleanSheets, PlayerPerformance.overallScore "
                "FROM PlayerPerformance "
                "JOIN athlete ON PlayerPerformance.athleteID = athlete.athleteID "
                "JOIN team ON athlete.teamID = team.teamID "
                "WHERE team.teamName = %s "
                "ORDER BY PlayerPerformance.overallScore DESC "
                "LIMIT 10",
                (team_name,),
            )

        else:
            cursor.execute(
                "SELECT PlayerPerformance.performanceID, athlete.athleteID, athlete.athleteFName, "
                "athlete.athleteLName, team.teamName, athlete.athletePosition, "
                "PlayerPerformance.goals, PlayerPerformance.assists, "
                "PlayerPerformance.cleanSheets, PlayerPerformance.overallScore "
                "FROM PlayerPerformance "
                "JOIN athlete ON PlayerPerformance.athleteID = athlete.athleteID "
                "JOIN team ON athlete.teamID = team.teamID "
                "ORDER BY PlayerPerformance.overallScore DESC "
                "LIMIT 10"
            )

        records = cursor.fetchall()

        for row in statistics_table.get_children():
            statistics_table.delete(row)

        for record in records:
            statistics_table.insert("", END, values=record)

        connection.close()

    def search_statistics():
        search_value = search_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT PlayerPerformance.performanceID, athlete.athleteID, athlete.athleteFName, "
            "athlete.athleteLName, team.teamName, athlete.athletePosition, "
            "PlayerPerformance.goals, PlayerPerformance.assists, "
            "PlayerPerformance.cleanSheets, PlayerPerformance.overallScore "
            "FROM PlayerPerformance "
            "JOIN athlete ON PlayerPerformance.athleteID = athlete.athleteID "
            "JOIN team ON athlete.teamID = team.teamID "
            "WHERE PlayerPerformance.performanceID LIKE %s "
            "OR athlete.athleteID LIKE %s "
            "OR athlete.athleteFName LIKE %s "
            "OR athlete.athleteLName LIKE %s "
            "OR team.teamName LIKE %s "
            "OR athlete.athletePosition LIKE %s "
            "ORDER BY PlayerPerformance.overallScore DESC",
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

        for row in statistics_table.get_children():
            statistics_table.delete(row)

        for record in records:
            statistics_table.insert("", END, values=record)

        connection.close()

    def clear_statistics():
        view_mode_entry.delete(0, END)
        team_name_entry.delete(0, END)
        search_entry.delete(0, END)

        view_mode_entry.set("None")
        team_name_entry.set("None")

        load_statistics()

    def go_to_dashboard():
        from ProgenFC_modules.ProgenFCdashboard import dashboard

        window.destroy()
        dashboard()

    window = Tk()
    window.geometry("1536x1024")
    window.title("Statistics Management")
    window.config(background="#0B1F33")

    heading = Label(
        window,
        text="Statistics Management",
        font=("Arial", 28, "bold"),
        bg="#0B1F33",
        fg="#4CCB3A",
    )

    heading.place(x=580, y=20)

    view_mode_label = Label(
        window,
        text="View Mode:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    view_mode_label.place(x=170, y=140)

    view_mode_entry = ttk.Combobox(
        window,
        font=("Arial", 14),
        values=(
            "None",
            "All Players",
            "By Team",
        ),
    )

    view_mode_entry.place(x=370, y=135, width=300, height=35)

    view_mode_entry.set("None")

    team_name_label = Label(
        window,
        text="Team Name:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    team_name_label.place(x=170, y=200)

    connection = database_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT teamName FROM team")

    teams = cursor.fetchall()

    connection.close()

    team_options = []

    for team_record in teams:
        team_options.append(team_record[0])

    team_options.insert(0, "None")

    team_name_entry = ttk.Combobox(
        window,
        font=("Arial", 14),
        values=team_options,
    )

    team_name_entry.place(x=370, y=195, width=300, height=35)

    team_name_entry.set("None")

    search_label = Label(
        window,
        text="Search Athlete:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    search_label.place(x=170, y=260)

    search_entry = Entry(
        window,
        font=("Arial", 14),
    )

    search_entry.place(x=370, y=255, width=300, height=35)

    view_button = Button(
        window,
        text="📊 View Statistics",
        font=("Arial", 13, "bold"),
        command=view_statistics,
    )

    view_button.place(x=170, y=350, width=170, height=40)

    top_10_button = Button(
        window,
        text="🏆 Top 10",
        font=("Arial", 13, "bold"),
        command=top_10,
    )

    top_10_button.place(x=360, y=350, width=140, height=40)

    clear_button = Button(
        window,
        text="♻️ Clear",
        font=("Arial", 13, "bold"),
        command=clear_statistics,
    )

    clear_button.place(x=520, y=350, width=140, height=40)

    search_button = Button(
        window,
        text="🔍 Search",
        font=("Arial", 13, "bold"),
        command=search_statistics,
    )

    search_button.place(x=690, y=350, width=140, height=40)

    statistics_table = ttk.Treeview(
        window,
        columns=(
            "performanceID",
            "athleteID",
            "athleteFName",
            "athleteLName",
            "teamName",
            "athletePosition",
            "goals",
            "assists",
            "cleanSheets",
            "overallScore",
        ),
        show="headings",
    )

    statistics_table.heading("performanceID", text="Performance ID")
    statistics_table.heading("athleteID", text="Athlete ID")
    statistics_table.heading("athleteFName", text="First Name")
    statistics_table.heading("athleteLName", text="Last Name")
    statistics_table.heading("teamName", text="Team Name")
    statistics_table.heading("athletePosition", text="Position")
    statistics_table.heading("goals", text="Goals")
    statistics_table.heading("assists", text="Assists")
    statistics_table.heading("cleanSheets", text="Clean Sheets")
    statistics_table.heading("overallScore", text="Overall Score")

    statistics_table.column("performanceID", width=120)
    statistics_table.column("athleteID", width=100)
    statistics_table.column("athleteFName", width=130)
    statistics_table.column("athleteLName", width=130)
    statistics_table.column("teamName", width=220)
    statistics_table.column("athletePosition", width=120)
    statistics_table.column("goals", width=80)
    statistics_table.column("assists", width=80)
    statistics_table.column("cleanSheets", width=110)
    statistics_table.column("overallScore", width=110)

    statistics_table.place(
        x=40,
        y=440,
        width=1400,
        height=430,
    )

    dashboard_button = Button(
        window,
        text="← Dashboard",
        font=("Arial", 13, "bold"),
        command=go_to_dashboard,
    )

    dashboard_button.place(
        x=30,
        y=25,
        width=130,
        height=40,
    )

    progen_logo = PhotoImage(file="ProgenFC_small_150.png")

    progen_logo_label = Label(
        window,
        image=progen_logo,
        bg="#0B1F33",
    )

    progen_logo_label.place(
        x=1400,
        y=95,
        anchor="center",
    )

    load_statistics()

    window.mainloop()


if __name__ == "__main__":
    statistics()
