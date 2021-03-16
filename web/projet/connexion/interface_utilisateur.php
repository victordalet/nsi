<!doctype HTML>
<html lang="fr">
      <head> 
	       <title> interface utilisateure </title> <!--le titre de la page -->
		   <link rel="stylesheet" href="../../css/style.css"> <!-- on imparte le css -->
		   <script src="js/jsindex.js"></script> <!-- on import le js -->
		   <link rel="icon" type="image/png" href="../../images/logo.png" /> <!-- logo à coté du titre-->
	  </head>
	  <body>
	 <?php 
            if (isset($_COOKIE["connecter"]))
            {
                print("le cookie");
            }
        ?>
	  </body>
</html>	  	