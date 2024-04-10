<?php
// include code, show array and uses html and php
include_once "phtml2.php"

?>

<h1> Seja Bem-vindo </h1>
<p><?= $nome; ?>, veja nossas ofertas:</p>
<ul>
	<?php foreach($produtos as $produto): ?>
		<li><?= $produto; ?></li>
	<?php endforeach; ?>
</ul>
