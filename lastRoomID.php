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

$sql = "SELECT room_id FROM Rooms WHERE user_id='".$_POST['uid']."' ORDER BY room_id DESC LIMIT 1";

$result = $conn->query($sql);

$response = array();
if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        array_push($response, array("room_id"=>$row['room_id']));
    }
	echo json_encode(array("ser_response"=>$response));
} else {
    array_push($response, array());
echo json_encode(array("ser_response"=>$response));
}
$conn->close();
?>