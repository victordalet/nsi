function envoieTouche() // fonction qui permet de tdetecter si une touche est frappé
{
    var event = window.event || touche; // constante d'évenement
     if (event.keyCode == 13 ) // s'il s'agit de la touche entrer
     {
     	document.getElementById("envoie"). submit(); /*on envoie le message*/
     }
}