function sauvegarde()
{
	var a = document.getElementById("message").value;
	var requestURL = "../messagerie/meffasgerie.json";
	var request = new XMLHttpRequest();
	request.open('GET', requestURL);
	
}