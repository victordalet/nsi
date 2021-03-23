<!doctype HTML>
<html lang="fr">
	<head>
		<title> Inscription </title>
		<link rel="stylesheet" href="../css/style.css"/>
		<script type="text/javascript" src="/"></script>
		<link rel="icon" type="image/png" href="../images/logo.png" /> <!-- logo à coté du titre-->
	</head>
	<body>
		<h1> Inscrivez vous ! </h1>
		<br><br><br><br><br><br>
		<section ><br><br><br><br>
		<form method = "POST" action = "redirection_inscription.php">
			<input class="formulaire" type = "textarea" name = "email" placeholder = "email">
			<br/>
			<input class="formulaire" type = "password" name = "mdp" placeholder = "mot de passe">
			<br/>
			<input class="formulaire" type="textarea" name="nom" placeholder="nom">
			<br/>
			<input class="formulaire" type="textarea" name="prenom" placeholder="prénom">
			<br/>
			<input class="login" type="submit" name ="type" value = "Inscription" ><br>
			<a href="http://localhost/projet/connexion/connexion.php"><input type="button" class="bouton" value="Se Connecter">
		</form>
		</section>
	</body>
</html>