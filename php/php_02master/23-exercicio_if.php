<?php
$var1 = 50;

if(is_int($var1) || is_float($var1)){
        $var2 = 2 * $var1;

        if($var2 > 100){
                echo "$var2 > 100 <br>";
        } else {
                echo "$var2 <= 100 <br>";
        }
}

?>
