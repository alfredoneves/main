<?php
// testando cast para inteiro de valores que não são inteiros

$a = 2.5;
$b = true;
$c = "teste";
$d = [1, 2, 3];

$na = (int) $a;
$nb = (int) $b;
$nc = (int) $c;
$nd = (int) $d;

echo "\$a = $a <br>";
echo "\$b = $b <br>";
echo "\$c = $c <br>";

$array2string = implode($d);    // converte um array para string
echo "\$d = $array2string <br>";

echo "\$na = $na <br>";
echo "\$nb = $nb <br>";
echo "\$nc = $nc <br>";
echo "\$nd = $nd <br>";
?>
