<?php
$liga = mysqli_connect("localhost", "horus", "password", "test");	# connects the database

#gets the parameters
$username = $_GET['username'];	
$password = $_GET['password'];

# creates and executes the query
$sql = "select * from users where username='$username' and password='$password'";
$query = mysqli_query($liga, $sql);

# some validation
if (mysqli_num_rows($query) == 1){
	header("Location: admin.php");
} 
else {
	echo "Username or Password incorrect";
}

?>
