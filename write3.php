<?php
$servername = "localhost";
$username = "u530593372_activ";
$password = "kylesy";
$dbname = "u530593372_activ";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$room_id = $_POST['rid'];
if($room_id == -1){
	$sql = "INSERT INTO Rooms (RMS_level, Power, Gas, Light, Temp, Humid, Lqd_Qntty, Flow_Rate, Lqd_Out, user_id)
	VALUES ('".$_POST['rms']."', '".$_POST['power']."', '".$_POST['gas']."', '".$_POST['light']."', '".$_POST['temp']."', '".$_POST['humid']."', '".$_POST['lqd_q']."', '".$_POST['flow']."', '".$_POST['lqd_o']."', '".$_POST['user_id']."')";

	if ($conn->query($sql) == TRUE) {
		echo "New record created successfully";
	} else {
		echo "Error: " . $sql . "<br>" . $conn->error;
	}
}else{
	$sql = "UPDATE Rooms SET RMS_level = '".$_POST['rms']."', Power= '".$_POST['power']."', gas= '".$_POST['gas']."', Light= '".$_POST['light']."', Temp= '".$_POST['temp']."', Humid= '".$_POST['humid']."', Lqd_Qntty= '".$_POST['lqd_q']."', Flow_Rate= '".$_POST['flow']."', Lqd_Out= '".$_POST['lqd_o']."', user_id= '".$_POST['user_id']."' WHERE room_id = '".$room_id."'";

	if ($conn->query($sql) == TRUE) {
		echo "Updated record successfully";
	} else {
		echo "Error: " . $sql . "<br>" . $conn->error;
	}
}

$conn->close();
?>			