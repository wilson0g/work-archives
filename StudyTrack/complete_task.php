<?php

include "db.php";

$id = $_GET["id"];

$sql = "UPDATE tasks SET status='Completed' WHERE id=$id";

$conn->query($sql);

header("Location: index.php");
exit();

?>