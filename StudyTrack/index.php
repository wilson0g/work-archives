<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>StudyTrack</title>
    <link rel="stylesheet" href="style.css?v=2">
</head>

<body>

    <div class="container">
        <h1>StudyTrack</h1>
        <p>Keep track of your study tasks</p>

        <form action="add_task.php" method="POST" id="taskForm">
            <input type="text" name="task" placeholder="Enter a task" required>
            <input type="text" name="course" placeholder="Enter course" required>
            <button type="submit">Add Task</button>
        </form>

        <h2>My Tasks</h2>

        <?php
        include "db.php";

        $result = $conn->query("SELECT * FROM tasks ORDER BY id DESC");
        if ($result->num_rows > 0) {
            while ($row = $result->fetch_assoc()) {
                echo "<div class='task-item'>";

                echo "<div class='task-info'>";
                echo "<strong>" . htmlspecialchars($row["task"]) . "</strong>";
                echo "<span>" . htmlspecialchars($row["course"]) . "</span>";
                echo "</div>";

                echo "<div class='task-actions'>";

                if ($row["status"] == "pending") {
                    echo "<span class='status pending'>Pending</span>";
                    echo "<a class='complete-btn' href='complete_task.php?id=" . $row["id"] . "'>✓ Complete</a>";
                } else {
                    echo "<span class='status completed'>✓ Completed</span>";
                }
                echo '<a class="delete-btn" href="delete_task.php?id=' . $row["id"] . '">Delete</a>';
                echo "</div>";
                echo "</div>";

                
            }
        } else {
            echo "<p>No tasks yet.</p>";
        }
        ?>

    </div>

    <script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
    <script src="script.js"></script>

</body>
</html>