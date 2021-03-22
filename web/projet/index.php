<!doctype HTML>
<html lang="fr">
      <head> 
	       <title> projet ecole  </title> <!--le titre de la page -->
		   <link rel="stylesheet" href="css/style.css"> <!-- on imparte le css -->
		   <script src="js/jsindex.js"></script> <!-- on import le js -->
		   <link rel="icon" type="image/png" href="images/logo.png" /> <!-- logo à coté du titre-->
	  </head>
	        
	  <body>
	  	    <h1 id="titre"><a href="http://localhost/projet"><img alt="logo" id="logoindex" src="images/logo.png"></a> NOTRE DAME DE LA PROVIDENCE
	  	     <?php 
            if (isset($_COOKIE["connecter"]))
            {
            	echo '<a href="http://localhost/projet/connexion/profil.php"><input type="button" value="bienvenue" ></a>';
            }
            else
            {
            	echo '<a href="http://localhost/projet/connexion/connexion.php"><input type="button" class="inscription" value="se connecter"></a><a href="http://localhost/projet/connexion/inscription.php"><input type="button" class="inscription" value="inscription" ></a>';
            }
	        ?></h1> <br>
			<br><br><br>
			<a href="http://localhost/projet/messagerie/messagerie.php"><img  alt="messagerie" id="messagerie" src="images/messagerie.png"></a>
			<br>
			 <form  method="post" id="formulaire" action="specialites/page_type/page_spe.php">
				<div class="spe">
					<h2> spécialité scientifique </h2>
					<button class="imagespe"onmouseover="affiche(1);" onmouseout="noaffiche(1);" type="submit" value="mathématiques" name="spe"><img id="math" alt="math" src="images/spe/math.png"><input type="button" value="math" id="textmath"class="text"></button> 

					<button class="imagespe" type="submit" value="NSI" name="spe"><img alt="nsi" src="images/spe/nsi.png"></button> 
					<button class="imagespe" type="submit" value="math complementaire" name="spe"><img alt="math complementaire" src="images/spe/math.png"></button> 
					<button class="imagespe" type="submit" value="Physique Chimie" name="spe"><img alt="pc" src="images/spe/pc.png"></button> 
					<button class="imagespe" type="submit" value="SVT" name="spe"><img alt="svt" src="images/spe/svt.png"></button> 
				</div>
				<br>
				<div class="spe">
					<h2> spécialité économique </h2>
					<button class="imagespe" type="submit" value="ses" name="spe"><img alt="ses" src="images/spe/ses.png"></button> 
					<button class="imagespe" type="submit" value="géopolitique" name="spe"><img alt="geopo" src="images/spe/geo.png"></button>  
				</div>
				<br>
				<div class="spe">
					<h2> spécialité littéraire </h2>
					<button class="imagespe" type="submit" value="hlp" name="spe"><img alt="hlp" src="images/spe/hlp.png"></button>  
					<button class="imagespe" type="submit" value="anglais littérature" name="spe"><img alt="anglais" src="images/spe/anglais.png"></button>  
					<button class="imagespe" type="submit" value="espagnol littérature" name="spe"><img alt="espagnol" src="images/spe/espagnol.png"></button>  
				</div>
			</form>	
			<br>
			<footer>
			 &copy; Copyright 2021 / Victor Gilbert Philipe Dalet
 / Ambroise Frédérique Manuel Marie Jacquemet--Ramirez Vega
 </footer>
	  </body>
</html>	  