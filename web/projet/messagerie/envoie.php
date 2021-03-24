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
		$date = date("(d.m.y ; H:i) : "); //la date de l'envoie du message
		$document = fopen("messagerie.json","c+"); // on ouvre le fichier 
		fseek($document, filesize('messagerie.json'));
		fwrite($document, '<span class="nom">'.$_COOKIE["nom"].'</span>'.'<span class="date">'.$date.'</span>'.$_POST["message"]."<br>"."\n" ); // on ajoute dans le json la personne la date suivit de son message
		header('Location: http://localhost/projet/messagerie/messagerie.php'); // on redirige vers la messagerie
        ?>		
        
	</body>
</html>	