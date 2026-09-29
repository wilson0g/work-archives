from tkinter import *
from tkinter import messagebox
import hashlib

from progenFCdatabase import database_connection
import user_session


def login():
    username = boxbelowusername.get()
    password = boxbelowpassword.get()

    if username == "" or password == "":
        messagebox.showerror("Login Error", "Please enter username and password")
        return

    connection = database_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT userID, username, passwordHash, userRole, athleteID, coachID FROM UserAccount WHERE username = %s",
        (username,),
    )

    user = cursor.fetchone()
    cursor.close()
    connection.close()
    if user is None:
        messagebox.showerror("Login Error", "Username or password is incorrect")
        return
    stored_password_hash = user[2]
    entered_password_hash = hashlib.sha256(password.encode()).hexdigest()
    if entered_password_hash == stored_password_hash:
        user_session.current_user_id = user[0]
        user_session.current_username = user[1]
        user_session.current_role = user[3]
        user_session.current_athlete_id = user[4]
        user_session.current_coach_id = user[5]
        messagebox.showinfo("Login Successful", "Welcome " + username)
        from ProgenFC_modules.ProgenFCdashboard import dashboard

        window.destroy()
        dashboard()
    else:
        messagebox.showerror("Login Error", "Username or password is incorrect")


window = Tk()
window.geometry("1536x1024")
window.title("Progen FC Sports Club Management System")
icon = PhotoImage(file="ProgenFC database logo copy.png")
window.iconphoto(True, icon)
window.config(background="#071A2F")
background_frame = Frame(window, bg="#071A2F")
background_frame.place(x=0, y=0, relwidth=1, relheight=1)
frame = Frame(
    window, background="#0B2138", highlightbackground="#49647C", highlightthickness=1
)
frame.place(relx=0.5, rely=0.5, anchor="center", width=630, height=760)
Photo = PhotoImage(file="ProgenFC_small_150.png")
logo = Label(frame, image=Photo, background="#0B2138")

logo.place(x=315, y=105, anchor="center")
welcome_label = Label(
    frame,
    text="Welcome Back to",
    font=("Arial", 28, "bold"),
    background="#0B2138",
    fg="white",
)
welcome_label.place(x=110, y=205)
progen_label = Label(
    frame,
    text="Progen FC",
    font=("Arial", 28, "bold"),
    background="#0B2138",
    fg="#4CCB3A",
)
progen_label.place(x=380, y=205)
subtitle = Label(
    frame,
    text="Sports Club Management System",
    font=("Arial", 14),
    background="#0B2138",
    fg="#B9C5CF",
)
subtitle.place(
    x=195,
    y=255,
)
left_line = Frame(
    frame,
    bg="#49647C",
)
left_line.place(
    x=60,
    y=265,
    width=120,
    height=1,
)
right_line = Frame(
    frame,
    bg="#49647C",
)
right_line.place(
    x=450,
    y=265,
    width=120,
    height=1,
)
label1 = Label(
    frame,
    text="Username",
    font=("Arial", 13, "bold"),
    background="#0B2138",
    fg="white",
)
label1.place(
    x=65,
    y=320,
)
boxbelowusername = Entry(
    frame,
    font=("Arial", 15),
    bg="#081C31",
    fg="white",
    insertbackground="white",
    relief="solid",
    bd=1,
)
boxbelowusername.place(
    x=65,
    y=355,
    width=500,
    height=55,
)
label2 = Label(
    frame,
    text="Password",
    font=("Arial", 13, "bold"),
    background="#0B2138",
    fg="white",
)
label2.place(
    x=65,
    y=445,
)
boxbelowpassword = Entry(
    frame,
    font=("Arial", 15),
    bg="#081C31",
    fg="white",
    insertbackground="white",
    relief="solid",
    bd=1,
)
boxbelowpassword.config(show="*")
boxbelowpassword.place(
    x=65,
    y=480,
    width=500,
    height=55,
)
loginbutton = Button(
    frame,
    text="LOGIN",
    font=("Arial", 15, "bold"),
    bg="#4CCB3A",
    fg="#0B1F33",
    activebackground="#3DB42D",
    activeforeground="#0B1F33",
    relief="flat",
    cursor="hand2",
    command=login,
)
loginbutton.place(
    x=65,
    y=580,
    width=500,
    height=55,
)
footer_line = Frame(
    frame,
    bg="#49647C",
)

footer_line.place(
    x=65,
    y=675,
    width=500,
    height=1,
)
footer_text = Label(
    frame,
    text="Progen FC • Sports Club Management System",
    font=("Arial", 10),
    background="#0B2138",
    fg="#8FA0AE",
)
footer_text.place(
    x=185,
    y=700,
)
window.mainloop()
