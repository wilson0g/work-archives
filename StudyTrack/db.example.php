<?php

$host = "localhost";
$user = "your database username";
$password = "your database password";
$database = "your database name";

$conn = new mysqli($host, $user, $password, $database);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

?>