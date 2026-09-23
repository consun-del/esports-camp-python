import tkinter as tk

usuario_logado = None

banco_de_dados = {
    "admin": {"senha": "admin123", "cargo": "administrador"},
    "jogador1": {"senha": "jogador123", "cargo": "jogador"}
}

lista_participantes = []

def limpar_janela():     
    elementos = app.winfo_children()
    
    for item in elementos:
        item.destroy()

def criar_botao_limpar(tela_atual):
    if tela_atual != "menu":
        botao_retornar_menu = tk.Button(app, text="Retornar ao Menu", command=abrir_menu, font=("Helvetica", 10, "bold"), bg="#555555", fg="white")
        botao_retornar_menu.pack(pady=(20, 20))
    else:
        botao_sair = tk.Button(app, text="Trocar Usuário", command=tela_login, font=("Helvetica", 10, "bold"), bg="#555555", fg="white")
        botao_sair.pack(pady=(20, 20))

def validar_login():
    global usuario_logado, label_mensagem_erro

    user_digitado = entrada_usuario.get()
    senha_digitada = entrada_senha.get()

    if user_digitado in banco_de_dados:
        senha_verdadeira = banco_de_dados[user_digitado]["senha"]

        if senha_digitada == senha_verdadeira:
            usuario_logado = user_digitado
            abrir_menu()
        else:
            label_mensagem_erro.config(text="Usuário ou Senha incorretos. Tente novamente.")
    else:
        label_mensagem_erro.config(text="Usuário ou Senha incorretos. Tente novamente.")

def cadastrar_participante():
    global lista_participantes

    nome = entrada_nome_participante.get()
    nickname = entrada_nickname_participante.get()
    idade = entrada_idade_participante.get()
    altura = entrada_altura_participante.get()
    matricula = entrada_matricula_participante.get()
    horas = entrada_horas_participante.get()
    campeonatos = entrada_campeonatos_participante.get()
    computador_booleano = var_computador.get()

    idade_convertida = int(idade)
    altura_convertida = float(altura)
    horas_convertidas = float(horas)
    campeonatos_convertidos = int(campeonatos)

    participante = {
        "nome": nome,
        "nickname": nickname,
        "idade": idade_convertida,
        "altura": altura_convertida,
        "matricula": matricula,
        "horas": horas_convertidas,
        "campeonatos": campeonatos_convertidos,
        "computador": computador_booleano
    }

    lista_participantes.append(participante)

    label_mensagem_sucesso = tk.Label(app, text="Participante Cadastrado com Sucesso!", fg="#00ff00", bg="black", font=("Helvetica", 12, "bold"))
    label_mensagem_sucesso.pack(pady=15)

def tela_login():
    global entrada_usuario, entrada_senha, label_mensagem_erro

    limpar_janela()
    
    label01 = tk.Label(app, text="E-SPORTS CAMP", bg="black", fg="white", font=("Helvetica", 24, "bold"))
    label01.pack(pady=(60, 40))
    
    label02 = tk.Label(app, text="Nome de Usuário:", bg="black", fg="white", font=("Helvetica", 12))
    label02.pack(pady=(10, 0))
    
    entrada_usuario = tk.Entry(app, bg="#333333", fg="white", insertbackground="white", font=("Helvetica", 12))
    entrada_usuario.pack(pady=(5, 20))
    
    label03 = tk.Label(app, text="Insira a Senha:", bg="black", fg="white", font=("Helvetica", 12))
    label03.pack(pady=(10, 0))
    
    entrada_senha = tk.Entry(app, show="*", bg="#333333", fg="white", insertbackground="white", font=("Helvetica", 12))
    entrada_senha.pack(pady=(5, 30))
    
    botao_entrada = tk.Button(app, text="Entrar", command=validar_login, font=("Helvetica", 12, "bold"), width=15, bg="#0055ff", fg="white")
    botao_entrada.pack(pady=10)

    label_mensagem_erro = tk.Label(app, text="", bg="black", fg="#ff4444", font=("Helvetica", 10))
    label_mensagem_erro.pack(pady=(10, 0))

