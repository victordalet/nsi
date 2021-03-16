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
				<section class="choix" id = "spe1">
					<h2> spécialité scientifique </h2>
					<input type="button" value="mathématiques" name ="math4" onclick="redirection(1);" class="index"> <br>
					<input type="button" value="nsi" name ="nsi" onclick="redirection(2);" class="index"> <br>
					<input type="button" value="math complementaire" name ="math3" onclick="redirection(3);" class="index"> <br>
					<input type="button" value="Physique Chimie" name ="pc" onclick="redirection(4);" class="index"> <br>
					<input type="button" value="Svt" name ="svt" onclick="redirection(5);" class="index"> 
				</section>
				<section class="choix" id = "spe2">
					<h2> spécialité économique </h2>
					<input type="button" value="ses" name ="ses" onclick="redirection(6);" class="index"> <br>
					<input type="button" value="géopolitique" name ="geopo" onclick="redirection(7);" class="index"> 
				</section >
				<section class="choix" id = "spe3">
					<h2> spécialité littéraire </h2>
					<input type="button" value="hlp" name ="hlp" onclick="redirection(8);" class="index"> <br>
					<input type="button" value="anglais littérature" name ="anglais" onclick="redirection(9);" class="index"> <br>
					<input type="button" value="espagnol littérature" name ="espagnol" onclick="redirection(10);" class="index"> 
				</section>

	  
	  </body>
</html>	  