<?php
//$arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20];
$arr = [];

for($i=1; $i<21; $i++){
    array_push($arr, $i);
}

print_r($arr);
echo "<br> pares: <br>";

for($i=0; $i<count($arr); $i++){
    if($arr[$i] % 2 == 0){
        echo $arr[$i] . "<br>";
    }
    
}

?>
