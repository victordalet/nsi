let point = 0;
let x = 0;
let y = 0;
let lancer = false;

function Touche(touche,x,y,lancer,point)
{
  var vitesse_deplacement = 8;
  var vitesse_saut = 10;
  var event = window.event || touche;
  if (lancer == true)
  {
    if (event.keyCode == 68) //68 == d
    {
       x += vitesse_deplacement;
       document.getElementById("perso").style.marginLeft = x+"px";
    }
    else if (event.keyCode == 81) // q == 81
    {
       x -= vitesse_deplacement;
       document.getElementById("perso").style.marginLeft = x+"px";
    } 
    else if (event.keyCode == 32) //32 == space
    {
       for (let i = 0; i < 100; i++) 
    {
      if (i < 50)
      {
        y += vitesse_saut;
        document.getElementById("perso").style.marginTop = y+"px";
      }
      else
      {
        y -= vitesse_saut;
        document.getElementById("perso").style.marginTop = y+"px";
      }
    } 
   } 
  if (document.getElementById("perso").style.marginLeft == document.getElementById("piece").style.marginLeft)
  {
    point++;
    document.getElementById("afficherpoint").value = "point : ",point;
    document.getElementById("piece").style.marginLeft = Math.floor(Math.random()* 400)+"px"; 
  }
  if (document.getElementById("perso").style.marginLeft == document.getElementById("ennemie").style.marginLeft)
  {
    point = 0;
    document.getElementById("boutonjouer").style;opacity+"1";
    lancer = false;
  }
  }
return x,y,point;
}  

function redirection()
{
	document.location.href="http://localhost/projet";
}

function gameOver(point)
{
	point = 0;
  return point;
}

function play(lancer)
{
   document.getElementById("boutonjouer").style.opacity = "0";
   lancer = true;
   return lancer;
}