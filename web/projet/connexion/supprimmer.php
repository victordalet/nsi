<!doctype HTML>
<html lang="fr">
      <head> 
	       <title> suppression  </title> <!--le titre de la page -->
	  </head>
	        
	  <body>

	  	<?php
	  	  unset($_COOKIE['connecter']);
	  	  unset($_COOKIE['nom']);
	  	  header('Location: http://localhost/projet/' )
	  	?>  
	  </body>
</html>	  