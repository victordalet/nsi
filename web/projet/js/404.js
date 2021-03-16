var point = 0

function Touche(touche)
{
   var event = window.event || touche;
   if (event.keyCode == 90) //32 == touche espace;90 == z
   {
       deplacement(0,90);
   }	
}

function deplacement(x,y)
{
    document.getElementById("perso").style.top += x; 
    document.getElementById("perso").style.left += y;
}

function redirection()
{
	document.location.href="http://localhost/projet";
}

function collision(point)
{
	if (document.getElementById("perso").marginLeft == document.getElementById("piece").marginLeft)
    {
    	if (document.getElementById("perso").marginTop == document.getElementById("piece").marginTop)
    	{
          	document.getElementsByClassName('pieces').marginLeft =  Math.floor(Math.random()* 400)+"px";
	        point += 1;
    	}
    }
	return point
}

function gameOver(point)
{
	point = 0;
    return points
}

/*while (1)
{
    point = collision(point);
}*/