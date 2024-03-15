<?php
$fp = fopen("write.txt", "a+");	// I prefer to use a+ because w erases the content of the file before writing to it
$ret = fwrite($fp, "some string \n");

if($ret){
        echo "ok";
} else{
        echo "fail";
}

fclose($fp);
?>
