# StudyTrack

StudyTrack is a simple web-based task management application designed to help students organize their academic tasks by course.

Users can:
- Add a new task
- Assign the task to a course
- View their tasks
- Mark tasks as completed
- Delete tasks
## Technologies Used

- HTML
- CSS
- JavaScript
- jQuery
- PHP
- MySQL
## Running StudyTrack Locally

### 1. Download the Project

Clone this repository or download it as a ZIP file and extract it on your computer.

### 2. Set Up MySQL

Create a new MySQL database for StudyTrack.

Import the included `database.sql` file into the database. This will create the `tasks` table required by the application.

### 3. Configure the Database Connection

Make a copy of `db.example.php` and rename the copy to:

`db.php`

Open `db.php` and replace the example values with your own MySQL database credentials.

### 4. Run the Application

Place the project in the document root of a local PHP server such as AMPPS, XAMPP, or MAMP.

Start Apache and MySQL, then open StudyTrack through localhost in your browser.