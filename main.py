import csv
import json
import pandas as pd

def exibir_menu():
  print("\n----------------------------------------")
  print("Escolha uma opção: ")
  print("1 - Adicionar peril")
  print("2 - Calcula idade média")
  print("3 - Adcionar perfil com informações complementares")
  print("4 - Filtra por ano de nascimento")
  print("5 - Top 5 perfis marcados como amigos")
  print("6 - Lista amigos exclusivos")
  print("12 - Encerrar escolha de opções")
  
def solicita_informacoes_usuario():
    """
    Solicita informações do usuário
    
    Retorna:
    novo_usurio (dict): retorna um dicionario com as informações do usuário
    """
    nome = solicita_nome()
    idade = solicita_numero("Digite a idade do usuário: ")
    cidade = solicita_cidade()
    estado = solicita_estado()
    novo_usuario = {"nome": nome, "idade": str(idade), "cidade": cidade, "estado": estado, "amigos":"Sem amigos cadastrados"}
    return novo_usuario

def solicita_informacoes_adcionais():
    hobbies = solicita_elementos('um hobby')
    coding = solicita_elementos('uma linguagem de programação') 
    jogos = solicita_jogos()
    informacoes_adicionais = {"hobbies": hobbies, "coding": coding, "jogos": jogos}
    return informacoes_adicionais

def solicita_elementos(campo_requerido):
    elementos = []
    while True:
        elemento = solicita_string(campo_requerido)
        elementos.append(elemento)
        
        while True:
            continuar = input(f"Deseja continuar inserindo {campo_requerido}? ('s' para sim, 'n' para não): ").strip().lower()
            if continuar in ('s', 'n'):
                break
            print("Opção inválida, Responda com 's' ou com 'n'.")
        
        if continuar == 'n':
            break
    return elementos
        
def solicita_jogos():
    jogos = []
    while True:
        jogo = solicita_string('um jogo')
        plataforma = solicita_string('a plataforma')
        jogos.append((jogo, plataforma))
        
        while True:
            continuar = input(f"Deseja inserir outro jogo? ('s' para sim, 'n' para não): ").strip().lower()
            if continuar in ('s', 'n'):
                break
            print("Opção inválida, Responda com 's' ou com 'n'.")
        
        if continuar == 'n':
            break
    return jogos       

def valida_nome(valor):
    return valor.isalpha() and len(valor.strip()) >= 3

def solicita_nome():
    """
    Solicita nome do usuário
    
    Retorna:
    nome(str): nome do usuário
    """
    while True: 
        nome = input("Digite o nome do perfil: ").strip().title()
        if valida_nome(nome):
            return nome
        else:
            print("Campo deve ter no mínimo 3 caracteres e deve ser composto apenas por letras!")
  

def solicita_numero(mensagem):
  while True:
    valor_inserido = input(mensagem)
    try:
      numero = int(valor_inserido)
      return numero
    except ValueError:
      print("Valor inválido, por favor, digite um número.")
      
def valida_estado(valor):
    """
    Retorna True se o valor seguir o padrão ou false caso não
    
    Parâmetros:
    valor(str): valor inserido
    """
    return valor.isalpha() and len(valor.strip()) == 2

def solicita_estado():
    """
    Solicita estado do usuário
    
    Retorna:
    estado.upper() (str): sigla do estado em maiúsculo
    """
    while True: 
        estado = input("Digite a sigla do estado do usuário: ").strip()
        if valida_estado(estado):
            return estado.upper()
        else:
            print("Valor inválido, Insira apenas duas letras para a sigla do estado (ex: SP, RJ, MG).")
        
def valida_string(valor_inserido):
    return len(valor_inserido.strip()) >= 2      
        
def solicita_string(campo_requerido):
     while True: 
        string = input(f"Digite {campo_requerido}: ").strip().title()
        if valida_string(string):
            return string.title()
        else:
            print("Deve conter no mínimo 2 caracteres!")

def valida_cidade(valor_inserido):
    return len(valor_inserido.strip()) >= 3    
        
