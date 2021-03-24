<!doctype HTML>
<html lang="fr">
	<head>
		<?php
		$specialite = $_POST["spe"];
		echo '<title>'.$specialite.'</title>';
		?>
		<link rel="stylesheet" href="../../css/style.css"/>
		<script type="text/javascript" src="/"></script>
		<link rel="icon" type="image/png" href="../../images/logo.png" /> <!-- logo à coté du titre-->
	</head>
	
	<body>
		<?php
		
		if ($specialite == 'SVT')
		{
			echo'
				<h1><a href="http://localhost/projet"><img alt="logo" class="logoindex" src="../../images/acceuil.png"></a>La SVT</h1>
				<br><br><br><br><br><br>
				<div class="spe"> 
				<h2>Description spécialité :</h2>
				<h5>La nouvelle spécialité Sciences de la vie et de la Terre vise à dispenser une formation scientifique solide. L objectif principale de la spécialité est de développer votre culture scientifique afin d effectuer votre citoyenneté</h5>
				</div>
				<div class="spe">
				<h2>les metiers</h2>
				<img alt="métiers" src="../../images/spe/description/svt2.jpeg">
			    </div>	
			    <div class="spe">
				<h2>programme</h2>
				<img alt="programme" src="../../images/spe/description/svt1.png">
				</div>
			';
		}
		if ($specialite == 'NSI')
		{
			echo'
				<h1><a href="http://localhost/projet"><img alt="logo" class="logoindex" src="../../images/acceuil.png"></a>La NSI</h1>
				<br><br><br><br><br><br>
				<div class="spe"> 
				<h2>Description spécialité : </h2>
				<h5>Aujourd’hui, le numérique, c’est de la culture générale, nécessaire pour votre vie personnelle comme professionnelle. Pour travailler dans le développement durable, la littérature, le cinéma ou la santé, c’est toujours bien de savoir ce qu’est un algorithme, un langage de programmation, une base de données. C’est d’ailleurs pour cette raison que tous les élèves de 2de suivent un cours de Sciences Numériques et Technologiques.

La spécialité Numérique et sciences informatiques vous permet de comprendre les bases de la programmation, pour élaborer des logiciels par exemple, des sites internet, des applications pour smartphones, etc.</h5>
				</div>
				<div class="spe">
				<h2>Les metiers : </h2>
				<img alt="métiers" src="../../images/spe/description/nsi2.jpg">
			    </div>	
			    <div class="spe">
				<h2>Programme :</h2>
				<img alt="programme" src="../../images/spe/description/nsi1.jpg">
				</div>
			';
		}
		if ($specialite == 'mathématiques')
		{
			echo'
				<h1><a href="http://localhost/projet"><img alt="logo" class="logoindex" src="../../images/acceuil.png"></a>Les Mathématiques</h1>
				<br><br><br><br><br><br>
				<div class="spe"> 
				<h2>Description spécialité :</h2>
				<h5>Le programme de mathématiques définit un ensemble de connaissances et de compétences, réaliste et ambitieux, qui s’appuie sur le programme de seconde dans un souci de cohérence, en réactivant les notions déjà étudiées et y ajoutant un nombre raisonnable de nouvelles notions, à étudier de manière suffisamment approfondie.</h5>
				</div>
				<div class="spe">
				<h2>Les metiers : </h2>
				<img alt="métiers" src="../../images/spe/description/math2.jpg">
			    </div>	
			    <div class="spe">
				<h2>Programme : </h2>
				<img alt="programme" src="../../images/spe/description/math1.jpg">
				</div>
			';
		}
		if ($specialite == 'math complementaire')
		{
			echo'
				<h1><a href="http://localhost/projet"><img alt="logo" class="logoindex" src="../../images/acceuil.png"></a>Les Math Complémentaire </h1>
				<br><br><br><br><br><br>
				<div class="spe"> 
				<h2>Description spécialité :</h2>
				<h5>Le programme de mathématiques définit un ensemble de connaissances et de compétences, réaliste et ambitieux, qui s’appuie sur le programme de seconde dans un souci de cohérence, en réactivant les notions déjà étudiées et y ajoutant un nombre raisonnable de nouvelles notions, à étudier de manière suffisamment approfondie.</h5>
				</div>
				<div class="spe">
				<h2>Les metiers : </h2>
				<img alt="métiers" src="../../images/spe/description/math2.jpg">
			    </div>	
			    <div class="spe">
				<h2>Programme : </h2>
				<img alt="programme" src="../../images/spe/description/math1.jpg">
				</div>
			';
		}
		if ($specialite == 'Physique Chimie')
		{
			echo'
				<h1><a href="http://localhost/projet"><img alt="logo" class="logoindex" src="../../images/acceuil.png"></a>La Physique Chimie</h1>
				<br><br><br><br><br><br>
				<div class="spe"> 
				<h2>Description spécialité :</h2>
				<h5>La physique-chimie a pour but de modéliser le réel en mettant en œuvre des mesures
qui conduisent à formuler des lois, afin d expliquer et de prévoir divers phénomènes.</h5>
				</div>
				<div class="spe">
				<h2>Les metiers : </h2>
				<img alt="métiers" src="../../images/spe/description/pc2.jpg">
			    </div>	
			    <div class="spe">
				<h2>Programme : </h2>
				<img alt="programme" src="../../images/spe/description/pc1.png">
				</div>
			';
		}
		if ($specialite == 'ses')
		{
			echo'
				<h1><a href="http://localhost/projet"><img alt="logo" class="logoindex" src="../../images/acceuil.png"></a>La SES</h1>
				<br><br><br><br><br><br>
				<div class="spe"> 
				<h2>Description spécialité :</h2>
				<h5>Une matière qui mobilise des disciplines
telles que l’économie, la sociologie, la
science politique mais également
l’histoire-géographie, les
mathématiques…</h5>
				</div>
				<div class="spe">
				<h2>Les metiers : </h2>
				<img alt="métiers" src="../../images/spe/description/ses2.jpg">
			    </div>	
			    <div class="spe">
				<h2>Programme : </h2>
				<img alt="programme" src="../../images/spe/description/ses1.png">
				</div>
			';
		}
		if ($specialite == 'géopolitique')
		{
			echo'
				<h1><a href="http://localhost/projet"><img alt="logo" class="logoindex" src="../../images/acceuil.png"></a>La géopolitique</h1>
				<br><br><br><br><br><br>
				<div class="spe"> 
				<h2>Description spécialité :</h2>
				<h5>Comprendre un régime politique : la démocratie (de l’Athènes antique à l’Union Européenne en passant par l’analyse de contre exemple comme les dictatures chilienne, espagnole ou portugaise).
Analyser les dynamiques des puissances internationales :
(ex : Russie, Etats-Unis, Firmes Transnationales , Softpower).
Etudier les divisions politiques du monde :
les frontières (ex :de l’Empire Romain aux deux Corée, l’Espace Schengen dans l’UE, la gestion de l’espace maritime).
S informer : un regard critique sur les sources et les modes de communication (ex : presse, Internet, fake news).
Analyser les relations entre Etats et religions (du monde médiéval aux enjeux contemporains).</h5>
				</div>
				<div class="spe">
				<h2>Les metiers : </h2>
				<img alt="métiers" src="../../images/spe/description/geo2.png">
			    </div>	
			    <div class="spe">
				<h2>Programme : </h2>
				<img alt="programme" src="../../images/spe/description/geo1.jpg">
				</div>
			';
		}
		if ($specialite == 'hlp')
		{
			echo'
				<h1><a href="http://localhost/projet"><img alt="logo" class="logoindex" src="../../images/acceuil.png"></a>Humanité littérature Phylosophie</h1>
				<br><br><br><br><br><br>
				<div class="spe"> 
				<h2>Description spécialité :</h2>
				<h5>La spécialité HLP est une formation dans le domaine des lettres, de la philosophie et des sciences humaine. Elle est prise en charge par deux professeurs qui enseignent chacun la littérature ou la philosophie.</h5>
				</div>
				<div class="spe">
				<h2>Les metiers : </h2>
				<img alt="métiers" src="../../images/spe/description/hlp2.png">
			    </div>	
			    <div class="spe">
				<h2>Programme : </h2>
				<img alt="programme" src="../../images/spe/description/hlp1.png">
				</div>
			';
		}
		if ($specialite == 'anglais littérature')
		{
			echo'
				<h1><a href="http://localhost/projet"><img alt="logo" class="logoindex" src="../../images/acceuil.png"></a>Anglais Littérature</h1>
				<br><br><br><br><br><br>
				<div class="spe"> 
				<h2>Description spécialité :</h2>
				<h5>- Exploration approfondie de la langue dans tous ses aspects
- Renforcement de la maîtrise de la langue
(5 activités langagières: à l’oral/écrit)
- Acquisition de stratégies de lecture et de méthodes d’analyse
- Enrichissement des connaissances (domaine littéraire, artistique, …)
- Meilleure compréhension des cultures du monde anglophone
- Ouverture sur le monde
- Développer le goût de la lecture en langue étrangère</h5>
				</div>
			    <div class="spe">
				<h2>Programme : </h2>
				<img alt="programme" src="../../images/spe/description/langue1.png">
				</div>
			';
		}
		if ($specialite == 'espagnol littérature')
		{
			echo'
				<h1><a href="http://localhost/projet"><img alt="logo" class="logoindex" src="../../images/acceuil.png"></a>Espagnol Littérature</h1>
				<br><br><br><br><br><br>
				<div class="spe"> 
				<h2>Description spécialité :</h2>
								<h5>- Exploration approfondie de la langue dans tous ses aspects
- Renforcement de la maîtrise de la langue
(5 activités langagières: à l’oral/écrit)
- Acquisition de stratégies de lecture et de méthodes d’analyse
- Enrichissement des connaissances (domaine littéraire, artistique, …)
- Meilleure compréhension des cultures du monde anglophone
- Ouverture sur le monde
- Développer le goût de la lecture en langue étrangère</h5>
				</div>
			    <div class="spe">
				<h2>Programme : </h2>
				<img alt="programme" src="../../images/spe/description/langue1.png">
				</div>
			';
		}
         		
		?>

	</body>
</html>