<?
header('Content-Type: text/html; charset=utf-8');
// o php usa a mesma ordem de operação que a matemática

$a = 7;
$b = 13;
$c = 2;

echo $a + $b * $c;
echo "<br>";
echo $a / $c * 10;
echo "<br>";
echo $a . $c . "<br>";   // concatenação que gera string

$tipo = gettype($a);    // pega o tipo da variável
echo "$a é do tipo $tipo <br>";

// php é fracamente tipado e permite alteração automática de string para inteiro como demonstrado abaixo:
$teste = "5" * 12;
echo $teste . "<br>";
echo gettype($teste) . "<br>";

// operador de módulo mostra apenas o resto da divisão
$mod = 10 % 3;
echo "10 % 3 = $mod <br>";

// exponenciação não funciona no php5
$pot1 = 3;
// $pot2 = $pot1 ** 3;
// echo "3 ** 3 = " . $pot2;
echo $pot1 * $pot1;
?>