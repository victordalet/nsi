<!doctype HTML>
<html lang="fr">
	<head>
	    <title> messagerie </title>
		<link rel="stylesheet" href="../css/style.css"/>
		<script type="text/javascript" src="../js/message.js"></script>
		<link rel="icon" type="image/png" href="../images/logo.png" /> <!-- logo à coté du titre-->
		 <?php 
		
		    // $delai = 100; 
			// $url = 'http://192.167.1.209/dalet/projet/messagerie/messagerie.php';
			// header("Refresh: $delai;url=$url");
	    // ?>
	</head>
	 <body onkeydown="  envoieTouche(event);">

	    <h1><a href="http://localhost/projet"><img alt="logo" id="logocontacte" src="../images/logo.png"></a> Contacte :  </h1>
	    <br><br><br><br><br>
	<div id="messageriecadre">
		<section style="overflow-y:scroll;">
        <?php
		if (isset($_COOKIE["connecter"]))
		{
		$text = file_get_contents('messagerie.json');
		echo $text; 
		}
		else
		{
			header('Location: http://localhost/projet/connexion.php');
		}
		?>
	</section>
		<form method = "POST" id="envoie" action = "envoie.php">
		     <br><textarea id="message" name="message" placeholder="écriver votre message"></textarea> <br>
			 <button id="send" type="submit"><img alt="envoie" src="../images/send.png"></button>
		</form>	 
			 
		</div>
	</body>
</html>	