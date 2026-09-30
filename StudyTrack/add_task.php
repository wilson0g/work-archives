<?php

include "db.php";
$task = $_POST["task"];
$course = $_POST["course"];
$stmt = $conn->prepare("INSERT INTO tasks (task, course) VALUES (?, ?)");
$stmt->bind_param("ss", $task, $course);
$stmt->execute();
header("Location: index.php");
exit();

?>