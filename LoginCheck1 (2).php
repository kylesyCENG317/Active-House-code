<?php



require_once 'connection1.php';
header('Content-Type: application/json ');

	

	class User {

		

		private $db;

		private $connection;

		

		function __construct() {

			$this -> db = new DB_Connection();

			$this -> connection = $this->db->getConnection();

		}

		

		public function does_user_exist($username,$password)
		{

			$query = "Select * from USERS where username='$username' and password = '$password' ";
			$result = mysqli_query($this->connection, $query);

           /* $query1 = "Select * from user where username='$username'";
			$result1 = mysqli_query($this->connection, $query1);*/
			if(mysqli_num_rows($result)>0){
				
				while($row = $result->fetch_assoc()){
				
			    //$json['name1'] = 'hello '.$row["name"];  
				$json['success'] = 'Welcome '.$username;
				$json['content1'] = $row["content"];
		    	$json['userid1'] = $row["user_id"];
		    	$json['RMS_Level1'] = $row["RMS_Level"];
				}

				
				
				

				

			}else{
					$json['error'] = 'Invalid Username or Password';
					
			}

				echo json_encode($json);
				mysqli_close($this->connection);

		}

		
	}
	
	$user = new User();
	if(isset($_POST['username'], $_POST['password'])){
		$username = $_POST['username'];
		$password = $_POST['password'];
		
		if(!empty($username) && !empty($password)){
			$encrypted_password = md5($password);
			$user -> does_user_exist($username, $password);
		} else{
			echo json_encode(" you must fill both fields");
			
		}
	}

?>