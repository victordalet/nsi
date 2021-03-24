// javascripte du jeu et de la page selon un clique ou un evenement
let point = 0; // variable nombre de point 
let x = 50; //variable position joueur en x
let y = 0; // variable position joueur en y
let lancer = false; // varaible si le jeu est lance ou non


function Touche(touche,x,y,lancer,point) // fonction se declanche si touche clavier detecter
{
  var vitesse_deplacement = 8; // constante 
  var vitesse_saut = -50; // constante
  var event = window.event || touche; //constante pour evenement de touche
  if (lancer == true) // si le jeu est lancer
  {
    if (event.keyCode == 68) //68 == d touche
    {
       x += vitesse_deplacement; // on augmente x
       document.getElementById("perso").style.marginLeft = x+"%"; //on affiche le changement
       console.log(x);
    }
    else if (event.keyCode == 81) // q == 81 touche
    {
       x -= vitesse_deplacement; // on diminue y
       document.getElementById("perso").style.marginLeft = x+"%"; // affichage du changement
    } 
    else if (event.keyCode == 32) //32 == space
    {
     y += vitesse_saut;
     document.getElementById("perso").style.marginTop = y+"px";
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