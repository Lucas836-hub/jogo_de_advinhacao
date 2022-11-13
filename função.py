
#criado por Lucas gabriel
# github : github.com/Lucas836
# instagra : @lucas_git

from random import randint
import os

#	topicos e palavras

animais=["leão","jacare","cobra","lagartixa"]
escola=["professor","livro","aluno","cantina","carteiras", "quadros", "alunos","faxineiros", "bibliotecarios", "diretores","cordenadores"]

shopping =["lojas","pessoas","objetos" ,"roupas","banhero","cinema", "brinquedos","praças-de-alimentação" ,"logistas"]

comercio=["lojas", "comerciantes","produtos", "objetos", "frutas"]
frutas =["Maçãs","pera","abacaxi","acerola", "banana","melancia","graviola","jaca","damasco","manga","uvas","kiwi","caja","caju","pitomba","morango","amora"]

#	palavra sorteada

keyword=[]

def tema():
	global keyword
	t =randint(1,5)
	
	if(t == 1):
		print("\033[4mO tema é : animais\033[m".center(70),"\n")
		word=randint(0,len(animais)-1)
		lock(animais[word])
		keyword=list(animais[word])
	
	if(t == 2):
		print("\033[4mO tema é : escola\033[m".center(70),"\n")
		word=randint(0,len(escola)-1)
		lock(escola[word])
		keyword=list(escola[word])
		
	if(t == 3):
		print("\033[4mO tema é : shopping \033[m".center(70),"\n")
		word=randint(0,len(shopping)-1)
		lock(shopping [word])
		keyword=list(shopping[word])
		
	if(t == 4):
		print("\033[4mO tema é : comercio\033[m".center(70),"\n")
		word=randint(0,len(comercio)-1)
		lock(comercio[word])
		keyword=list(comercio[word])
	
	if(t == 5):
		print("\033[4mO tema é : frutas\033[m".center(70),"\n")
		word=randint(0,len(frutas)-1)
		lock(frutas[word])
		keyword=list(frutas[word])
		

#	criptografia

cript=[]
def lock(a):
	for c in range(0,len(a)):
		if( "-" in a):
			cript.append("-")
		else:
			cript.append(" _ ")
		
		
def usuario_resp():
	for q in range(0,len(keyword)):
		print(cript[q],end="")
	print("\n")
	while True:
		resp =input("Digite a letra : ").lower().strip()
		
		if(len(resp) == 1):
			break
		else:
			continue

	if(resp in keyword):
		resp

		subst(resp)
	else :
		print("\n\033[33mQue pena não tem essa letra:( \033[m\n")

	

def subst(a):
		
	resp=a
	global cript
	global keyword
	global verificar
	
	for cont in range(0,len(keyword)):
		if(resp in keyword[cont]):
			if(resp == keyword[cont] and resp == cript[cont]):
				print("\033[33m Preste mais atencao essa letra já foi :/\033[m")
			else:
				cript[cont]=resp
				if(resp == "a"):
					if(cript[cont] == "ã"):
						cript[cont]="ã"
				if(resp == "c"):
					if(cript[cont] == "ç"):
						cript[cont]="ç"
				if(resp == "e"):
					if(cript[cont] == "é"):
						cript[cont]="é"
				verificar += 1
			

verificar=0											
def play_again():								
	try: 
		 tema()
	except:
		print("")

	tentar=len(keyword)+5
	while (tentar > 0):
		print(f"\nvoce tem {tentar} tentativas")
		usuario_resp()
		tentar-=1
	
		if(verificar == len(keyword)):
			print("\033[36m\n\nParabens voce conseguiu :)\033[m")
			print("\nA palavra era : ",end="")
			for q in range(0,len(keyword)):
				print(cript[q],end="")
			print("\n")
			break
		
		if(tentar == 0):
			print("\033[33m\n\nQue pena voce não conseguiu :(\033[m")
			print("Mas a palavra era : ",end="")
			for x in range(0,len(keyword)):
				print(keyword[x],end="")
			print("\n")
					
		try:
			os.System("clear")
		except:
			continue
again="s"
while (again == "s"):
	play_again()
	while True:
		again=input("Você quer jogar novamente ? ").strip().lower().replace("sim","s").replace("ss","s").replace("nao","n").replace("não","n").replace("nn","n")
		if(again == "s" or again == "n"):
			break
	for limp in range(0,len(keyword)):
		del keyword[0]
		del cript[0]
	verificar=0