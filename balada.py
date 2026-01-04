# 1. PERGUNTAR (Input devolve sempre texto)
nome = input("Qual é o seu nome? ")
idade_texto = input("Qual é a sua idade? ")

# 2. CONVERTER (Transformar texto em número inteiro)
idade = int(idade_texto)

# 3. DECIDIR (Lógica Condicional)
if idade >= 18:
    print(f"Olá {nome}, podes entrar na festa! 🍺")
else:
    print(f"Desculpa {nome}, és menor de idade. Vai para casa estudar Python! 📚")