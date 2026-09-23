import tkinter as tk

usuario_logado = None

banco_de_dados = {
    "admin": {"senha": "admin123", "cargo": "administrador"},
    "jogador1": {"senha": "jogador123", "cargo": "jogador"}
}

def limpar_janela():     
    elementos = app.winfo_children()
    
    for item in elementos:
        item.destroy()

def criar_botao_limpar(tela_atual):
    if tela_atual != "menu":
       
        botao_retornar_menu = tk.Button(app, text="Retornar ao Menu", command=abrir_menu)
        botao_retornar_menu.pack(pady=50)

def validar_login ():
    global usuario_logado

    user_digitado = entrada_usuario.get()
    senha_digitada = entrada_senha.get()

    if user_digitado in banco_de_dados:
        senha_verdadeira = banco_de_dados[user_digitado]["senha"]

        if senha_digitada == senha_verdadeira:
            usuario_logado = user_digitado
            abrir_menu()
        else:
            print("Senha incorreta!")
    else:
        print("Usuário não encontrado!")
    
def tela_login ():
    global entrada_usuario, entrada_senha

    limpar_janela()
    
    label01 = tk.Label(app, text="Bem-Vindo ao E-Sports Camp")
    label01.pack(pady=50)
    
    label02 = tk.Label(app, text="Nome de Usuário: ")
    label02.pack()
    
    entrada_usuario = tk.Entry(app)
    entrada_usuario.pack(pady=50)
    
    
    label03 = tk.Label(app, text="Insira a Senha: ")
    label03.pack()
    entrada_senha = tk.Entry(app, show="*")
    entrada_senha.pack(pady=50)
    
    botao_entrada = tk.Button(app, text="Entrar", command=validar_login)
    botao_entrada.pack(pady=50)


def abrir_menu():
    limpar_janela()
   
    text_01 = tk.Label(app, text="MENU DE SELEÇÃO")
    text_01.pack(pady=25)
    
    # Botão para cadastros
    botao_cadastrar = tk.Button(app, text="Cadastrar", command=janela_cadastrar)
    botao_cadastrar.pack(pady=25)
    
    # Botão para acessar um cadastro.
    botao_acessarcadastro = tk.Button(app, text="Acessar Cadastro", command=acessar_cadastro)
    botao_acessarcadastro.pack(pady=25)
    
    # Botão para acessar lista de participantes.
    botao_participantes = tk.Button(app, text="Acessar Participantes")
    botao_participantes.pack(pady=25)

    criar_botao_limpar("menu")

def janela_cadastrar():
    limpar_janela()
    
    label = tk.Label(app, text="ACESSAR CADASTRO")
    label.pack(pady=25)
    
    criar_botao_limpar("cadastrar")
    
def acessar_cadastro():
    limpar_janela()

    label = tk.Label(app, text="CADASTROS")
    label.pack(pady=25)
    
    criar_botao_limpar("acessarcadastro")

app = tk.Tk()
app.title("E-SPORTS CAMP")

tela_login()

app.mainloop()
