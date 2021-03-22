<!doctype HTML>
<html lang="fr">
	<head>
		<title> connexion </title>
		<link rel="stylesheet" href="../css/connexion.css"/>
		<script type="text/javascript" src="/"></script>
		<link rel="icon" type="image/png" href="../images/logo.png" /> <!-- logo à coté du titre-->
	</head>
	<div>
	<div id="cadre">
	<h1> connectez vous </h1>
	<form method = "POST" action = "redirection.php">
	<label for="mail"><img alt="logo mail" src="../images/mail.png"></label>
	<input id="mail" type = "textarea" name = "email" placeholder = "email"> <br>
	<label for="mdp"><img alt="logo mail" src="../images/mail.png"></label>
	<input id="mdp" type = "password" name = "mdp" placeholder = "mot de passebr"> <br><br>
	<input type="submit" id="bouton" value = "connexion"><br><br>
	<a href="http://localhost/projet/connexion/inscription.php"><input type="button" id="autre" value="s'inscrire"></a>
	</form>
    </div>
    </div>
	</body>
</html>