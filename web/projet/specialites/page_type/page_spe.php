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
				<h1>La SVT</h1>
				<section class="gen_descriptif"> 
				<h2>description spécialité</h2>
				<div>dans cette spécialité, vous allez travaillez blablabla</div>
				<h2>les metiers</h2>
				<div>blametier bla</div>
				<h2>programme</h2>
				<div>blabla programme</div>
				</section>
			';
		}
		if ($specialite == 'NSI')
		{
			echo'
				<h1>La NSI</h1>
				<section class="gen_descriptif"> 
				<h2>description spécialité</h2>
				<div>dans cette spécialité, vous allez travaillez blablabla</div>
				<h2>les metiers</h2>
				<div>blametier bla</div>
				<h2>programme</h2>
				<div>blabla programme</div>
				</section>
			';
		}
		if ($specialite == 'mathématiques')
		{
			echo'
				<h1> Les mathématiques (spécialité 4h)</h1>
				<section class="gen_descriptif"> 
				<h2>description spécialité</h2>
				<div>dans cette spécialité, vous allez travaillez blablabla</div>
				<h2>les metiers</h2>
				<div>blametier bla</div>
				<h2>programme</h2>
				<div>blabla programme</div>
				</section>
			';
		}
		if ($specialite == 'math complementaire')
		{
			echo'
				<h1>Les Maths complémentaires</h1>
				<section class="gen_descriptif"> 
				<h2>description spécialité</h2>
				<div>dans cette spécialité, vous allez travaillez blablabla</div>
				<h2>les metiers</h2>
				<div>blametier bla</div>
				<h2>programme</h2>
				<div>blabla programme</div>
				</section>
			';
		}
		if ($specialite == 'Physique Chimie')
		{
			echo'
				<h1>La physique Chimie</h1>
				<section class="gen_descriptif"> 
				<h2>description spécialité</h2>
				<div>dans cette spécialité, vous allez travaillez blablabla</div>
				<h2>les metiers</h2>
				<div>blametier bla</div>
				<h2>programme</h2>
				<div>blabla programme</div>
				</section>
			';
		}
		if ($specialite == 'ses')
		{
			echo'
				<h1>La SES</h1>
				<section class="gen_descriptif"> 
				<h2>description spécialité</h2>
				<div>dans cette spécialité, vous allez travaillez blablabla</div>
				<h2>les metiers</h2>
				<div>blametier bla</div>
				<h2>programme</h2>
				<div>blabla programme</div>
				</section>
			';
		}
		if ($specialite == 'géopolitique')
		{
			echo'
				<h1>La géopolotique (truc de merde)</h1>
				<section class="gen_descriptif"> 
				<h2>description spécialité</h2>
				<div>dans cette spécialité, vous allez travaillez blablabla</div>
				<h2>les metiers</h2>
				<div>blametier bla</div>
				<h2>programme</h2>
				<div>blabla programme</div>
				</section>
			';
		}
		if ($specialite == 'hlp')
		{
			echo'
				<h1>Humanité littérature philosophie (C\'EST DE LA MERDE)</h1>
				<section class="gen_descriptif"> 
				<h2>description spécialité</h2>
				<div>dans cette spécialité, vous allez travaillez blablabla</div>
				<h2>les metiers</h2>
				<div>blametier bla</div>
				<h2>programme</h2>
				<div>blabla programme</div>
				</section>
			';
		}
		if ($specialite == 'anglais littérature')
		{
			echo'
				<h1>anglais</h1>
				<section class="gen_descriptif"> 
				<h2>description spécialité</h2>
				<div>dans cette spécialité, vous allez travaillez blablabla</div>
				<h2>les metiers</h2>
				<div>blametier bla</div>
				<h2>programme</h2>
				<div>blabla programme</div>
				</section>
			';
		}
		if ($specialite == 'espagnol littérature')
		{
			echo'
				<h1>espagnol</h1>
				<section class="gen_descriptif"> 
				<h2>description spécialité</h2>
				<div>dans cette spécialité, vous allez travaillez blablabla</div>
				<h2>les metiers</h2>
				<div>blametier bla</div>
				<h2>programme</h2>
				<div>blabla programme</div>
				</section>
			';
		}
         		
		?>

	</body>
</html>