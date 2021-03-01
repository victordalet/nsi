var gold = 20
var play = true
var gobeletA2 = false
var gobeletA3 = false
var gobeletA4 = false

function animation1(play)
{
	if (play == true)
	{
        var img = document.getElementById("gobelet"); //decomposer pour meilleure visibilité
        var t = img.style.transform.match(/(\d+)/g) || [0]; 
        var val = ( t[0] *1 +180) % 360; // le degrés                     
        img.style.transform = 'rotate(' +val +'deg)'; //la forme finale
        
        play = false
        setTimeout(suiteAnimation1, 2000)
        return play
	}
}

function suiteAnimation1()
{
	var img = document.getElementById("gobelet");
    var t = img.style.transform.match(/(\d+)/g) || [0]; 
    var val = ( t[0] *1 +180) % 360;                      
    img.style.transform = 'rotate(' +val +'deg)';
}

function animation2(play)
{
	if (play == true)
	{
		var img = document.getElementById("gobelet2");
        var t = img.style.transform.match(/(\d+)/g) || [0]; 
        var val = ( t[0] *1 +180) % 360;                      
        img.style.transform = 'rotate(' +val +'deg)';
        
        play = false
        setTimeout(suiteAnimation2, 2000)
        return play
	}
}

function suiteAnimation2()
{
	var img = document.getElementById("gobelet2");
    var t = img.style.transform.match(/(\d+)/g) || [0]; 
    var val = ( t[0] *1 +180) % 360;                      
    img.style.transform = 'rotate(' +val +'deg)';
}

function animation3(play)
{
	if (play==true)
	{
       	var img = document.getElementById("gobelet3");
        var t = img.style.transform.match(/(\d+)/g) || [0]; 
        var val = ( t[0] *1 +180) % 360;                      
        img.style.transform = 'rotate(' +val +'deg)';
        
        play = false
        setTimeout(suiteAnimation3, 2000)
        return play
	}
}            

function suiteAnimation3()
{
	var img = document.getElementById("gobelet3");
    var t = img.style.transform.match(/(\d+)/g) || [0]; 
    var val = ( t[0] *1 +180) % 360;                      
    img.style.transform = 'rotate(' +val +'deg)';
}

function aleatoire(gold,play)
{
	if (gold >= 5 && play==true)
	{
		verre = Math.floor(Math.random()*1000)
		gold -= 5
		if (verre < 333)
		{
			document.getElementById("resultat").style.opacity = "1	";
			document.getElementById("resultat").value = "Vous gagné 20 pièces";
			gold += 20;
		}
		else if (verre >=333 && verre <= 666)
		{
			document.getElementById("resultat").style.opacity = "1";
			document.getElementById("resultat").value = "Perdue";
		}	
		else 
		{
			document.getElementById("resultat").style.opacity = "1";
			document.getElementById("resultat").value = "Perdue";
		}
		
		
	}
	document.getElementById("nombre").value = gold;
	return gold
}

function restart(play)
{
	document.getElementById("resultat").style.opacity = "0";
	play = true
	return play
}

function changeskin(skins,gold,gobeletA2,gobeletA3,gobeletA4)
{
    if (skins==1) //  || = or
    {
	   	document.getElementById("gobelet").src = "images/gobelet.png"
	    document.getElementById("gobelet2").src = "images/gobelet.png"
	    document.getElementById("gobelet3").src = "images/gobelet.png"
    }
    else if (skins == 2 && gold >=100 )
    {
    	if (gobeletA2 == false)
    	{
          gold -= 100
    	}
        document.getElementById("gobelet").src = "images/gobelet2.png"
	    document.getElementById("gobelet2").src = "images/gobelet2.png"
	    document.getElementById("gobelet3").src = "images/gobelet2.png"
	    gobeletA2 = true
    }
        else if (skins == 3 && gold >=50 )
    {
    	if (gobeletA3 == false)
    	{
          gold -= 50
    	}
        document.getElementById("gobelet").src = "images/gobelet3.png"
	    document.getElementById("gobelet2").src = "images/gobelet3.png"
	    document.getElementById("gobelet3").src = "images/gobelet3.png"
	    gobeletA3 = true
    }
        else if (skins == 4 && gold >= 10 )
    {
    	if (gobeletA2 == false)
    	{
          gold -= 10
    	}
        document.getElementById("gobelet").src = "images/gobelet4.png"
	    document.getElementById("gobelet2").src = "images/gobelet4.png"
	    document.getElementById("gobelet3").src = "images/gobelet4.png"
	    gobeletA4 = true
    }
    document.getElementById("nombre").value = gold;
    return gold,gobeletA2,gobeletA3,gobeletA4
}
