<?php
require "conse.php";
date('Y/m/d', strtotime("-1 days"));
$mysql_qry = "select * from Defaulters where Paid='0'";
$result = mysqli_query($con, $mysql_qry);
$response = array();
while ($row = mysqli_fetch_array($result)) {
    array_push($response, array(
        "noplate" => $row[0],
        "fault" => $row[1],
        "place" => $row[2],
        "fine" => $row[4],
        "mobile" => $row[5],
        "mail" => $row[6],
        "owner" => $row[7],
        "dati" => $row[8],
        "id" => $row[9]
    ));
}
echo json_encode(array(
    "server_respone" => $response
));
/*
 * if(mysqli_num_rows($result)>0)
 * {
 * echo "valid";
 * }
 * else
 * {
 * echo "invalid";
 * }
 */
mysqli_close($con);
?>
