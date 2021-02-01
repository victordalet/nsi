function validationMDP() 
{
	if (document.getElementById("mot_de_passe").value == 123456) 
	{
		alert("bienvenue");
		location.href = "index2.html";
	}
	else
	{
		alert("oust");
	}
}

function indice_visible()
{
	document.getElementById('indice').style.opacity=1;
}

function indice_invisible()
{
	document.getElementById('indice').style.opacity=0;
}

function affichage_mot2passe()
{
	if (document.getElementById("mot_de_passe").type == "text")
	{
	    document.getElementById("mot_de_passe").type = "password";	
	}    
	else
	{
		document.getElementById("mot_de_passe").type = "text";
	}	
}

function majuscules()
{
	document.getElementById("mot_de_passe").value = document.getElementById("mot_de_passe").value.toUpperCase();

}

function randomBouton()
{
    document.getElementById("tp").style.marginTop = Math.floor(Math.random()* 400)+"px"; 
    document.getElementById("tp").style.marginLeft = Math.floor(Math.random()* 400)+"px"; 
}	

function cliqueTP()
{
	alert("bien jouer");
}
