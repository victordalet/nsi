<!doctype HTML>
<html lang="fr">
      <head> 
	       <title> nsi </title> <!--le titre de la page -->
		   <link rel="stylesheet" href="css/404.css"> <!-- on imparte le css -->
		   <script src="js/404.js"></script> <!-- on import le js -->
		   <script src="js/4042.js"></script> <!-- on import le js -->
		   <link rel="icon" type="image/png" href="images/logo.png" /> <!-- logo à coté du titre-->
	  </head>
	  <body onkeydown="x,y,point = Touche(event,x,y,lancer,point);"> 
	  	    <h1>Erreur 404 cette page n'existe pas! </h1>
	  	    <div id="logo404"><input type="button" value="Revenir à la page d'accueil" onclick="redirection();"> <br>
	  	    <img alt="404" src="images/404.png"><br></div>
	  	    <input type="button" value="jouer" id="boutonjouer" onclick="lancer = play(lancer);"><br>
	  	    <div id="jeu">
	  	    	<input type="button" id="afficherpoint" value="point : 0"> 
	  	    	<img alt="ennemie" src="images/ennemie.gif" id="ennemie">
	  	    	<img alt="piece1" src="images/piece.png" id="piece">  <br><br>
	  	    	<img alt="personnage" src="images/perso.gif" id="perso"> 
	  	    	
	            
	  	    </div>
	  </body>
</html>	  