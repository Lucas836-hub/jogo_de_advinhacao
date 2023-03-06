
#criado por Lucas gabriel
# github : https://github.com/Lucas836-hub/
# instagra : @lucas_git

from random import randint
import os
import update_file # CHAMANDO O ATUALIZADOR

#	topicos e palavras
class jogar:
	def __init__(self):
		#     temas [[[titulo],[elementos]]]
		self.temas=[[["Animais"],["leão","jacare","cobra","lagartixa"]],\
		[["Escola"],["professor","livro","aluno","cantina","carteiras", "quadros", "alunos","faxineiros", "bibliotecarios", "diretores","cordenadores"]],\
		[["Shopping"],["lojas","pessoas","objetos" ,"roupas","banhero","cinema", "brinquedos","praças-de-alimentação" ,"logistas"]],\
		[["Comercio"],["lojas", "comerciantes","produtos", "objetos", "frutas"]],\
		[["Frutas"],["maçãs","pera","abacaxi","acerola", "banana","melancia","graviola","jaca","damasco","manga","uvas","kiwi","caja","caju","pitomba","morango","amora"]]]

		self.keyword=[]
		self.cript = []
		self.verificar=0
		self.tentar=0
		self.replay=False

		self.play_again()

	def tema(self):
		t =randint(1,len(self.temas))
		t-=1

		print(f"\033[4mO tema é : {self.temas[t][0][0]}\033[m".center(70), "\n")
		word = randint(0, len(self.temas[t][1]) - 1)
		self.lock(self.temas[t][1][word])
		self.keyword = list(self.temas[t][1][word])


	def lock(self,a):
		# meio que criptografa as letras em traços
		for c in range(0,len(a)):
			if( "-" in a):
				self.cript.append("-")
			else:
				self.cript.append(" _ ")
		
		
	def usuario_resp(self):
		# recebe a letra digitada pelo usuario e verifica se tem na palavra
		for q in range(0,len(self.keyword)):
			print(self.cript[q],end="")
		print("\n")
		while True:
			resp =input("Digite a letra : ").lower().strip()
		
			if(len(resp) == 1):
				break
			else:
				continue

		if(resp in self.keyword):
			resp
			self.subst(resp)
		else :
			print("\n\033[33mQue pena não tem essa letra:( \033[m\n")

	

	def subst(self,a):

		resp=a
		J_PRIN=False
		for cont in range(0,len(self.keyword)):
			if(resp in self.keyword[cont]):
				if(resp == self.keyword[cont] and resp == self.cript[cont] and not J_PRIN):
					print("\033[33m Preste mais atencao essa letra já foi :/\033[m")
					J_PRIN = True
				else:
					self.cript[cont]=resp
					if(resp == "a"):
						if(self.cript[cont] == "ã"):
							self.cript[cont]="ã"
					if(resp == "c"):
						if(self.cript[cont] == "ç"):
							self.cript[cont]="ç"
					if(resp == "e"):
						if(self.cript[cont] == "é"):
							self.cript[cont]="é"
					self.verificar += 1
			


	def play_again(self):

		try:
			if update_file.check_atualizacao("https://github.com/Lucas836-hub/jogo_de_advinhacao"):
				# ATUALIZANDO O SCRIPT LOCAL
				update_file.atualizar("https://github.com/Lucas836-hub/jogo_de_advinhacao")
				print("\033[32mvai atualizar\033[m")
			else:
				print("\033[31mnao vai atualizar\033[m")
		except:
			pass
		print("ta rodando")
		try:
			 self.tema()
		except:
			print("")

		self.tentar=len(self.keyword)+5
		while (self.tentar > 0):
			print(f"\nvoce tem {self.tentar} tentativas")
			self.usuario_resp()
			self.tentar-=1


			if(self.verificar == len(self.keyword)):
				print("\033[36m\n\nParabens voce conseguiu :)\033[m")
				print("\nA palavra era : ",end="")
				for q in range(0,len(self.keyword)):
					print(self.cript[q],end="")
				print("\n")
				self.jogar_novamente()
		
			if(self.tentar == 0):
				print("\033[33m\n\nQue pena voce não conseguiu :(\033[m")
				print("Mas a palavra era : ",end="")
				for x in range(0,len(self.keyword)):
					print(self.keyword[x],end="")
				print("\n")
				self.jogar_novamente()

			self.limp()


	def jogar_novamente(self):
		while True:
			again = input("Você quer jogar novamente ? ").strip().lower().replace("sim", "s").replace("ss", "s").replace(
			"nao", "n").replace("não", "n").replace("nn", "n")
			if (again == "s"):
				self.replay=True
				break
			if(again == "n"):
				break

			else:
				print("\033[31mERRO RESPOSTA INVÁLIDA !!!\033[m")
		if self.replay:
			jogar()
		else:
			exit()


	def plataforma(self):
		import platform
		return platform.system()
	def limp(self):
		s = self.plataforma()

		if s == "Linux":
			os.system("clear")

		if s == "Windows":
			os.system("cls")

		if s == "Darwin":
			os.system("clear")


jogar()
