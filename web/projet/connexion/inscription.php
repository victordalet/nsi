<!doctype HTML>
<html lang="fr">
	<head>
		<title> connexion </title>
		<link rel="stylesheet" href="../css/connexion.css"/>
		<script type="text/javascript" src="/"></script>
		<link rel="icon" type="image/png" href="../images/logo.png" /> <!-- logo à coté du titre-->
	</head>
	<body>
	<section id="insrciption">
	<h1> inscrivez vous ! </h1>
	<form method = "POST" action = "redirection.php">
	<input  name = "nom" placeholder = "nom">
	<input  name = "email" placeholder = "email">
	<input  name = "image" placeholder = "url d'un photo de profile">
	<input type = "password" name = "mdp" placeholder = "mot de passe">
	<input type="submit" id="bouton" name ="type" value = "inscription" > <br>
	<a href="http://localhost/projet/connexion/connexion.php"><input type="button" id="autre" value="se connecter"></a>
	</form>
	</section>
	</body>
</html>