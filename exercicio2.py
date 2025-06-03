usuario_cadastrado = input("Digite o nome de usuário: ")
senha_cadastrada = input("Digite sua senha: ")

usuario_digitado = input("Digite o nome de usuário novamente: ")
senha_digitada = input("Digite sua senha novamente: ")

if usuario_digitado == usuario_cadastrado and senha_digitada == senha_cadastrada:
    print("Dados cadastrados com sucesso!")
else:
    print("Usuário ou senha incorretas, tente novamente!")