def abrir_menu():
    limpar_janela()
    cargo_usuario = banco_de_dados[usuario_logado]["cargo"]

    if cargo_usuario == "administrador":
        text_01 = tk.Label(app, text="PAINEL DO ADMINISTRADOR", bg="black", fg="white", font=("Helvetica", 18, "bold"))
        text_01.pack(pady=(50, 30))
    
        botao_cadastrar = tk.Button(app, text="Cadastrar Jogador", command=janela_cadastrar, font=("Helvetica", 12), width=25, bg="#333333", fg="white")
        botao_cadastrar.pack(pady=10)
    
        botao_acessarcadastro = tk.Button(app, text="Acessar Fichas", command=acessar_cadastro, font=("Helvetica", 12), width=25, bg="#333333", fg="white")
        botao_acessarcadastro.pack(pady=10)
        
        botao_participantes = tk.Button(app, text="Lista de Participantes", command=acessar_participantes, font=("Helvetica", 12), width=25, bg="#333333", fg="white")
        botao_participantes.pack(pady=10)

    else:
        text_01 = tk.Label(app, text="PORTAL DO JOGADOR", bg="black", fg="white", font=("Helvetica", 18, "bold"))
        text_01.pack(pady=(50, 30))

        botao_cadastrar = tk.Button(app, text="Realizar Cadastro", command=janela_cadastrar, font=("Helvetica", 12), width=25, bg="#333333", fg="white")
        botao_cadastrar.pack(pady=10)
    
    criar_botao_limpar("menu")

def janela_cadastrar():
    global entrada_nome_participante, entrada_nickname_participante, entrada_idade_participante, entrada_altura_participante, entrada_matricula_participante, entrada_horas_participante, entrada_campeonatos_participante, var_computador

    var_computador = tk.BooleanVar()

    limpar_janela()
    
    label_titulo = tk.Label(app, text="FICHA DE INSCRIÇÃO", bg="black", fg="white", font=("Helvetica", 16, "bold"))
    label_titulo.pack(pady=(20, 20))
    
    linha1 = tk.Frame(app, bg="black")
    linha1.pack(pady=5)
    tk.Label(linha1, text="Nome do Participante:", bg="black", fg="white", width=35, anchor="e").pack(side=tk.LEFT, padx=5)
    entrada_nome_participante = tk.Entry(linha1, bg="#333333", fg="white", insertbackground="white", width=30)
    entrada_nome_participante.pack(side=tk.LEFT, padx=5)

    linha2 = tk.Frame(app, bg="black")
    linha2.pack(pady=5)
    tk.Label(linha2, text="Nickname do Participante:", bg="black", fg="white", width=35, anchor="e").pack(side=tk.LEFT, padx=5)
    entrada_nickname_participante = tk.Entry(linha2, bg="#333333", fg="white", insertbackground="white", width=30)
    entrada_nickname_participante.pack(side=tk.LEFT, padx=5)

    linha3 = tk.Frame(app, bg="black")
    linha3.pack(pady=5)
    tk.Label(linha3, text="Idade do Participante:", bg="black", fg="white", width=35, anchor="e").pack(side=tk.LEFT, padx=5)
    entrada_idade_participante = tk.Entry(linha3, bg="#333333", fg="white", insertbackground="white", width=30)
    entrada_idade_participante.pack(side=tk.LEFT, padx=5)

    linha4 = tk.Frame(app, bg="black")
    linha4.pack(pady=5)
    tk.Label(linha4, text="Altura (ex: 1.75):", bg="black", fg="white", width=35, anchor="e").pack(side=tk.LEFT, padx=5)
    entrada_altura_participante = tk.Entry(linha4, bg="#333333", fg="white", insertbackground="white", width=30)
    entrada_altura_participante.pack(side=tk.LEFT, padx=5)

    linha5 = tk.Frame(app, bg="black")
    linha5.pack(pady=5)
    tk.Label(linha5, text="Número da Matrícula:", bg="black", fg="white", width=35, anchor="e").pack(side=tk.LEFT, padx=5)
    entrada_matricula_participante = tk.Entry(linha5, bg="#333333", fg="white", insertbackground="white", width=30)
    entrada_matricula_participante.pack(side=tk.LEFT, padx=5)

    linha6 = tk.Frame(app, bg="black")
    linha6.pack(pady=5)
    tk.Label(linha6, text="Média de Horas Jogadas (Semana):", bg="black", fg="white", width=35, anchor="e").pack(side=tk.LEFT, padx=5)
    entrada_horas_participante = tk.Entry(linha6, bg="#333333", fg="white", insertbackground="white", width=30)
    entrada_horas_participante.pack(side=tk.LEFT, padx=5)

    linha7 = tk.Frame(app, bg="black")
    linha7.pack(pady=5)
    tk.Label(linha7, text="Número de Campeonatos já Participados:", bg="black", fg="white", width=35, anchor="e").pack(side=tk.LEFT, padx=5)
    entrada_campeonatos_participante = tk.Entry(linha7, bg="#333333", fg="white", insertbackground="white", width=30)
    entrada_campeonatos_participante.pack(side=tk.LEFT, padx=5)

    linha8 = tk.Frame(app, bg="black")
    linha8.pack(pady=5)
    tk.Label(linha8, text="Possui Computador próprio?:", bg="black", fg="white", width=35, anchor="e").pack(side=tk.LEFT, padx=5)
    tk.Radiobutton(linha8, text="Sim", variable=var_computador, value=True, bg="black", fg="#00ff00", selectcolor="black").pack(side=tk.LEFT, padx=5)
    tk.Radiobutton(linha8, text="Não", variable=var_computador, value=False, bg="black", fg="#ff4444", selectcolor="black").pack(side=tk.LEFT, padx=5)

    botao_cadastrar_participante = tk.Button(app, text="Salvar Cadastro", command=cadastrar_participante, bg="#0055ff", fg="white", font=("Helvetica", 10, "bold"), width=20)
    botao_cadastrar_participante.pack(pady=20)

    criar_botao_limpar("cadastrar")
    
