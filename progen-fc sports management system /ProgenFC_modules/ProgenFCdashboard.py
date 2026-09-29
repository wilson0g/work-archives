from tkinter import *
import os
import sys
import subprocess

current_folder = os.path.dirname(os.path.abspath(__file__))

project_folder = os.path.dirname(current_folder)

if project_folder not in sys.path:
    sys.path.insert(0, project_folder)

from progenFCdatabase import database_connection
import user_session


def dashboard():
    window = Tk()
    window.geometry("1536x1024")
    window.title("Progen FC Sports Club Management System")
    window.config(background="#0B1F33")
    username = user_session.current_username
    user_role = user_session.current_role

    def tomembership():
        from ProgenFC_modules.membership import membership

        window.destroy()
        membership()

    def tocoach():
        from ProgenFC_modules.coach import coach

        window.destroy()
        coach()

    def toteam():
        from ProgenFC_modules.team import team

        window.destroy()
        team()

    def tocompetition():
        from ProgenFC_modules.competition import competition

        window.destroy()
        competition()

    def tofacility():
        from ProgenFC_modules.facility import facility

        window.destroy()
        facility()

    def topayment():
        from ProgenFC_modules.transaction import transaction

        window.destroy()
        transaction()

    def tomatch():
        from ProgenFC_modules.match import match

        window.destroy()
        match()

    def tostatistics():
        from ProgenFC_modules.statistics import statistics

        window.destroy()
        statistics()

    def logout():
        user_session.current_user_id = None
        user_session.current_username = None
        user_session.current_role = None
        user_session.current_athlete_id = None
        user_session.current_coach_id = None
        window.destroy()
        login_page = os.path.join(project_folder, "progenFCloginpage.py")
        subprocess.Popen([sys.executable, login_page])

    connection = database_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT COUNT(*) FROM athlete")
    athlete_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM team")
    team_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM competition")
    competition_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM transaction")
    transaction_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM membership")
    membership_count = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM booking")

    booking_count = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM session")
    session_count = cursor.fetchone()[0]
    cursor.execute(
        "SELECT COUNT(*) FROM transaction WHERE transactionStatus = 'Completed'"
    )
    completed_transaction_count = cursor.fetchone()[0]
    cursor.execute(
        "SELECT matches.matchID, "
        "team.teamName, "
        "matches.opponentName, "
        "matches.goalsScored, "
        "matches.goalsConceded, "
        "matches.matchResult "
        "FROM matches "
        "JOIN team "
        "ON matches.teamID = team.teamID "
        "ORDER BY matches.matchID DESC "
        "LIMIT 5"
    )
    match_records = cursor.fetchall()
    cursor.execute(
        "SELECT transaction.transactionID, "
        "athlete.athleteFName, "
        "athlete.athleteLName, "
        "transaction.transactionDate, "
        "transaction.transactionAmount, "
        "transaction.transactionMedium, "
        "transaction.transactionStatus "
        "FROM transaction "
        "JOIN athlete "
        "ON transaction.athleteID = athlete.athleteID "
        "ORDER BY transaction.transactionDate DESC "
        "LIMIT 5"
    )
    transaction_records = cursor.fetchall()
    cursor.close()
    connection.close()
    icon = PhotoImage(file="ProgenFC database logo copy.png")
    window.iconphoto(True, icon)

    sidebar = Frame(window, bg="#081A2B")
    sidebar.place(x=0, y=0, width=230, height=1024)
    sidebar_logo_image = PhotoImage(file="ProgenFC_small_150.png")
    sidebar_logo = Label(sidebar, image=sidebar_logo_image, bg="#081A2B")
    sidebar_logo.place(x=40, y=15, width=150, height=150)
    club_name = Label(
        sidebar, text="PROGEN FC", font=("Arial", 18, "bold"), bg="#081A2B", fg="white"
    )
    club_name.place(x=55, y=165)

    club_subtitle = Label(
        sidebar,
        text="Sports Club Management System",
        font=("Arial", 8),
        bg="#081A2B",
        fg="#4CCB3A",
    )

    club_subtitle.place(x=35, y=195)

    membership_button = Button(
        sidebar,
        text=" 💳   Membership",
        font=("Arial", 13, "bold"),
        fg="#0B1F33",
        anchor="w",
        command=tomembership,
    )

    membership_button.place(x=20, y=240, width=190, height=45)
    coach_button = Button(
        sidebar,
        text=" 👤   Coaches",
        font=("Arial", 13, "bold"),
        fg="#0B1F33",
        anchor="w",
        command=tocoach,
    )

    coach_button.place(x=20, y=300, width=190, height=45)
    team_button = Button(
        sidebar,
        text=" 👥   Teams",
        font=("Arial", 13, "bold"),
        fg="#0B1F33",
        anchor="w",
        command=toteam,
    )
    team_button.place(x=20, y=360, width=190, height=45)
    competition_button = Button(
        sidebar,
        text=" 🏆   Competitions",
        font=("Arial", 13, "bold"),
        fg="#0B1F33",
        anchor="w",
        command=tocompetition,
    )

    competition_button.place(x=20, y=420, width=190, height=45)

    facility_button = Button(
        sidebar,
        text=" 📅   Facility Booking",
        font=("Arial", 13, "bold"),
        fg="#0B1F33",
        anchor="w",
        command=tofacility,
    )

    facility_button.place(x=20, y=480, width=190, height=45)
    payment_button = Button(
        sidebar,
        text=" 💵   Payments",
        font=("Arial", 13, "bold"),
        fg="#0B1F33",
        anchor="w",
        command=topayment,
    )

    payment_button.place(x=20, y=540, width=190, height=45)
    match_button = Button(
        sidebar,
        text=" ⚽   Matches",
        font=("Arial", 13, "bold"),
        fg="#0B1F33",
        anchor="w",
        command=tomatch,
    )
    match_button.place(x=20, y=600, width=190, height=45)

    statistics_button = Button(
        sidebar,
        text=" 📊   Statistics",
        font=("Arial", 13, "bold"),
        fg="#0B1F33",
        anchor="w",
        command=tostatistics,
    )
    statistics_button.place(x=20, y=660, width=190, height=45)
    if user_role == "Administrator":
        membership_button.config(state=NORMAL)
        coach_button.config(state=NORMAL)
        team_button.config(state=NORMAL)
        competition_button.config(state=NORMAL)
        facility_button.config(state=NORMAL)
        payment_button.config(state=NORMAL)
        match_button.config(state=NORMAL)
        statistics_button.config(state=NORMAL)
    elif user_role == "Coach":
        membership_button.config(state=NORMAL)
        coach_button.config(state=NORMAL)
        team_button.config(state=NORMAL)
        competition_button.config(state=NORMAL)
        facility_button.config(state=NORMAL)
        payment_button.config(state=NORMAL)
        match_button.config(state=NORMAL)
        statistics_button.config(state=NORMAL)

    elif user_role == "Finance Officer":
        membership_button.config(state=NORMAL)

        coach_button.config(state=NORMAL)

        team_button.config(state=NORMAL)

        competition_button.config(state=NORMAL)

        facility_button.config(state=NORMAL)

        payment_button.config(state=NORMAL)

        match_button.config(state=NORMAL)

        statistics_button.config(state=DISABLED)
    elif user_role == "Facility Manager":
        membership_button.config(state=DISABLED)

        coach_button.config(state=NORMAL)

        team_button.config(state=NORMAL)

        competition_button.config(state=NORMAL)

        facility_button.config(state=NORMAL)

        payment_button.config(state=DISABLED)

        match_button.config(state=NORMAL)

        statistics_button.config(state=DISABLED)
    elif user_role == "Competition Manager":
        membership_button.config(state=DISABLED)

        coach_button.config(state=NORMAL)

        team_button.config(state=NORMAL)

        competition_button.config(state=NORMAL)

        facility_button.config(state=NORMAL)

        payment_button.config(state=DISABLED)

        match_button.config(state=NORMAL)

        statistics_button.config(state=DISABLED)

    elif user_role == "Athlete":
        membership_button.config(state=NORMAL)
        coach_button.config(state=NORMAL)
        team_button.config(state=NORMAL)
        competition_button.config(state=NORMAL)
        facility_button.config(state=NORMAL)
        payment_button.config(state=NORMAL)
        match_button.config(state=NORMAL)
        statistics_button.config(state=NORMAL)
    else:
        membership_button.config(state=DISABLED)
        coach_button.config(state=DISABLED)
        team_button.config(state=DISABLED)
        competition_button.config(state=DISABLED)
        facility_button.config(state=DISABLED)
        payment_button.config(state=DISABLED)
        match_button.config(state=DISABLED)
        statistics_button.config(state=DISABLED)
    logout_button = Button(
        sidebar,
        text=" ↪️   Logout",
        font=("Arial", 13, "bold"),
        fg="red",
        anchor="w",
        command=logout,
    )

    logout_button.place(x=20, y=850, width=190, height=45)

    main_frame = Frame(window, bg="#0B1F33")

    main_frame.place(x=230, y=0, width=1306, height=1024)

    heading = Label(
        main_frame,
        text="Welcome To Progen FC!",
        font=("Arial", 30, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    heading.place(x=410, y=25)

    subheading = Label(
        main_frame,
        text="Sports Club Management Dashboard",
        font=("Arial", 15),
        bg="#0B1F33",
        fg="#C7CED6",
    )

    subheading.place(x=480, y=75)

    logged_in_user = Label(
        main_frame,
        text=("Logged in as: " + str(username) + " | " + str(user_role)),
        font=("Arial", 11, "bold"),
        bg="#0B1F33",
        fg="#4CCB3A",
    )

    logged_in_user.place(x=500, y=110)

    athlete_card = Frame(
        main_frame, bg="#13293D", highlightbackground="#4A6075", highlightthickness=1
    )

    athlete_card.place(x=70, y=150, width=240, height=125)

    athlete_number = Label(
        athlete_card,
        text=str(athlete_count),
        font=("Arial", 28, "bold"),
        bg="#13293D",
        fg="#4CCB3A",
    )

    athlete_number.place(x=85, y=25)

    athlete_text = Label(
        athlete_card,
        text="Total Athletes",
        font=("Arial", 13),
        bg="#13293D",
        fg="white",
    )

    athlete_text.place(x=75, y=78)

    team_card = Frame(
        main_frame, bg="#13293D", highlightbackground="#4A6075", highlightthickness=1
    )
    team_card.place(x=370, y=150, width=240, height=125)
    team_number = Label(
        team_card,
        text=str(team_count),
        font=("Arial", 28, "bold"),
        bg="#13293D",
        fg="#4CCB3A",
    )

    team_number.place(x=95, y=25)

    team_text = Label(
        team_card, text="Teams", font=("Arial", 13), bg="#13293D", fg="white"
    )

    team_text.place(x=100, y=78)

    competition_card = Frame(
        main_frame, bg="#13293D", highlightbackground="#4A6075", highlightthickness=1
    )

    competition_card.place(x=670, y=150, width=240, height=125)

    competition_number = Label(
        competition_card,
        text=str(competition_count),
        font=("Arial", 28, "bold"),
        bg="#13293D",
        fg="#4CCB3A",
    )

    competition_number.place(x=95, y=25)

    competition_text = Label(
        competition_card,
        text="Competitions",
        font=("Arial", 13),
        bg="#13293D",
        fg="white",
    )

    competition_text.place(x=75, y=78)

    transaction_card = Frame(
        main_frame, bg="#13293D", highlightbackground="#4A6075", highlightthickness=1
    )

    transaction_card.place(x=970, y=150, width=240, height=125)

    transaction_number = Label(
        transaction_card,
        text=str(transaction_count),
        font=("Arial", 28, "bold"),
        bg="#13293D",
        fg="#4CCB3A",
    )

    transaction_number.place(x=95, y=25)

    transaction_text = Label(
        transaction_card,
        text="Transactions",
        font=("Arial", 13),
        bg="#13293D",
        fg="white",
    )

    transaction_text.place(x=75, y=78)
    matches_frame = Frame(
        main_frame, bg="#13293D", highlightbackground="#4A6075", highlightthickness=1
    )

    matches_frame.place(x=70, y=320, width=570, height=330)

    matches_title = Label(
        matches_frame,
        text="⚽ Match Results",
        font=("Arial", 18, "bold"),
        bg="#13293D",
        fg="white",
    )

    matches_title.place(x=20, y=20)

    match_team_heading = Label(
        matches_frame,
        text="Team",
        font=("Arial", 11, "bold"),
        bg="#13293D",
        fg="#C7CED6",
    )

    match_team_heading.place(x=20, y=65)

    match_opponent_heading = Label(
        matches_frame,
        text="Opponent",
        font=("Arial", 11, "bold"),
        bg="#13293D",
        fg="#C7CED6",
    )

    match_opponent_heading.place(x=190, y=65)

    match_score_heading = Label(
        matches_frame,
        text="Score",
        font=("Arial", 11, "bold"),
        bg="#13293D",
        fg="#C7CED6",
    )

    match_score_heading.place(x=365, y=65)

    match_result_heading = Label(
        matches_frame,
        text="Result",
        font=("Arial", 11, "bold"),
        bg="#13293D",
        fg="#C7CED6",
    )

    match_result_heading.place(x=460, y=65)

    match_y = 105

    for match_record in match_records:
        team_name = match_record[1]

        opponent_name = match_record[2]

        goals_scored = match_record[3]

        goals_conceded = match_record[4]

        match_result = match_record[5]

        team_label = Label(
            matches_frame, text=team_name, font=("Arial", 10), bg="#13293D", fg="white"
        )

        team_label.place(x=20, y=match_y)

        opponent_label = Label(
            matches_frame,
            text=opponent_name,
            font=("Arial", 10),
            bg="#13293D",
            fg="white",
        )

        opponent_label.place(x=190, y=match_y)

        score_label = Label(
            matches_frame,
            text=(str(goals_scored) + " - " + str(goals_conceded)),
            font=("Arial", 10, "bold"),
            bg="#13293D",
            fg="white",
        )

        score_label.place(x=365, y=match_y)

        result_label = Label(
            matches_frame,
            text=match_result,
            font=("Arial", 10, "bold"),
            bg="#13293D",
            fg="#4CCB3A",
        )

        result_label.place(x=460, y=match_y)
        match_y = match_y + 40
    transactions_frame = Frame(
        main_frame, bg="#13293D", highlightbackground="#4A6075", highlightthickness=1
    )
    transactions_frame.place(x=680, y=320, width=570, height=330)
    transactions_title = Label(
        transactions_frame,
        text="💳 Recent Transactions",
        font=("Arial", 18, "bold"),
        bg="#13293D",
        fg="white",
    )
    transactions_title.place(x=20, y=20)
    transaction_name_heading = Label(
        transactions_frame,
        text="Athlete",
        font=("Arial", 11, "bold"),
        bg="#13293D",
        fg="#C7CED6",
    )
    transaction_name_heading.place(x=20, y=65)
    transaction_date_heading = Label(
        transactions_frame,
        text="Date",
        font=("Arial", 11, "bold"),
        bg="#13293D",
        fg="#C7CED6",
    )
    transaction_date_heading.place(x=180, y=65)
    transaction_amount_heading = Label(
        transactions_frame,
        text="Amount",
        font=("Arial", 11, "bold"),
        bg="#13293D",
        fg="#C7CED6",
    )
    transaction_amount_heading.place(x=300, y=65)
    transaction_status_heading = Label(
        transactions_frame,
        text="Status",
        font=("Arial", 11, "bold"),
        bg="#13293D",
        fg="#C7CED6",
    )
    transaction_status_heading.place(x=430, y=65)
    transaction_y = 105
    for transaction_record in transaction_records:
        athlete_name = transaction_record[1] + " " + transaction_record[2]
        transaction_date = transaction_record[3]
        transaction_amount = transaction_record[4]
        transaction_status = transaction_record[6]
        athlete_label = Label(
            transactions_frame,
            text=athlete_name,
            font=("Arial", 10),
            bg="#13293D",
            fg="white",
        )
        athlete_label.place(x=20, y=transaction_y)
        date_label = Label(
            transactions_frame,
            text=str(transaction_date),
            font=("Arial", 10),
            bg="#13293D",
            fg="white",
        )
        date_label.place(x=180, y=transaction_y)
        amount_label = Label(
            transactions_frame,
            text=("GHS " + str(transaction_amount)),
            font=("Arial", 10),
            bg="#13293D",
            fg="white",
        )
        amount_label.place(x=300, y=transaction_y)
        status_label = Label(
            transactions_frame,
            text=transaction_status,
            font=("Arial", 10, "bold"),
            bg="#13293D",
            fg="#4CCB3A",
        )
        status_label.place(x=430, y=transaction_y)
        transaction_y = transaction_y + 40
    # ---------------- QUICK STATISTICS ----------------
    quick_statistics_frame = Frame(
        main_frame, bg="#13293D", highlightbackground="#4A6075", highlightthickness=1
    )
    quick_statistics_frame.place(x=70, y=690, width=1180, height=190)
    quick_statistics_title = Label(
        quick_statistics_frame,
        text="📊 Quick Statistics",
        font=("Arial", 18, "bold"),
        bg="#13293D",
        fg="white",
    )
    quick_statistics_title.place(x=20, y=20)
    membership_stat = Label(
        quick_statistics_frame,
        text=str(membership_count),
        font=("Arial", 24, "bold"),
        bg="#13293D",
        fg="#4CCB3A",
    )
    membership_stat.place(x=130, y=80)
    membership_stat_text = Label(
        quick_statistics_frame,
        text="Memberships",
        font=("Arial", 12),
        bg="#13293D",
        fg="white",
    )
    membership_stat_text.place(x=105, y=125)
    booking_stat = Label(
        quick_statistics_frame,
        text=str(booking_count),
        font=("Arial", 24, "bold"),
        bg="#13293D",
        fg="#4CCB3A",
    )
    booking_stat.place(x=420, y=80)
    booking_stat_text = Label(
        quick_statistics_frame,
        text="Facility Bookings",
        font=("Arial", 12),
        bg="#13293D",
        fg="white",
    )
    booking_stat_text.place(x=375, y=125)
    session_stat = Label(
        quick_statistics_frame,
        text=str(session_count),
        font=("Arial", 24, "bold"),
        bg="#13293D",
        fg="#4CCB3A",
    )
    session_stat.place(x=710, y=80)
    session_stat_text = Label(
        quick_statistics_frame,
        text="Training Sessions",
        font=("Arial", 12),
        bg="#13293D",
        fg="white",
    )
    session_stat_text.place(x=660, y=125)
    completed_stat = Label(
        quick_statistics_frame,
        text=str(completed_transaction_count),
        font=("Arial", 24, "bold"),
        bg="#13293D",
        fg="#4CCB3A",
    )
    completed_stat.place(x=1000, y=80)
    completed_stat_text = Label(
        quick_statistics_frame,
        text="Completed Payments",
        font=("Arial", 12),
        bg="#13293D",
        fg="white",
    )
    completed_stat_text.place(x=935, y=125)

    window.mainloop()


if __name__ == "__main__":
    dashboard()
