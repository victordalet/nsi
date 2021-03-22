<?php
$fichier = file("liste_identifiant.txt");
$total = count($fichier)
?>
<!doctype HTML>
<html lang="fr">
	<head>
		<title> redirection </title>
	</head>
	<body>
	<?php
	$choix = $_POST["type"];
	$nom = $_POST["email"];
	$mdp = $_POST["mdp"];
	$source = $POST["image"];
	if ($source == "")
	{
		$source == "../images/profilebase.png";
	}
	if ($choix == "inscription")
	{   
	    $id_utilisateur = $id +1;
		$s = (id_utilisateur($save,$source));
		file_put_contents('saves.json', json_encode($s));
		setcookie("connecter", $_POST["email"],$_POST["mdp"], time()+1000000000);
		setcookie("photo",$source, time()+1000000000);
		header('Location: http://localhost/projet');	
		// envoie de mail
		ini_set( 'display_errors', 1 );
	    error_reporting( E_ALL );
	    $from = "stephane.dalet.sd@gmail.Com";
	    $subject = "Bienvenue";
	    $message = "Merci de vous êtes inscrit.";
	    $headers = "De :" . $from;
	    mail($nom,$subject,$message, $headers);
	    echo "Un mail vous à été envoyé.";	
	    //
	}
	else	
	{
		$liste = file_get_contents('saves.json');
		foreach( $liste as $value )
		{
            if( $value == $nom && $mdp )
			{ // rajouter la liste pour retrouver l'id
				setcookie("connecter", $nom, time()+1000000000);
				setcookie("photo",$source, time()+1000000000);
				header('Location: http://localhost/projet');
			}
			else
			{
				header('Location: http://localhost/projet/connexion/connexion.php');
			}
		}	
	}
	?>

	</body>
</html>