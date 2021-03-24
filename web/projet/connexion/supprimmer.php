<!doctype HTML>
<html lang="fr">
      <head> 
	       <title> suppression  </title> <!--le titre de la page -->
	  </head>
	        
	  <body>

	  	<?php
	  	if (isset($_COOKIE["connecter"]))
        {
		setcookie("nom","",time()-3600,"/");
	    setcookie("connecter","",time()-5416,"/");
	  	header('Location: http://localhost/projet/' );
	    }
	    else{
	    	print("bug");
	    }
	  	?>  
	  </body>
</html>	  