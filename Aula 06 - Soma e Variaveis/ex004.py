n1 = input("Digite um valor: ")
print(type(n1))
n2 = str(input("Digite um valor: "))
print(type(n2))
n3 = int(input("Digite um valor: "))
print(type(n3))
n4 = float(input("Digite um valor: "))
print(type(n4))
n5 = bool(input("Digite um valor: "))
print(type(n5))

print("A primeiro valor")
print("É um numero ", n1.isnumeric())
print("É um numero e texto ", n1.isalnum())
print("É um decimal ",n1.isdecimal())
print("É um texto ", n1.isalpha())
print("É um digito ", n1.isdigit())
print("É uma palavra sem espaço", n1.isidentifier())
print("É tudo caixa baixa ", n1.islower())
print("É um impresso na tela ", n1.isprintable())
print("É tudo caixa alta ", n1.isupper())
print("É um capitalizada(primeira letra em maiusculo) ", n1.istitle())
print("É um espaço ", n1.isspace())
