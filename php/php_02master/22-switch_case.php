<?php
$option = $_GET["option"];

// o switch case executa os bloco no qual a condição é atendida e todos os anteriores também
switch($option){
	case "1":
		echo "you chose option 1<br>";
		break;	// use o break ou o return se você está trabalhando com funções
	case "2":
		echo "you chose option 2<br>";
		break;
	default:
		echo "option not found<br>";
}

?>
