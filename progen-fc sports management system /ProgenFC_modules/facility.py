from tkinter import *
from tkinter import ttk

from progenFCdatabase import database_connection


def facility():
    def search_booking():
        search_value = search_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT booking.bookingID, booking.facilityID, facility.facilityName, facility.facilityType, "
            "facility.facilityCapacity, booking.teamID, team.teamName, booking.bookingDate, "
            "booking.bookingStart, booking.bookingEnd, booking.bookingReason "
            "FROM booking "
            "JOIN facility ON booking.facilityID = facility.facilityID "
            "JOIN team ON booking.teamID = team.teamID "
            "WHERE booking.bookingID LIKE %s OR booking.facilityID LIKE %s "
            "OR facility.facilityName LIKE %s OR facility.facilityType LIKE %s "
            "OR booking.teamID LIKE %s OR team.teamName LIKE %s "
            "OR booking.bookingDate LIKE %s OR booking.bookingReason LIKE %s",
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

        for row in booking_table.get_children():
            booking_table.delete(row)

        for record in records:
            booking_table.insert("", END, values=record)

        connection.close()

    def load_bookings():
        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT booking.bookingID, booking.facilityID, facility.facilityName, facility.facilityType, "
            "facility.facilityCapacity, booking.teamID, team.teamName, booking.bookingDate, "
            "booking.bookingStart, booking.bookingEnd, booking.bookingReason "
            "FROM booking "
            "JOIN facility ON booking.facilityID = facility.facilityID "
            "JOIN team ON booking.teamID = team.teamID"
        )

        records = cursor.fetchall()

        for row in booking_table.get_children():
            booking_table.delete(row)

        for record in records:
            booking_table.insert("", END, values=record)

        connection.close()

    def add_booking():
        booking_id = booking_id_entry.get()

        facility_id = facility_id_entry.get().split(" - ")[0]

        team_id = team_id_entry.get().split(" - ")[0]

        booking_date = booking_date_entry.get()
        booking_start = booking_start_entry.get()
        booking_end = booking_end_entry.get()
        booking_reason = booking_reason_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "INSERT INTO booking "
            "(bookingID, facilityID, teamID, bookingDate, bookingStart, bookingEnd, bookingReason) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (
                booking_id,
                facility_id,
                team_id,
                booking_date,
                booking_start,
                booking_end,
                booking_reason,
            ),
        )

        connection.commit()

        cursor.execute(
            "SELECT booking.bookingID, booking.facilityID, facility.facilityName, facility.facilityType, "
            "facility.facilityCapacity, booking.teamID, team.teamName, booking.bookingDate, "
            "booking.bookingStart, booking.bookingEnd, booking.bookingReason "
            "FROM booking "
            "JOIN facility ON booking.facilityID = facility.facilityID "
            "JOIN team ON booking.teamID = team.teamID "
            "WHERE booking.bookingID = %s",
            (booking_id,),
        )

        record = cursor.fetchone()

        connection.close()

        booking_table.insert("", END, values=record)

    def clear_booking():
        booking_id_entry.delete(0, END)
        facility_id_entry.delete(0, END)
        team_id_entry.delete(0, END)
        booking_date_entry.delete(0, END)
        booking_start_entry.delete(0, END)
        booking_end_entry.delete(0, END)
        booking_reason_entry.delete(0, END)

    def delete_booking():
        booking_id = booking_id_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "DELETE FROM booking WHERE bookingID = %s",
            (booking_id,),
        )

        connection.commit()
        connection.close()

        for row in booking_table.get_children():
            values = booking_table.item(row)["values"]

            if str(values[0]) == booking_id:
                booking_table.delete(row)
                break

    def update_booking():
        booking_id = booking_id_entry.get()

        facility_id = facility_id_entry.get().split(" - ")[0]

        team_id = team_id_entry.get().split(" - ")[0]

        booking_date = booking_date_entry.get()
        booking_start = booking_start_entry.get()
        booking_end = booking_end_entry.get()
        booking_reason = booking_reason_entry.get()

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "UPDATE booking SET facilityID = %s, teamID = %s, bookingDate = %s, "
            "bookingStart = %s, bookingEnd = %s, bookingReason = %s "
            "WHERE bookingID = %s",
            (
                facility_id,
                team_id,
                booking_date,
                booking_start,
                booking_end,
                booking_reason,
                booking_id,
            ),
        )

        connection.commit()

        cursor.execute(
            "SELECT booking.bookingID, booking.facilityID, facility.facilityName, facility.facilityType, "
            "facility.facilityCapacity, booking.teamID, team.teamName, booking.bookingDate, "
            "booking.bookingStart, booking.bookingEnd, booking.bookingReason "
            "FROM booking "
            "JOIN facility ON booking.facilityID = facility.facilityID "
            "JOIN team ON booking.teamID = team.teamID "
            "WHERE booking.bookingID = %s",
            (booking_id,),
        )

        record = cursor.fetchone()

        connection.close()

        for row in booking_table.get_children():
            values = booking_table.item(row)["values"]

            if str(values[0]) == booking_id:
                booking_table.item(row, values=record)
                break

    def view_sessions():
        facility_id = facility_id_entry.get().split(" - ")[0]

        connection = database_connection()
        cursor = connection.cursor()

        cursor.execute(
            "SELECT facilityName FROM facility WHERE facilityID = %s",
            (facility_id,),
        )

        facility_record = cursor.fetchone()

        facility_name = facility_record[0]

        cursor.execute(
            "SELECT sessionID, facilityID, sessionDate, sessionStart, sessionEnd, sessionFocus "
            "FROM session WHERE facilityID = %s",
            (facility_id,),
        )

        records = cursor.fetchall()

        connection.close()

        session_window = Toplevel(window)
        session_window.geometry("1200x600")
        session_window.title("Facility Sessions")
        session_window.config(background="#0B1F33")

        session_heading = Label(
            session_window,
            text="Sessions at " + facility_name,
            font=("Arial", 25, "bold"),
            bg="#0B1F33",
            fg="#4CCB3A",
        )

        session_heading.place(x=430, y=40)

        session_table = ttk.Treeview(
            session_window,
            columns=(
                "sessionID",
                "facilityID",
                "sessionDate",
                "sessionStart",
                "sessionEnd",
                "sessionFocus",
            ),
            show="headings",
        )

        session_table.heading("sessionID", text="Session ID")
        session_table.heading("facilityID", text="Facility ID")
        session_table.heading("sessionDate", text="Session Date")
        session_table.heading("sessionStart", text="Session Start")
        session_table.heading("sessionEnd", text="Session End")
        session_table.heading("sessionFocus", text="Session Focus")

        session_table.column("sessionID", width=130)
        session_table.column("facilityID", width=130)
        session_table.column("sessionDate", width=150)
        session_table.column("sessionStart", width=150)
        session_table.column("sessionEnd", width=150)
        session_table.column("sessionFocus", width=250)

        session_table.place(x=40, y=120, width=1120, height=400)

        for record in records:
            session_table.insert("", END, values=record)

    def go_to_dashboard():
        from ProgenFC_modules.ProgenFCdashboard import dashboard

        window.destroy()
        dashboard()

    window = Tk()
    window.geometry("1536x1024")
    window.title("Facility Booking Management")
    window.config(background="#0B1F33")

    heading = Label(
        window,
        text="Facility Booking Management",
        font=("Arial", 28, "bold"),
        bg="#0B1F33",
        fg="#4CCB3A",
    )

    heading.place(x=520, y=20)

    booking_id_label = Label(
        window,
        text="Booking ID:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    booking_id_label.place(x=170, y=80)

    booking_id_entry = Entry(window, font=("Arial", 14))

    booking_id_entry.place(x=370, y=75, width=300, height=35)

    facility_id_label = Label(
        window,
        text="Facility:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    facility_id_label.place(x=170, y=140)

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

    facility_id_entry.place(x=370, y=135, width=300, height=35)

    team_id_label = Label(
        window,
        text="Team:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    team_id_label.place(x=170, y=200)

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

    team_id_entry.place(x=370, y=195, width=300, height=35)

    booking_date_label = Label(
        window,
        text="Booking Date:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    booking_date_label.place(x=170, y=260)

    booking_date_entry = Entry(window, font=("Arial", 14))

    booking_date_entry.place(x=370, y=255, width=300, height=35)

    booking_start_label = Label(
        window,
        text="Booking Start:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    booking_start_label.place(x=170, y=320)

    booking_start_entry = Entry(window, font=("Arial", 14))

    booking_start_entry.place(x=370, y=315, width=300, height=35)

    booking_end_label = Label(
        window,
        text="Booking End:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    booking_end_label.place(x=170, y=380)

    booking_end_entry = Entry(window, font=("Arial", 14))

    booking_end_entry.place(x=370, y=375, width=300, height=35)

    booking_reason_label = Label(
        window,
        text="Booking Reason:",
        font=("Arial", 15, "bold"),
        bg="#0B1F33",
        fg="white",
    )

    booking_reason_label.place(x=170, y=440)

    booking_reason_entry = Entry(window, font=("Arial", 14))

    booking_reason_entry.place(x=370, y=435, width=300, height=35)

    add_button = Button(
        window,
        text=" ➕ Add",
        font=("Arial", 13, "bold"),
        command=add_booking,
    )

    add_button.place(x=170, y=505, width=120, height=40)

    update_button = Button(
        window,
        text="✏️ Update",
        font=("Arial", 13, "bold"),
        command=update_booking,
    )

    update_button.place(x=310, y=505, width=120, height=40)

    delete_button = Button(
        window,
        text=" 🗑️ Delete",
        font=("Arial", 13, "bold"),
        command=delete_booking,
    )

    delete_button.place(x=450, y=505, width=120, height=40)

    clear_button = Button(
        window,
        text=" ♻️ Clear",
        font=("Arial", 13, "bold"),
        command=clear_booking,
    )

    clear_button.place(x=590, y=505, width=120, height=40)

    view_sessions_button = Button(
        window,
        text="📅 View Sessions",
        font=("Arial", 13, "bold"),
        command=view_sessions,
    )

    view_sessions_button.place(x=730, y=505, width=150, height=40)

    search_entry = Entry(window, font=("Arial", 13))

    search_entry.place(x=200, y=593, width=940, height=35)

    search_button = Button(
        window,
        text="🔍    Search",
        font=("Arial", 13, "bold"),
        command=search_booking,
    )

    search_button.place(x=1160, y=593, width=120, height=35)

    booking_table = ttk.Treeview(
        window,
        columns=(
            "bookingID",
            "facilityID",
            "facilityName",
            "facilityType",
            "facilityCapacity",
            "teamID",
            "teamName",
            "bookingDate",
            "bookingStart",
            "bookingEnd",
            "bookingReason",
        ),
        show="headings",
    )

    booking_table.heading("bookingID", text="Booking ID")
    booking_table.heading("facilityID", text="Facility ID")
    booking_table.heading("facilityName", text="Facility Name")
    booking_table.heading("facilityType", text="Facility Type")
    booking_table.heading("facilityCapacity", text="Capacity")
    booking_table.heading("teamID", text="Team ID")
    booking_table.heading("teamName", text="Team Name")
    booking_table.heading("bookingDate", text="Booking Date")
    booking_table.heading("bookingStart", text="Start")
    booking_table.heading("bookingEnd", text="End")
    booking_table.heading("bookingReason", text="Booking Reason")

    booking_table.column("bookingID", width=100)
    booking_table.column("facilityID", width=100)
    booking_table.column("facilityName", width=180)
    booking_table.column("facilityType", width=150)
    booking_table.column("facilityCapacity", width=100)
    booking_table.column("teamID", width=100)
    booking_table.column("teamName", width=200)
    booking_table.column("bookingDate", width=120)
    booking_table.column("bookingStart", width=100)
    booking_table.column("bookingEnd", width=100)
    booking_table.column("bookingReason", width=200)

    booking_table.place(x=40, y=640, width=1400, height=300)

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

    load_bookings()

    window.mainloop()


if __name__ == "__main__":
    facility()
