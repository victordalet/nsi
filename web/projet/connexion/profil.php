<!doctype HTML>
<html lang="fr">
      <head> 
	       <title> projet ecole  </title> <!--le titre de la page -->
		   <link rel="stylesheet" href="css/style.css"> <!-- on imparte le css -->
		   <script src="../js/jsindex.js"></script> <!-- on import le js -->
		   <link rel="icon" type="image/png" href="images/logo.png" /> <!-- logo à coté du titre-->
	  </head>
	        <div> 
			     <?php
                     echo '
					 <img alt="profil" href=" $_COOKIE["photo"]"> <br>
					 $_COOKIE["connecter"] <br>
					 <input type="button" value="changer image">
					  <input type="button" value="changer nom "onclick="nom();"> <br>
					  <input id="nom" value="$_COOKIE["connecter"]">
					  <input id="image" value="$_COOKIE["photo"]">
					  <input type="submit" value="envoyer" onclick="envoie();">
					 ';
				 ?>
			</div>
	  <body>
	  </body>
</html>	  