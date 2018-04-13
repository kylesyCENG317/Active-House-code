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

$sql = "SELECT * FROM Rooms WHERE user_id='2'";
$result = $conn->query($sql);

$response = array();
if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        array_push($response, array("room_id"=>$row['room_id'], "RMS_level"=>$row['RMS_level'], "Power"=>$row['Power'], "Gas"=>$row['Gas'], "Light"=>$row['Light'], "Temp"=>$row['Temp'], "Humid"=>$row['Humid'], "Lqd_Qntty"=>$row['Lqd_Qntty'], "Flow_Rate"=>$row['Flow_Rate'], "Lqd_Out"=>$row['Lqd_Out']));
    }
	echo json_encode(array("ser_response"=>$response));
} else {
    array_push($response, array());
echo json_encode(array("ser_response"=>$response));
}
$conn->close();
?>	