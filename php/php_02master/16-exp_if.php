<?php
$nome = $_GET["nome"];
$idade = $_GET["idade"];
$rico = $_GET["rico"];

if($idade >= 18){
        echo "$nome pode beber e votar <br>";
} elseif($idade >=16){
        echo "$nome pode votar <br>";
} elseif($rico == "true"){      // tratando como string
        echo "$nome pode fazer o que quiser <br>";
} else {
        echo "você tem direito de ficar calado <br>";
}

?>
