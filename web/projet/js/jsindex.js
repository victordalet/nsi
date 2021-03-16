var compteur = 0
document.getElementById("spe1").style.marginTop = 100+"px"
document.getElementById("spe2").style.marginTop = 100+"px"
document.getElementById("spe3").style.marginTop = 100+"px"


function redirection(spe)
{
	if (spe == 1)
	{
		document.location.href="specialites/math4/math4.php"; // redirection vers une autres pages web selon la spe choisie
	}
	if (spe == 2)
	{
		document.location.href="specialites/nsi/nsi.php"; // redirection vers une autres pages web selon la spe choisie
	}
	if (spe == 3)
	{
		document.location.href="specialites/math3/math3.php"; // redirection vers une autres pages web selon la spe choisie
	}
	if (spe == 4)
	{
		document.location.href="specialites/pc/pc.php"; // redirection vers une autres pages web selon la spe choisie
	}
	if (spe == 5)
	{
		document.location.href="specialites/svt/svt.php"; // redirection vers une autres pages web selon la spe choisie
	}
	if (spe == 6)
	{
		document.location.href="specialites/ses/ses.php"; // redirection vers une autres pages web selon la spe choisie
	}
	if (spe == 7)
	{
		document.location.href="specialites/geopo/geopo.php"; // redirection vers une autres pages web selon la spe choisie
	}
	if (spe == 8)
	{
		document.location.href="specialites/hlp/hlp.php"; // redirection vers une autres pages web selon la spe choisie
	}
	if (spe == 9)
	{
		document.location.href="specialites/angllitt/angllitt.php"; // redirection vers une autres pages web selon la spe choisie
	}
	if (spe == 10)
	{
		document.location.href="specialites/espagnollitt/espagnollitt.php"; // redirection vers une autres pages web selon la spe choisie
	}
}

function animationtexte(compteur)
{
		if (compteur < 100)
		{
			document.getElementById("titre").style.marginLeft += Math.floor(Math.random()* 3)+"px";
		}
		else
		{
			document.getElementById("titre").style.marginLeft -= Math.floor(Math.random()* 3)+"px";
		}
		compteur +=1
		if (compteur == 200)
		{
		    compteur = 0;
		}
		
        return compteur
} 
while (1) 
{
	compteur = animationtexte(compteur);
}
