<?
header('Content-Type: text/html; charset=utf-8');

// números inteiros
echo "1 + 2 = ".(1+2). "<br>";  // concatenação

$var0 = 4;
$result0 = is_int($var0);

if($result0){
    echo "$var0 = inteiro<br>";
}

// float
$var1 = 4.0;    // 4.0 é float, mas na hora de imprimir o 0 é ignorado
$result1 = is_float($var1);

if($result1){
    echo "$var1 = float<br>";
}

echo "var0 + var1 = $var0 + $var1 = ". ($var0 + $var1). "<br>";

// string
$idade = "15";  // se está entre aspas é string (chora javascript)
echo "eu tenho $idade anos <br>";    // string interpretada
echo 'eu tenho $idade anos <br>';    // string literal

if(!is_string($idade)){ // ! = negação
    echo "$idade não é uma string <br>";
}else{
    echo "$idade é uma string <br>";
}

//boolean
$idade = 22;

if($idade >= 18){
    $maior = true;
}

if(0 == false AND is_bool($maior)){
    echo "0 é considerado falso e \$maior é booleano <br>";
}

?>