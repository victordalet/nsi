//javascript du jeu de la page 404 en boucle infinie
var y_e = 0;// variable de la position de l'ennemie
var y_p = 0; //variable de la position de la piece
var vitesse = 0.1; // varaible de la vitesse de déscente
while (1)
{
   y_e += vitesse; // vitesse de l'ennnemie
   y_p += vitesse; // vitesse déscente
   document.getElementById("piece").style.marginTop = y_p+"px";
   document.getElementById("ennemie").style.marginTop = y_e+"px";
   document.getElementById("perso").style.marginLeft = x+"%"; 
   if (document.getElementById("ennemie").style.left == 0+"px") // si l'ennemie touche le bord de l'écrant
   {
    	document.getElementById("ennemie".style.left == 100+"px");// il revient en arrière
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
    document.getElementById("boutonjouer").style.opacity+"1"; // on fait apparaitre le bouton de jeu
    lancer = false; // on eteint le jeu
  }
}