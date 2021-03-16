function Touche(touche)
{
   var event = window.event || touche;
   if (event.keyCode == 32) // touche espace
   {
       document.getElementById("perso").marginTop = 200+"px";   
       document.getElementsByClassName('test').marginLeft += 8+"px";
   }
 	
}

function redirection()
{
	document.location.href="http://localhost/projet";
}
//while (1)
{
	document.getElementsByClassName('test').marginLeft += 8+"px";
}