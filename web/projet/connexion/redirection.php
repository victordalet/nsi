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
	for($i = 0; $i < $total; $i++) {
		$id = explode("&$&", $fichier[$i], 2);
		if ($id[0] == $_POST["email"])
		{
			if ($id[1] == $_POST["mdp"])
			{
				setcookie("connecter", true, time()+1000000000)
				header('Location: http://localhost/projet');
			}
		}
		
    // On affiche ligne par ligne le contenu du fichier
    // avec la fonction nl2br pour ajouter les sauts de lignes
    //echo nl2br($fichier[$i]);
    }
	?>

	</body>
</html>