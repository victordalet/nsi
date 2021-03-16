<!doctype HTML>
<html lang="fr">
      <head> 
	       <title> projet ecole  </title> <!--le titre de la page -->
		   <link rel="stylesheet" href="css/style.css"> <!-- on imparte le css -->
		   <script src="js/jsindex.js"></script> <!-- on import le js -->
		   <link rel="icon" type="image/png" href="images/logo.png" /> <!-- logo à coté du titre-->
	  </head>
	        
	  <body>
	        <div id="cadretitre"><h1 id="titre"> le site de l'école </h1></div> <br>
			<h3> descirption de l'école <h3> <br>
			<br>
			 <form  method="post" id="formulaire" action="specialites/page_type/page_type.php">
				<section class="choix" id = "spe1">
					<h2> spécialité scientifique </h2>
					<input type="submit" value="mathématiques" name="spe" onclick="redirection(1);" class="index"> <br>
					<input type="submit" value="NSI" name ="spe" onclick="redirection(2);" class="index"> <br>
					<input type="submit" value="math complementaire" name ="spe" onclick="redirection(3);" class="index"> <br>
					<input type="submit" value="Physique Chimie" name ="spe" onclick="redirection(4);" class="index"> <br>
					<input type="submit" value="SVT" name ="spe" onclick="redirection(5);" class="index"> 
				</section>
				<section class="choix" id = "spe2">
					<h2> spécialité économique </h2>
					<input type="submit" value="ses" name ="spe" onclick="redirection(6);" class="index"> <br>
					<input type="submit" value="géopolitique" name ="spe" onclick="redirection(7);" class="index"> 
				</section >
				<section class="choix" id = "spe3">
					<h2> spécialité littéraire </h2>
					<input type="submit" value="hlp" name ="spe" onclick="redirection(8);" class="index"> <br>
					<input type="submit" value="anglais littérature" name ="spe" onclick="redirection(9);" class="index"> <br>
					<input type="submit" value="espagnol littérature" name ="spe" onclick="redirection(10);" class="index"> 
				</section>
			</form>	

	  
	  </body>
</html>	  