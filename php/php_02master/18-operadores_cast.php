<?php
// operadores de cast convertem valores para outros tipos
// int, bool, float, string, array, object e unset
$a = "20";
echo "a = $a <br>";
$ta = gettype($a);
echo "type(a) = $ta <br>";

$b = (int) $a;	// converte o valor para inteiro
echo '$b = (int) $a <br>';
$tb = gettype($b);
echo "type(b) = $tb <br>";

?>
