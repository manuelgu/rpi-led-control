<?php

$file = 'color.txt';

$current = file_get_contents($file);

if (isset($_GET['color'])) {
	$current = $_GET['color'];
}

file_put_contents($file, $current);

?>



<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>RPi LED Control</title>
	<style>
	input {
        width: 490px;
        height: 210px;
        font-size: 9em;
	}
	</style>
</head>
<body>
	<form action="index.php" method="GET" name="ledform">
		<input type="submit" value="red" name="color" style="color:red">
		<br><br>
		<input type="submit" value="blue" name="color" style="color:blue">
		<br><br>
		<input type="submit" value="green" name="color" style="color:green">
	</form>
</body>
</html>
