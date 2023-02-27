import datetime
import customtkinter as ctk

janela = ctk.CTk()
janela.title('Sistema de Registro de Ponto')
janela.geometry('500x600')
janela._set_appearance_mode('dark')

OPC = ['Entrada', 'Inicio Intervalo', 'Fim intervalo', 'Saida']


def call():
    n_matricula = matricula.get()
    n_senha = senha.get()
    t_opcao = opcoes.get()
    validacao(n_matricula, n_senha, t_opcao)


def validacao(n_matricula, n_senha, t_opcao):
    data = datetime.datetime.now().strftime('%d/%m/%Y')
    hora = datetime.datetime.now().strftime('%H:%M:%S')

    if n_matricula == '':
        return aviso.configure(text="MATRICULA VAZIA, DIGITE UM NUMERO", text_color='RED', width=300, height=40,
                               font=('arial', 15))
    if not (n_matricula.isnumeric()):
        return aviso.configure(text="MATRICULA INVALIDA, APENAS NUMEROS", text_color='RED', width=300, height=40,
                               font=('arial', 15))
    if n_senha == '':
        return aviso.configure(text="SENHA VAZIA, DIGITE A SENHA", text_color='RED', width=300, height=40,
                               font=('arial', 15))
    if n_matricula and n_senha != '':
        visualizacao.configure(
            text=f'Horario Registrado com sucesso\nMatricula: {n_matricula}\nData: {data}\nHora: {hora}\nRegistro: {t_opcao}'
            , font=('times bold', 28), width=400, height=200, bg_color='#000', text_color='white')
        visualizacao.pack(padx=20, pady=20)
        try:
            inserir = open('registro.txt', 'at', encoding='UTF-8')
        except:
            print('\033[31mERRO!\033[m: Não foi possivel abrir o arquivo!')
        else:
            try:
                inserir.write(f'Matricula: {n_matricula}; Data: {data}; Hora: {hora}; Opção: {t_opcao}\n')
            except:
                print('\033[31mERRO!\033[m: Não foi possivel inserir a informação!')
                inserir.close()
        aviso.configure(text="")


texto = ctk.CTkLabel(janela, text='Registro de Ponto', font=('arial', 40), width=300, height=40)
texto.pack(padx=5, pady=5)

aviso = ctk.CTkLabel(janela, text='', width=0, height=0, font=('arial', 20))
aviso.pack(padx=0, pady=0)

matricula = ctk.CTkEntry(janela, placeholder_text='Digite Sua Matricula', font=('arial', 20), width=300, height=40)
matricula.pack(padx=5, pady=5)

opcoes = ctk.CTkComboBox(janela, values=OPC, font=('arial', 20), width=300, height=40)
opcoes.pack(padx=5, pady=5)

senha = ctk.CTkEntry(janela, placeholder_text='Digite Sua Senha', font=('arial', 20), width=300, height=40)
senha.pack(padx=5, pady=5)

botao = ctk.CTkButton(janela, text='Registrar', corner_radius=50, command=call, font=('arial', 20), width=300, height=40)
botao.pack(padx=5, pady=5)

visualizacao = ctk.CTkLabel(janela, text=f'', font=('arial', 0), width=0, height=0)
visualizacao.pack()

janela.mainloop()
