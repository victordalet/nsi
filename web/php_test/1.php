<!doctype HTML>
<html lang="fr">
      <head> 
	       <title> petit formulaire  </title> <!--le titre de la page -->
		   <link rel="stylesheet" href="1.css"> <!-- on imparte le css -->
		   <script src="1.js"></script> <!-- on import le js -->
		   
	  </head>
	  
	  <body>
       <?php 
	       $name = $_POST["name"];
		   $mdp  = $_POST["message"];
		   $nb1 = $_POST["nombre1"];
		   $nb2 = $_POST["nombre2"];
		   $symbole = $_POST["symbole"];
		   setcookie("premier",$name,time()+360000000);

    
		   if ($name == "bruce" )
		   {
			   if ($mdp ="batman"){
				    print("bonjour, ".$name. '!<br />'); 
			   }
			   else {
				   header('Location: index.html' );
			   }
		   } 
           else
		   {
			   header('Location: index.html' );
		   }
           if ($nb1 == "")
		   {
			   $nb1 = 0;
		   }		
           if ($nb2 == "")
		   {
			   $nb2 = 0;
		   }			   
		   if ($symbole == "+")
		   {
			   $resultat = $nb1 + $nb2;
		   }
		    else if ($symbole == "-")
		   {
			   $resultat = $nb1 - $nb2;
		   }
		   else if ($symbole == "/")
		   {
			   $resultat = $nb1 / $nb2;
		   }
		    else if ($symbole == "*")
		   {
			   $resultat = $nb1 * $nb2;
		   }
		   print(" le calcule vaux: ".$resultat. '!<br />');
		   
		   	if (isset($_COOKIE["premier"]))
		   {
			   print("Le cookie existe " . $_COOKIE["premier"]);
		   }  
           else
		   {
			   ('Le cookie n\'existe pas ');
		   }
		?> 



		</body>   
</html>	