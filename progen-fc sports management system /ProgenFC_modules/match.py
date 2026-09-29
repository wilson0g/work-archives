from tkinter import *
from tkinter import ttk

from progenFCdatabase import database_connection


def match():
    def search_match():
        search_value = search_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT matches.matchID, matches.teamID, team.teamName, matches.facilityID, facility.facilityName, "
            "matches.competitionID, competition.competitionName, matches.opponentName, matches.goalsScored, "
            "matches.goalsConceded, matches.matchResult "
            "FROM matches "
            "JOIN team ON matches.teamID = team.teamID "
            "JOIN facility ON matches.facilityID = facility.facilityID "
            "JOIN competition ON matches.competitionID = competition.competitionID "
            "WHERE matches.matchID LIKE %s OR matches.teamID LIKE %s OR team.teamName LIKE %s "
            "OR matches.facilityID LIKE %s OR facility.facilityName LIKE %s "
            "OR matches.competitionID LIKE %s OR competition.competitionName LIKE %s "
            "OR matches.opponentName LIKE %s OR matches.matchResult LIKE %s",
            (
                "%" + search_value + "%",
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

        for row in match_table.get_children():
            match_table.delete(row)

        for record in records:
            match_table.insert("", END, values=record)

        connection.close()

    def load_matches():
        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT matches.matchID, matches.teamID, team.teamName, matches.facilityID, facility.facilityName, "
            "matches.competitionID, competition.competitionName, matches.opponentName, matches.goalsScored, "
            "matches.goalsConceded, matches.matchResult "
            "FROM matches "
            "JOIN team ON matches.teamID = team.teamID "
            "JOIN facility ON matches.facilityID = facility.facilityID "
            "JOIN competition ON matches.competitionID = competition.competitionID"
        )

        records = cursor.fetchall()

        for row in match_table.get_children():
            match_table.delete(row)

        for record in records:
            match_table.insert("", END, values=record)

        connection.close()

    def add_match():
        match_id = match_id_entry.get()
        team_id = team_id_entry.get().split(" - ")[0]
        facility_id = facility_id_entry.get().split(" - ")[0]
        competition_id = competition_id_entry.get().split(" - ")[0]
        opponent_name = opponent_name_entry.get()
        goals_scored = goals_scored_entry.get()
        goals_conceded = goals_conceded_entry.get()

        if int(goals_scored) > int(goals_conceded):
            match_result = "Win"

        elif int(goals_scored) < int(goals_conceded):
            match_result = "Loss"

        else:
            match_result = "Draw"

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO matches "
            "(matchID, teamID, facilityID, competitionID, opponentName, goalsScored, goalsConceded, matchResult) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (
                match_id,
                team_id,
                facility_id,
                competition_id,
                opponent_name,
                goals_scored,
                goals_conceded,
                match_result,
            ),
        )

        connection.commit()

        cursor.execute(
            "SELECT matches.matchID, matches.teamID, team.teamName, matches.facilityID, facility.facilityName, "
            "matches.competitionID, competition.competitionName, matches.opponentName, matches.goalsScored, "
            "matches.goalsConceded, matches.matchResult "
            "FROM matches "
            "JOIN team ON matches.teamID = team.teamID "
            "JOIN facility ON matches.facilityID = facility.facilityID "
            "JOIN competition ON matches.competitionID = competition.competitionID "
            "WHERE matches.matchID = %s",
            (match_id,),
        )

        record = cursor.fetchone()

        connection.close()

        match_table.insert("", END, values=record)

    def clear_match():
        match_id_entry.delete(0, END)
        team_id_entry.delete(0, END)
        facility_id_entry.delete(0, END)
        competition_id_entry.delete(0, END)
        opponent_name_entry.delete(0, END)
        goals_scored_entry.delete(0, END)
        goals_conceded_entry.delete(0, END)
        match_result_entry.delete(0, END)

    def delete_match():
        match_id = match_id_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM matches WHERE matchID = %s",
            (match_id,),
        )

        connection.commit()
        connection.close()

        for row in match_table.get_children():
            values = match_table.item(row)["values"]

            if str(values[0]) == match_id:
                match_table.delete(row)
                break

    def update_match():
        match_id = match_id_entry.get()
        team_id = team_id_entry.get().split(" - ")[0]
        facility_id = facility_id_entry.get().split(" - ")[0]
        competition_id = competition_id_entry.get().split(" - ")[0]
        opponent_name = opponent_name_entry.get()
        goals_scored = goals_scored_entry.get()
        goals_conceded = goals_conceded_entry.get()

        if int(goals_scored) > int(goals_conceded):
            match_result = "Win"

        elif int(goals_scored) < int(goals_conceded):
            match_result = "Loss"

        else:
            match_result = "Draw"

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE matches SET teamID = %s, facilityID = %s, competitionID = %s, "
            "opponentName = %s, goalsScored = %s, goalsConceded = %s, matchResult = %s "
            "WHERE matchID = %s",
            (
                team_id,
                facility_id,
                competition_id,
                opponent_name,
                goals_scored,
                goals_conceded,
                match_result,
                match_id,
            ),
        )

        connection.commit()

        cursor.execute(
            "SELECT matches.matchID, matches.teamID, team.teamName, matches.facilityID, facility.facilityName, "
            "matches.competitionID, competition.competitionName, matches.opponentName, matches.goalsScored, "
            "matches.goalsConceded, matches.matchResult "
            "FROM matches "
            "JOIN team ON matches.teamID = team.teamID "
            "JOIN facility ON matches.facilityID = facility.facilityID "
            "JOIN competition ON matches.competitionID = competition.competitionID "
            "WHERE matches.matchID = %s",
            (match_id,),
        )

        record = cursor.fetchone()

        connection.close()

        for row in match_table.get_children():
            values = match_table.item(row)["values"]

            if str(values[0]) == match_id:
                match_table.item(row, values=record)
                break

    def go_to_dashboard():
        from ProgenFC_modules.ProgenFCdashboard import dashboard

        window.destroy()
        dashboard()

    window = Tk()
    window.geometry("1536x1024")
    window.title("Match Management")
    window.config(background="#0B1F33")

    heading = Label(
        window,
        text="Match Management",
        font=("Arial", 28, "bold"),
        bg="#0B1F33",
        fg="#4CCB3A",
    )

    heading.place(x=600, y=20)

    match_id_label = Label(
        window,
        text="Match ID:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    match_id_label.place(x=170, y=80)

    match_id_entry = Entry(window, font=("Arial", 14))

    match_id_entry.place(x=370, y=75, width=300, height=35)

    team_id_label = Label(
        window,
        text="Team:",
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

    facility_id_label = Label(
        window,
        text="Facility:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    facility_id_label.place(x=170, y=200)

    connection = database_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT facilityID, facilityName FROM facility")

    facilities = cursor.fetchall()

    connection.close()

    facility_options = []

    for facility_record in facilities:
        facility_options.append(facility_record[0] + " - " + facility_record[1])

    facility_id_entry = ttk.Combobox(
        window,
        font=("Arial", 14),
        values=facility_options,
    )

    facility_id_entry.place(x=370, y=195, width=300, height=35)

    competition_id_label = Label(
        window,
        text="Competition:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    competition_id_label.place(x=170, y=260)

    connection = database_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT competitionID, competitionName FROM competition")

    competitions = cursor.fetchall()

    connection.close()

    competition_options = []

    for competition_record in competitions:
        competition_options.append(
            competition_record[0] + " - " + competition_record[1]
        )

    competition_id_entry = ttk.Combobox(
        window,
        font=("Arial", 14),
        values=competition_options,
    )

    competition_id_entry.place(x=370, y=255, width=300, height=35)

    opponent_name_label = Label(
        window,
        text="Opponent Name:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    opponent_name_label.place(x=170, y=320)

    opponent_name_entry = Entry(window, font=("Arial", 14))

    opponent_name_entry.place(x=370, y=315, width=300, height=35)

    goals_scored_label = Label(
        window,
        text="Goals Scored:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    goals_scored_label.place(x=170, y=380)

    goals_scored_entry = Entry(window, font=("Arial", 14))

    goals_scored_entry.place(x=370, y=375, width=300, height=35)

    goals_conceded_label = Label(
        window,
        text="Goals Conceded:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    goals_conceded_label.place(x=170, y=440)

    goals_conceded_entry = Entry(window, font=("Arial", 14))

    goals_conceded_entry.place(x=370, y=435, width=300, height=35)

    match_result_label = Label(
        window,
        text="Match Result:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    match_result_label.place(x=760, y=380)

    match_result_entry = Entry(window, font=("Arial", 14))

    match_result_entry.place(x=950, y=375, width=250, height=35)

    search_entry = Entry(window, font=("Arial", 13))

    search_entry.place(x=200, y=593, width=940, height=35)

    search_button = Button(
        window,
        text="🔍    Search",
        font=("Arial", 13, "bold"),
        command=search_match,
    )

    search_button.place(x=1160, y=593, width=120, height=35)

    add_button = Button(
        window,
        text=" ➕ Add",
        font=("Arial", 13, "bold"),
        command=add_match,
    )

    add_button.place(x=170, y=505, width=120, height=40)

    update_button = Button(
        window,
        text="✏️ Update",
        font=("Arial", 13, "bold"),
        command=update_match,
    )

    update_button.place(x=310, y=505, width=120, height=40)

    delete_button = Button(
        window,
        text=" 🗑️ Delete",
        font=("Arial", 13, "bold"),
        command=delete_match,
    )

    delete_button.place(x=450, y=505, width=120, height=40)

    clear_button = Button(
        window,
        text=" ♻️ Clear",
        font=("Arial", 13, "bold"),
        command=clear_match,
    )

    clear_button.place(x=590, y=505, width=120, height=40)

    match_table = ttk.Treeview(
        window,
        columns=(
            "matchID",
            "teamID",
            "teamName",
            "facilityID",
            "facilityName",
            "competitionID",
            "competitionName",
            "opponentName",
            "goalsScored",
            "goalsConceded",
            "matchResult",
        ),
        show="headings",
    )

    match_table.heading("matchID", text="Match ID")
    match_table.heading("teamID", text="Team ID")
    match_table.heading("teamName", text="Team Name")
    match_table.heading("facilityID", text="Facility ID")
    match_table.heading("facilityName", text="Facility Name")
    match_table.heading("competitionID", text="Competition ID")
    match_table.heading("competitionName", text="Competition Name")
    match_table.heading("opponentName", text="Opponent")
    match_table.heading("goalsScored", text="Goals Scored")
    match_table.heading("goalsConceded", text="Goals Conceded")
    match_table.heading("matchResult", text="Result")

    match_table.column("matchID", width=90)
    match_table.column("teamID", width=90)
    match_table.column("teamName", width=180)
    match_table.column("facilityID", width=90)
    match_table.column("facilityName", width=180)
    match_table.column("competitionID", width=110)
    match_table.column("competitionName", width=180)
    match_table.column("opponentName", width=150)
    match_table.column("goalsScored", width=100)
    match_table.column("goalsConceded", width=110)
    match_table.column("matchResult", width=90)

    match_table.place(x=40, y=640, width=1400, height=300)

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

    load_matches()

    window.mainloop()


if __name__ == "__main__":
    match()
