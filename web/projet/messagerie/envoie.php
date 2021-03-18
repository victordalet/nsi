!doctype HTML>
<html lang="fr">
	<head>
	    <title> envoie </title>
		<link rel="stylesheet" href="../../css/style.css"/>
		<script type="text/javascript" src="../js/message.js"></script>
		<link rel="icon" type="image/png" href="../../images/logo.png" /> <!-- logo à coté du titre-->
	</head>
    <body>	
		<?php
		file_put_contents('messagerie.json', json_encode($_COOKIE["connecter"].$_POST["message"]));
		header('Location: http://192.167.1.209/dalet/projet/messagerie/messagerie.php');	
        ?>		
	</body>
</html>	