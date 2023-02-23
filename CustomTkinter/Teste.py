import customtkinter as ctk

janela = ctk.CTk()
janela.title('Sistema de Registro de Ponto')
janela.geometry('400x500')
janela._set_appearance_mode('dark')

matriculas = [11, 22, 33, 44, 55]


def validacao():
    if matricula.get() and senha.get() != '':
        aviso.configure(text='')
    elif matricula.get() == '':
        aviso.configure(text="DIGITE UMA MATRICULA", text_color='RED', width=250, height=10)
    elif senha.get() == '':
        aviso.configure(text="DIGITE A SENHA", text_color='RED', width=250, height=10)
    janela.mainloop()


texto = ctk.CTkLabel(janela, text='Registro de Ponto', font=('arial', 24), width=250)
texto.pack(padx=5, pady=5)

aviso = ctk.CTkLabel(janela, text='', width=0, height=0, font=('arial', 20))
aviso.pack(padx=5, pady=5)

matricula = ctk.CTkEntry(janela, placeholder_text='Digite Sua Matricula', font=('arial', 20), width=250)
matricula.pack(padx=5, pady=5)

senha = ctk.CTkEntry(janela, placeholder_text='Digite Sua Senha', font=('arial', 20), width=250)
senha.pack(padx=5, pady=5)

botao = ctk.CTkButton(janela, text='Registrar', corner_radius=50, command=validacao, font=('arial', 20), width=250)
botao.pack(padx=5, pady=5)

janela.mainloop()
