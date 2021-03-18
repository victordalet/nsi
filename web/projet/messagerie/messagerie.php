<!doctype HTML>
<html lang="fr">
	<head>
	    <title> messagerie </title>
		<link rel="stylesheet" href="../../css/style.css"/>
		<script type="text/javascript" src="../js/message.js"></script>
		<link rel="icon" type="image/png" href="../../images/logo.png" /> <!-- logo à coté du titre-->
		// <?php 
		
		    // $delai = 100; 
			// $url = 'http://192.167.1.209/dalet/projet/messagerie/messagerie.php';
			// header("Refresh: $delai;url=$url");
	    // ?>
	</head>
	<body>
	    <h1> contacte </h1>
	<div>
        <?php
		setcookie("connecter","victor",time()+360000000);
		if (isset($_COOKIE["connecter"]))
		{
		$text = file_get_contents('messagerie.json');
		echo $text;
		}
		else
		{
			header('Location: http://localhost/projet');
		}
		?>
		<form method = "POST" action = "envoie.php">	
		     <textarea id="message" name="message">ecrire votre message </textarea>
			 <input type="submit" value='envoyer'>
		</form>	 
			 
		</div>
	</body>
</html>	