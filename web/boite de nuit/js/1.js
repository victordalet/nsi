function rouge()
{
	document.getElementById('couleur').style.color = "#FC2F03"
}

function vert()
{
	document.getElementById('couleur').style.color = "#38FC03"
}

function bleu()
{
	document.getElementById('couleur').style.color = "#030BFC"
}

function randomCouleurs()
{
	couleurchoisie = Math.floor(Math.random()*1000)
	if (couleurchoisie < 333)
	{
	    document.getElementById('couleur').style.color = "#030BFC"
	}
	else if (couleurchoisie < 666 && couleurchoisie > 333)
	{
		document.getElementById('couleur').style.color = "#38FC03"
	}		
	else
	{
		document.getElementById('couleur').style.color = "#FC2F03"
	}
}

function cadrecouleurs()
{
	couleurchoisiefond = Math.floor(Math.random()*1000)
	if (couleurchoisiefond < 333)
	{
	    document.getElementById('couleur').style.backgroundColor = "#030BFC"
	}
	else if (couleurchoisiefond < 666 && couleurchoisiefond > 333)
	{
		document.getElementById('couleur').style.backgroundColor = "#38FC03"
	}		
	else
	{
		document.getElementById('couleur').style.backgroundColor = "#FC2F03"
	}
}

function randombg() 
{
	couleurchoisiebg = Math.floor(Math.random()*1000)
	if (couleurchoisiebg < 333)
	{
	    document.body.style.background = "#030BFC" //vert
	}
	else if (couleurchoisiebg < 666 && couleurchoisiefond > 333)
	{
		document.body.style.background = "#38FC03" //bleu
	}		
	else
	{
		document.body.style.background = "#FC2F03" //rouge
	}
}

function pause()
{
  setInterval(function(){ boiteNuit(); }, 100); 
}
	

function boiteNuit()
{
	cadrecouleurs();
	randomCouleurs();
	randombg();
}

function randomBouton()
{
    document.getElementById("tp").style.marginTop = Math.floor(Math.random()* 400)+"px"; 
    document.getElementById("tp").style.marginLeft = Math.floor(Math.random()* 400)+"px"; 
}	

function cliquebouton()
{
	alert("gg")
}


function couleurDemande()
{
	document.body.style.background = document.getElementById("couleurfond").value;
}

function couleurDemandetext()
{
	document.getElementById('couleur').style.color = document.getElementById("couleurtext").value;
}

function couleurDemandetextfond()
{
	document.getElementById('couleur').style.backgroundColor= document.getElementById("couleurtextfond").value;
}