def acessar_cadastro():
    limpar_janela()

    label = tk.Label(app, text="FICHAS CADASTRADAS", bg="black", fg="white", font=("Helvetica", 16, "bold"))
    label.pack(pady=25)
    
    for participante in lista_participantes:
        label = tk.Label(app, text=f"Dados do Participante {participante['nome']} atualizados com sucesso no terminal!", bg="black", fg="white", font=("Helvetica", 10))
        label.pack(pady=5)

        print("-" * 50)
        print(f"DADOS DO JOGADOR {participante['nome']}:")
        print(f"Nome: {participante['nome']} -> Tipo: {type(participante['nome'])}")
        print(f"Nickname: {participante['nickname']} -> Tipo: {type(participante['nickname'])}")
        print(f"Idade: {participante['idade']} -> Tipo: {type(participante['idade'])}")
        print(f"Altura: {participante['altura']} -> Tipo: {type(participante['altura'])}")
        print(f"Matrícula: {participante['matricula']} -> Tipo: {type(participante['matricula'])}") 
        print(f"Média de Horas Jogadas: {participante['horas']} -> Tipo: {type(participante['horas'])}")
        print(f"Número de Campeonatos: {participante['campeonatos']} -> Tipo: {type(participante['campeonatos'])}")
        print(f"Possui Computador Próprio: {participante['computador']} -> Tipo: {type(participante['computador'])}")
        print("-" * 50)

    criar_botao_limpar("acessarcadastro")

def acessar_participantes():
    limpar_janela()

    label = tk.Label(app, text="LISTA DE JOGADORES", bg="black", fg="white", font=("Helvetica", 16, "bold"))
    label.pack(pady=25)

    for participante in lista_participantes:

        label_info = tk.Label(app, text=f"Nome: {participante['nome']}, Nick: {participante['nickname']}", bg="black", fg="white", font=("Helvetica", 10))
        label_info.pack(pady=5)

    criar_botao_limpar("participantes")

app = tk.Tk()
app.geometry("800x600")
app.config(bg="black")
app.title("E-SPORTS CAMP")

tela_login()

app.mainloop()
