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
				<h1><a href="http://localhost/projet"><img alt="logo" id="logospe" src="../../images/logo.png"></a>La SVT</h1>
				<br><br><br><br><br><br>
				<div class="spe"> 
				<h2>description spécialité</h2>
				</div>
				<div class="spe">
				<h2>les metiers</h2>
			    </div>	
			    </div class="spe">
				<h2>programme</h2>
				</div>
			';
		}
		if ($specialite == 'NSI')
		{
			echo'
				<h1><a href="http://localhost/projet"><img alt="logo" id="logospe" src="../../images/logo.png"></a>La NSI</h1>
				<br><br><br><br><br><br>
				<div class="spe"> 
				<h2>description spécialité</h2>
				</div>
				<div class="spe">
				<h2>les metiers</h2>
			    </div>	
			    </div class="spe">
				<h2>programme</h2>
				</div>
			';
		}
		if ($specialite == 'mathématiques')
		{
			echo'
				<h1><a href="http://localhost/projet"><img alt="logo" id="logospe" src="../../images/logo.png"></a>Les Mathématiques</h1>
				<br><br><br><br><br><br>
				<div class="spe"> 
				<h2>description spécialité :</h2>
				</div>
				<div class="spe">
				<h2>Les metiers : </h2>
			    </div>	
			    <div class="spe">
				<h2>Programme : </h2>
				</div>
			';
		}
		if ($specialite == 'math complementaire')
		{
			echo'
				<h1><a href="http://localhost/projet"><img alt="logo" id="logospe" src="../../images/logo.png"></a>Les Math Complémentaire </h1>
				<br><br><br><br><br><br>
				<div class="spe"> 
				<h2>description spécialité :</h2>
				</div>
				<div class="spe">
				<h2>Les metiers : </h2>
			    </div>	
			    <div class="spe">
				<h2>Programme : </h2>
				</div>
			';
		}
		if ($specialite == 'Physique Chimie')
		{
			echo'
				<h1><a href="http://localhost/projet"><img alt="logo" id="logospe" src="../../images/logo.png"></a>La Physique Chimie</h1>
				<br><br><br><br><br><br>
				<div class="spe"> 
				<h2>description spécialité :</h2>
				</div>
				<div class="spe">
				<h2>Les metiers : </h2>
			    </div>	
			    <div class="spe">
				<h2>Programme : </h2>
				</div>
			';
		}
		if ($specialite == 'ses')
		{
			echo'
				<h1><a href="http://localhost/projet"><img alt="logo" id="logospe" src="../../images/logo.png"></a>La SES</h1>
				<br><br><br><br><br><br>
				<div class="spe"> 
				<h2>description spécialité :</h2>
				</div>
				<div class="spe">
				<h2>Les metiers : </h2>
			    </div>	
			    <div class="spe">
				<h2>Programme : </h2>
				</div>
			';
		}
		if ($specialite == 'géopolitique')
		{
			echo'
				<h1><a href="http://localhost/projet"><img alt="logo" id="logospe" src="../../images/logo.png"></a>La géopolitique</h1>
				<br><br><br><br><br><br>
				<div class="spe"> 
				<h2>description spécialité :</h2>
				</div>
				<div class="spe">
				<h2>Les metiers : </h2>
			    </div>	
			    <div class="spe">
				<h2>Programme : </h2>
				</div>
			';
		}
		if ($specialite == 'hlp')
		{
			echo'
				<h1><a href="http://localhost/projet"><img alt="logo" id="logospe" src="../../images/logo.png"></a>Humanité littérature Phylosophie</h1>
				<br><br><br><br><br><br>
				<div class="spe"> 
				<h2>description spécialité :</h2>
				</div>
				<div class="spe">
				<h2>Les metiers : </h2>
			    </div>	
			    <div class="spe">
				<h2>Programme : </h2>
				</div>
			';
		}
		if ($specialite == 'anglais littérature')
		{
			echo'
				<h1><a href="http://localhost/projet"><img alt="logo" id="logospe" src="../../images/logo.png"></a>Anglais Littérature</h1>
				<br><br><br><br><br><br>
				<div class="spe"> 
				<h2>description spécialité :</h2>
				</div>
				<div class="spe">
				<h2>Les metiers : </h2>
			    </div>	
			    <div class="spe">
				<h2>Programme : </h2>
				</div>
			';
		}
		if ($specialite == 'espagnol littérature')
		{
			echo'
				<h1><a href="http://localhost/projet"><img alt="logo" id="logospe" src="../../images/logo.png"></a>Espagnol Littérature</h1>
				<br><br><br><br><br><br>
				<div class="spe"> 
				<h2>description spécialité :</h2>
				</div>
				<div class="spe">
				<h2>Les metiers : </h2>
			    </div>	
			    <div class="spe">
				<h2>Programme : </h2>
				</div>
			';
		}
         		
		?>

	</body>
</html>