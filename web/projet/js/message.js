function envoieTouche()
{
    var event = window.event || touche;
     if (event.keyCode == 13 ) // entrer
     {
     	document.getElementById("envoie"). submit();
     }
}