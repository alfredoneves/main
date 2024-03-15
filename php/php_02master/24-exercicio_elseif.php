<?php 
header('Content-Type: text/html; charset=utf-8');

$velocidade = 10;

if($velocidade < 40){
        echo "assim é melhor ir andando ";
} elseif($velocidade <= 80){
        echo "assim está bom ";
} else{
        echo "a pressa é inimiga da perfeição ";
}

echo  "($velocidade km/h) <br>";

?>
