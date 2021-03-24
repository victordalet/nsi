<!doctype HTML>
<html lang="fr">
	<head>
		<title> connexion </title>
		<link rel="stylesheet" href="../css/style.css"/>
		<script type="text/javascript" src="/"></script>
		<link rel="icon" type="image/png" href="../images/logo.png" /> <!-- logo à coté du titre-->
	</head>
	<body>
			<h1> <a href="http://localhost/projet"><img alt="logo" class="logoindex" src="../images/acceuil.png"></a>Connectez vous ! </h1><br><br><br><br><br><br>
	<section>
	<form method = "POST" action = "redirection.php">
		<br><br><br><br>
		<input class="formulaire" type="textarea" name="identifiant" placeholder="identifiant"><br>
		
		<input class="formulaire" type = "textarea" name = "email" placeholder = "email"><br>

		<input class="formulaire" type = "password" name = "mdp" placeholder = "mot de passe"><br>

		<input class="login" type="submit" value = "connexion"><br>
		<a href="http://localhost/projet/connexion/inscription.php"><input type="button" class="bouton" value="créer un compte">
	</form>
	</section>
	</body>
</html>