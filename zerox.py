#Offical Version : v1 (Initial Release)
#Authour : https://github.com/qertyuiop12345678
#Minified : True
###############################################
print('\033[0;31;47m Red \n[!] Zerox Sniper Is Generating!')
print('\n[!] If Not Working, Contact: ! Godly Static#0880')
G=int
C=str
import requests as D
global E,A,B,F
E=1
H='https://polytoria.com/api/fetch/catalog/items?limit=99999999999999999999999999999999999999999999999999999999&page='+C(E)
A=0
F=D.get(H)
B=F.json()
def I():
	E='AssetID';global A
	for I in B:
		if B[A]['Limited']==True:
			F=D.get('https://polytoria.com/api/fetch/catalog/resellers?id='+C(B[A][E])+'&limit=4&offset=')
			for J in range(1):
				if G(F.json()[0]['price'])<1000:print(C(B[G(A)][E]));H=open('goodItems.txt','a');H.write('\n'+C(B[G(A)][E]))
		A=A+1
def J():A=I()
J()