def solicita_cidade():
     while True: 
        cidade = input(f"Digite o nome da cidade do usuário: ").strip()
        if valida_cidade(cidade):
            return cidade.title()
        else:
            print("Deve conter no mínimo 3 caracteres e ser composta apenas por letras!")

def le_arquivo_txt(arquivo):
    """
    Lê um arquivo txt
    
    Parâmetros:
    arquivo(str): nome do arquivo
    
    Retorna:
    lista_de_perfis (list): lista de perfis, onde cada perfil é uma string
    """
    with open(arquivo, 'r', encoding='utf-8') as arquivo_txt:
        lista_de_perfis = []
        perfis = arquivo_txt.readlines()
        for perfil in perfis:
            lista_de_perfis.append(perfil.strip())
        return lista_de_perfis
        
def converte_para_csv(lista, arquivo):
    """
    Escreve em um csv informações a partir de uma lista de string
    
    Parâmetros:
    lista (list): lista de string, onde cada perfil é uma string
    arquivo (str): nome do arquivo
    
    Retorna:
    Escreve as informações no arquivo passado
    """
    header = ['nome', 'idade', 'cidade', 'estado', 'amigos']
    dados = []
    for perfil in lista:
        perfil_dividido = perfil.split(",", 4)
        nome = perfil_dividido[0].split(": ")[1] #pegar o valor do nome
        idade = perfil_dividido[1].split(": ")[1]
        cidade = perfil_dividido[2].split(": ")[1]
        estado = perfil_dividido[3].split(": ")[1]
        amigos = perfil_dividido[4].split(": ")[1]
        dados.append([nome, idade, cidade, estado, amigos])
    
    with open(arquivo, 'w', encoding='utf-8') as arquivo_csv:
        writer = csv.writer(arquivo_csv)
        writer.writerow(header)
        writer.writerows(dados)
        
def csv_para_dicionario(arquivo_em_csv):
    perfis = []
    with open(arquivo_em_csv, 'r', encoding='utf-8') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv)
        for linha in leitor:
            perfis.append(linha)
    return perfis
        
def atualiza_json(perfis, arquivo_em_json):
    """
    Lê um arquivo em csv e transforma em json
    
    Parâmetros:
    arquivo_em_csv(str): nome do arquivo csv
    arquivo_em_json(str): nome do arquivo json
    
    Retorna:
    Escreve as informações no arquivo json
    """ 
        
    with open(arquivo_em_json, 'w', encoding='utf-8') as arquivo_json:
        json.dump(perfis, arquivo_json, ensure_ascii=False, indent=4)
        
def leitura_novos_usuarios(arquivo):
    novos_perfis = []
    with open(arquivo, 'r', encoding='utf-8') as arquivo_csv:
        leitor = csv.DictReader(arquivo_csv, delimiter=';')
        for linha in leitor:
            novos_perfis.append(linha)   
    return novos_perfis

def formata_novos_perfis(perfis):
    perfis_campo_unificado = []
    for perfil in perfis:
        id = perfil["id"]
        nome = perfil['nome'] + " " + perfil["sobrenome"]
        email = perfil['email']
        idade = perfil['idade']
        data_nascimento = perfil['data de nascimento']
        cidade = perfil['cidade']
        estado = perfil['estado']
        amigos = []
        hobbies = perfil['hobbies']
        coding = perfil['linguagens de programação']
        jogos = perfil['jogos']
        perfis_campo_unificado.append({
            'id': id,
            'nome': nome,
            'email': email,
            'idade': idade,
            'data_de_nascimento': data_nascimento,
            'cidade': cidade,
            'estado': estado,
            'amigos': amigos,
            'hobbies': hobbies,
            'coding': coding,
            'jogos': jogos
        })
    return perfis_campo_unificado
        
