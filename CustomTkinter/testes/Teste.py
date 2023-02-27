import customtkinter as ctk

janela = ctk.CTk()
janela.title('Sistema de Registro de Ponto')
janela.geometry('400x500')
janela._set_appearance_mode('dark')

def validacao():
    if matricula.get().isdigit():
        return aviso.configure(text="MATRICULA NÃO DEVE CONTER LETRAS OU PONTOS", text_color='RED', width=250, height=40, font=('arial', 15))
    if matricula.get() == '':
        return aviso.configure(text="DIGITE UMA MATRICULA", text_color='RED', width=250, height=40)
    if senha.get() == '':
        return aviso.configure(text="DIGITE A SENHA", text_color='RED', width=250, height=40)
    if matricula.get() and senha.get() != '':
        return aviso.configure(text='')


texto = ctk.CTkLabel(janela, text='Registro de Ponto', font=('arial', 40), width=250, height=40)
texto.pack(padx=5, pady=5)

aviso = ctk.CTkLabel(janela, text='', width=0, height=0, font=('arial', 20))
aviso.pack(padx=0, pady=0)

matricula = ctk.CTkEntry(janela, placeholder_text='Digite Sua Matricula', font=('arial', 20), width=250, height=40)
matricula.pack(padx=5, pady=5)

senha = ctk.CTkEntry(janela, placeholder_text='Digite Sua Senha', font=('arial', 20), width=250, height=40)
senha.pack(padx=5, pady=5)

botao = ctk.CTkButton(janela, text='Registrar', corner_radius=50, command=validacao, font=('arial', 20), width=250, height=40)
botao.pack(padx=5, pady=5)

janela.mainloop()
