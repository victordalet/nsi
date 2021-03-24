<!doctype HTML>
<html lang="fr">
	<head>
		<title> redirection </title>
	</head>
	<body>
	<?php
	
	$id = $_POST["identifiant"];
	$email = $_POST["email"];
	$mdp = $_POST["mdp"];
	$id = (int)$id;

	$data = file_get_contents("liste_identifiant.json");

	$obj = json_decode($data);
	$prenom = $obj[$id]->prenom;
	$nom = $obj[$id]->nom;
	define('PREFIX_SALT', 'ecole');
    define('SUFFIX_SALT', 'dfkrengjt');
    $hash = md5(PREFIX_SALT.$mdp.SUFFIX_SALT);

	print($obj[$id]->nom);
	if ($email == $obj[$id]->email && $hash == $obj[$id]->mdp)
	{
		echo " 
   		<h3> Bonjour ".$obj[$id]->prenom."</h3>
		<div>vous ètes desormais connecter</div>
		<a href='index.php' ><input type = 'button' value = 'retour'></a>";
		setcookie("nom",$prenom." ".$nom,time()+360000000,"/");
	    setcookie("connecter",$id,time()+5416415516,"/");
	    header('Location: http://localhost/projet/');
	}
	else
	{
		header('Location: http://localhost/projet/connexion/connexion.php' );
	}
	?>

	</body>
</html>