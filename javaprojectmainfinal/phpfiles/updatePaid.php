<?php
require "conse.php";
$id = ($_POST["id"]);

$mysql_qry = "update Defaulters set Paid='1' where id='$id'";

$result = mysqli_query($con, $mysql_qry);
$response = array();

if (mysqli_num_rows($result) > 0) {
    // echo "Valid";
} else {
    // echo "invalid";
}

mysqli_close($con);
?>

