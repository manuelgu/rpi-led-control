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
		<br>
		<input type="submit" value="yellow" name="color" style="color:yellow">
		<br>
		<input type="submit" value="green" name="color" style="color:green">
		<br>
		<input type="submit" value="stop" name="color" style="color:black">
	</form>
</body>
</html>
