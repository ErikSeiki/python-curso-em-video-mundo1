n = str(input("Digite o seu nome completo: "))
print("Seu nome com todas as letras maiusculas: {}".format(n.upper()))
print("Seu nome com todas as letras minusculas: {}".format(n.lower()))
print("Você tem {} letras no seu nome completo".format(len("".join(n.split()))))
nn = n.split()
print("Seu primeiro nome é {} e tem {} letras no seu primeiro nome".format(nn[0], len(nn[0])))

n1 = str(input("Digite o seu nome completo: ")).strip()
print("Seu nome com todas as letras maiusculas: {}".format(n1.upper()))
print("Seu nome com todas as letras minusculas: {}".format(n1.lower()))
print("Você tem {} letras no seu nome completo".format(len(n1) - n1.count(" ")))
print("Seu primeiro nome tem {}".format(n.find(" ")))
