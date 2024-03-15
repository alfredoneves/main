<?php
$meu_array = [];
$c = 10;

while($c <= 100){
    $meu_array[$c/10] = $c;
    $c += 10;
}

$c = 1;

while($c <= 10){
    if($meu_array[$c] == 30 || $meu_array[$c] == 40){
        $c++;
        continue;
    }

    echo $meu_array[$c] . "<br>";
    $c++;
}

?>