def formata_perfis(perfis):
    perfis_formatados = []
    for perfil in perfis:
        id = ''
        nome = perfil['nome']
        email = ''
        idade = perfil['idade']
        data_nascimento = ''
        cidade = perfil['cidade']
        estado = perfil['estado']
        amigos = perfil['amigos']
        hobbies = []
        coding = []
        jogos = []
        perfis_formatados.append({
            'id': id,
            'nome': nome,
            'email': email,
            'idade': idade,
            'data_de_nascimento': data_nascimento,
            'cidade': cidade,
            'estado': estado,
            'amigos': amigos,
            'hobbies': hobbies,
            'coding': coding,
            'jogos': jogos
        })
    return perfis_formatados
    
def filtra_por_nascimento(df, ano):
    usurios_por_ano_nascimento = df[df['ano_nascimento'] == int(ano)]
    return usurios_por_ano_nascimento
        
lista_perfis = le_arquivo_txt('rede_infnet.txt') #salva em uma lista, onde cada elemento é uma string
converte_para_csv(lista_perfis, 'rede_infnet.csv') #converte a lista em um csv
perfis = csv_para_dicionario('rede_infnet.csv') #converte o csv em um dicionario
atualiza_json(perfis, 'rede_infnet.json')  #escreve no arquivo json

novos_perfis = leitura_novos_usuarios('dados_usuarios_novos.txt')    
novos_perfis_formatado = formata_novos_perfis(novos_perfis)   

perfis_formatado = formata_perfis(perfis)
lista_unificada = perfis_formatado + novos_perfis_formatado 

df_unificado = pd.DataFrame(lista_unificada)
df_unificado['idade'] = pd.to_numeric(df_unificado['idade'], errors='coerce').astype('Int64') #conversão do campo foi utiilizado chatgpt
df_unificado['ano_nascimento'] = 2024 - df_unificado['idade']

#preenche os valores vazios com a média das outras idades
media_de_idade = df_unificado['idade'].mean()
df_unificado['idade'] = df_unificado['idade'].astype('Float64')
df_unificado['idade'] = df_unificado['idade'].fillna(media_de_idade)
df_unificado['idade'] = df_unificado['idade'].round(0)

# print(df_unificado.to_string(index=False))

usuarios_sp = df_unificado[df_unificado['estado'] == 'SP']
usuarios_mg = df_unificado[df_unificado['estado'] == 'MG']
usuarios_rj = df_unificado[df_unificado['estado'] == 'RJ']

usuarios_mg.to_csv('grupo_mg.csv', index=False, encoding='utf-8')
usuarios_sp.to_csv('grupo_sp.csv', index=False, encoding='utf-8')
usuarios_rj.to_csv('grupo_rj.csv', index=False, encoding='utf-8')

#transforma o data frame em um dicionário para converter para json
lista_de_dicionarios = df_unificado.to_dict(orient='records')
atualiza_json(lista_de_dicionarios, 'INFwebNet_Data.json') 

while True:
   exibir_menu()
   opcao = input("\nDigite o número da opção escolhida: ").lower().strip()
   if opcao == "1":
    novo_perfil = solicita_informacoes_usuario()
    perfis.append(novo_perfil)
    atualiza_json(perfis, 'rede_infnet.json')
    
   elif opcao == "2":
    df_novo = pd.read_json('rede_infnet.json')
    media_idade = round(df_novo['idade'].mean(), 2)
    print(f"A média de idade dos usuários da rede social é de : {media_idade}")
    
   elif opcao == "3":
    novo_perfil = solicita_informacoes_usuario()
    dados_complementares  = solicita_informacoes_adcionais()
    novo_perfil.update(dados_complementares)
    perfis.append(novo_perfil)
    atualiza_json(perfis, 'rede_infnet.json')
    
   elif opcao == "4":
    ano = input("Digite um ano para ser filtrado: ").strip()
    usuarios_filtrados = filtra_por_nascimento(df_unificado, ano)
    print(usuarios_filtrados)
    
   elif opcao == "5":
    pass
        
   elif opcao == "6":
    pass
   
   elif opcao == "12":
    print("\nMenu encerrado!")
    break
   else:
       
    print("\nEscolha errada, tente novamente!\n")
