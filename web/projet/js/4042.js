//javascript du jeu de la page 404 en boucle infinie
var x_e = 0;// variable de la position de l'ennemie
var vitesse_ennemie = 8;// varaible de la vitesse de l'ennemie
while (1)
{
   x_e -= vitesse_ennemie; // vitesse de l'ennnemie
   if (document.getElementById("ennemie").style.left == 0+"px") // si l'ennemie touche le bord de l'écrant
   {
    	document.getElementById("ennemie".style.left == 100+"px");// il revient en arrière
   }

   if (document.getElementById("perso").style.marginLeft == document.getElementById("piece").style.marginLeft) //colision entre le joeur et la piece
  {
    point++; // on augmente la variable point 
    document.getElementById("afficherpoint").value = "point : ",point; //affichage
    document.getElementById("piece").style.marginLeft = Math.floor(Math.random()* 400)+"px";  //on repositionne aléatoirement la pièce
    vitesse_ennemie++; //on augmente la vitesse de l'ennemie
  }
  if (document.getElementById("perso").style.marginLeft == document.getElementById("ennemie").style.marginLeft) // colision avec ennemie
  {
    point = 0; // on réinitialise les points
    document.getElementById("boutonjouer").style.opacity+"1"; // on fait apparaitre le bouton de jeu
    lancer = false; // on eteint le jeu
  }
}