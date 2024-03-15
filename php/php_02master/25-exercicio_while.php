<?php
$meu_array = [1, 2, "a", "k", 9, true, "la", 12, "12", "m", 0, false, "ultimo"];

$tamanho = sizeof($meu_array);

$c = 0;

while($c < $tamanho){	// percorre o array
    if(is_string($meu_array[$c])){	// verificar se o valor é string para imprimir
        echo $meu_array[$c] . "<br>";
    }
    $c++;
}

?>
