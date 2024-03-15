<?php
$fp = fopen("http://localhost/ola.php", "r");   // reads an online page

if($fp){
    while(!feof($fp)){  // the condition is the end of the file, use this for efeciency
        echo fgets($fp);
    }
} else {
    echo "failed to oppen the file <br>";
}

fclose($fp);	// remember to close the file

?>
