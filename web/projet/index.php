<!doctype HTML>
<html lang="fr">
      <head> 
	       <title> projet ecole  </title> <!--le titre de la page -->
		   <link rel="stylesheet" href="css/style.css"> <!-- on imparte le css -->
		   <link rel="icon" type="image/png" href="images/logo.png" /> <!-- logo à coté du titre-->
	  </head>
	        
	  <body>
	  	    <h1 id="titre"><a href="http://localhost/projet"><img alt="logo" class="logoindex" src="images/acceuil.png"></a> NOTRE DAME DE LA PROVIDENCE
	  	     <?php 

            if (isset($_COOKIE["connecter"])) //si il y a un cookie on propose de se déconnecter
            {
            	echo '<a href="http://localhost/projet/connexion/supprimmer.php"><input type="button" class="inscription" value="Se Déconnecter" ></a>';
            }
            else // sinon on propose de se connecter ou de s'inscrire
            {
            	echo '<a href="http://localhost/projet/connexion/connexion.php"><input type="button" class="inscription" value="se connecter"></a><a href="http://localhost/projet/connexion/inscription.php"><input type="button" class="inscription" value="inscription" ></a>';
            }
	        ?></h1> <br>
			<br><br><br>
			<a href="http://localhost/projet/messagerie/messagerie.php"><img  alt="messagerie" id="messagerie" src="images/messagerie.png"></a>
			<br>
			 <form  method="post" id="formulaire" action="specialites/page_type/page_spe.php">
				<div class="spe">
					<h2> spécialité scientifique </h2> <!--plusieures div avec les spe -->
					<button class="imagespe" type="submit" value="mathématiques" name="spe"><img id="math" alt="math" src="images/spe/math4.png"><h3 class="text">Mathématiques</h3> </button>

					<button class="imagespe" type="submit" value="NSI" name="spe"><img alt="nsi" src="images/spe/nsi.png"><h3 class="text">NSI</h3></button> 

					<button class="imagespe" type="submit" value="math complementaire" name="spe"><img alt="math complementaire" src="images/spe/math.png"><h3 class="text">Math Compl</h3></button> 

					<button class="imagespe" type="submit" value="Physique Chimie" name="spe"><img alt="pc" src="images/spe/pc.png"><h3 class="text">Physique Chimie</h3></button> 

					<button class="imagespe" type="submit" value="SVT" name="spe"><img alt="svt" src="images/spe/svt.png"><h3 class="text">SVT</h3></button> 
				</div>
				<br>
				<div class="spe">
					<h2> spécialité économique </h2>
					<button class="imagespe" type="submit" value="ses" name="spe"><img alt="ses" src="images/spe/ses.png"><h3 class="text">SES</h3></button>

					<button class="imagespe" type="submit" value="géopolitique" name="spe"><img alt="geopo" src="images/spe/geo.png"><h3 class="text">Géopolitique</h3></button>  
				</div>
				<br>
				<div class="spe">
					<h2> spécialité littéraire </h2>
					<button class="imagespe" type="submit" value="hlp" name="spe"><img alt="hlp" src="images/spe/hlp.png"><h3 class="text">HLP</h3></button>

					<button class="imagespe" type="submit" value="anglais littérature" name="spe"><img alt="anglais" src="images/spe/anglais.png"><h3 class="text">Anlgais</h3></button>  

					<button class="imagespe" type="submit" value="espagnol littérature" name="spe"><img alt="espagnol" src="images/spe/espagnol.png"><h3 class="text">Espagnol</h3></button>  
				</div>
			</form>	
			<br>
			<footer>
			 &copy; Copyright 2021 / Victor Gilbert Philipe Dalet
 / Ambroise Frédérique Manuel Marie Jacquemet--Ramirez Vega
 </footer>
	  </body>
</html>	  