// javascripte du jeu et de la page selon un clique ou un evenement
let point = 0; // variable nombre de point 
let x = 0; //variable position joueur en x
let y = 0; // variable position joueur en y
let lancer = false; // varaible si le jeu est lance ou non

function Touche(touche,x,y,lancer,point) // fonction se declanche si touche clavier detecter
{
  var vitesse_deplacement = 8; // constante 
  var vitesse_saut = 10; // constante
  var event = window.event || touche; //constante pour evenement de touche
  if (lancer == true) // si le jeu est lancer
  {
    if (event.keyCode == 68) //68 == d touche
    {
       x += vitesse_deplacement; // on augmente x
       document.getElementById("perso").style.marginLeft = x+"px"; //on affiche le changement
    }
    else if (event.keyCode == 81) // q == 81 touche
    {
       x -= vitesse_deplacement; // on diminue y
       document.getElementById("perso").style.marginLeft = x+"px"; // affichage du changement
    } 
    else if (event.keyCode == 32) //32 == space
    {
       for (let i = 0; i < 100; i++)  //boucle 
    {
      if (i < 50) 
      {
        y += vitesse_saut; //on augmente pour que le joueur monte
        document.getElementById("perso").style.marginTop = y+"px";
      }
      else
      {
        y -= vitesse_saut; // on diminue pour qu'il redéscende
        document.getElementById("perso").style.marginTop = y+"px";
      }
    } 
   } 
  if (document.getElementById("perso").style.marginLeft == document.getElementById("piece").style.marginLeft) //colision entre le joeur et la piece
  {
    point++; // on augmente la variable point 
    document.getElementById("afficherpoint").value = "point : ",point; //affichage
    document.getElementById("piece").style.marginLeft = Math.floor(Math.random()* 400)+"px";  //on repositionne aléatoirement la pièce
  }
  if (document.getElementById("perso").style.marginLeft == document.getElementById("ennemie").style.marginLeft) // colision avec ennemie
  {
    point = 0; // on réinitialise les points
    document.getElementById("boutonjouer").style;opacity+"1"; // on fait apparaitre le bouton de jeu
    lancer = false; // on eteint le jeu
  }
  }
return x,y,point;
}  

function redirection()
{
	document.location.href="http://localhost/projet"; //redirection sur l'acceuil
}


function play(lancer) // quand on appuit sur le bouton play
{
   document.getElementById("boutonjouer").style.opacity = "0"; //on fait disparaitre le bouton
   lancer = true; //on actionne la partie
   return lancer;
}