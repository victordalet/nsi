<!doctype HTML>
<html lang="fr">
	<head>
		<title> redirection </title>
		<link rel="stylesheet" href="../css/style.css"> <!-- on imparte le css -->
		<script src="../js/404.js"></script> <!-- on import le js -->
		<link rel="icon" type="image/png" href="../images/logo.png" /> <!-- logo à coté du titre-->
	</head>
	<body>
	<div class="centre"><input type="button" id="acceuil" value="Revenir à la page d'accueil" onclick="redirection();"></div>
	<?php
	$email = $_POST["email"];
	$mdp = $_POST["mdp"];
	$nom = $_POST["nom"];
	$prenom = $_POST["prenom"];
	
	$json = file_get_contents("liste_identifiant.json");
	//echo $json;
	$obj_json = json_decode($json);
	define('PREFIX_SALT', 'ecole');
    define('SUFFIX_SALT', 'dfkrengjt');
    $hash = md5(PREFIX_SALT.$mdp.SUFFIX_SALT);
	//echo $obj_json;
	$obj_json[]=['email' => $email,'mdp' =>  $hash, 'prenom' => $prenom,'nom'=>$nom];
	//echo $obj_json;
	$id = (sizeof($obj_json)-1);
	echo '<h6>votre identifiant est : '.$id.'</h6>';
	$data = json_encode($obj_json);
	$fichier = file_put_contents("liste_identifiant.json", $data);
    // envoie de mail
	ini_set( 'display_errors', 1 );
	error_reporting( E_ALL );
	setcookie("nom",$prenom." ".$nom,time()+360000000,"/");
	setcookie("connecter",$id,time()+5416415516,"/");
	
	?>
	</body>
</html>