<?
header('Content-Type: text/html; charset=utf-8');
// é possível criar variáveis de variáveis
$x = "teste";
$$x = 5;

echo $x. "<br>";
echo $teste. "<br>";

// variáveis por referência possuem o mesmo endereço de memória e sofrem as mesmas alterações
$a = 2;
$b =& $a;
echo "as variáveis a e b estão ligadas por referência $a = $b";
?>