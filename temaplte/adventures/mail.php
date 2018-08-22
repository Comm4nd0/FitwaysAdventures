<?php
$f_name = $_POST['f_name'];
$l_name = $_POST['l_name'];
$email = $_POST['email'];
$number = $_POST['number'];
$message = $_POST['message'];
$formcontent=" From: $f_name"." "."$l_name \n email: $email \n Message: $message";
$recipient = "admin@themepure.net";
$subject = "Add Your Subject Here";
$mailheader = "From: $email \r\n";
mail($recipient, $subject, $formcontent, $mailheader) or die("Error!");
header("location: thank-you.html"); 
?>