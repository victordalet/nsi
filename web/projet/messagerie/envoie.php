<!doctype HTML>
<html lang="fr">
	<head>
	    <title> envoie </title>
		<link rel="stylesheet" href="../../css/style.css"/>
		<script type="text/javascript" src="../js/message.js"></script>
		<link rel="icon" type="image/png" href="../../images/logo.png" /> <!-- logo à coté du titre-->
	</head>
    <body>	
		<?php
		$document = fopen("messagerie.json","c+");
		fseek($document, filesize('messagerie.json'));
		fwrite($document, $_COOKIE["connecter"].": ".$_POST["message"]."<br>"."\n" );
		header('Location: http://localhost/projet/messagerie/messagerie.php');	
        ?>		
        
	</body>
</html>	