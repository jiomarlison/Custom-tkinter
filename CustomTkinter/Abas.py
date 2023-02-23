import customtkinter as ctk

janela = ctk.CTk()
janela.title('Teste de abas')
janela.geometry('700x700')
janela._set_appearance_mode('dark')
nome_abas = ['Dados Pessoais', 'Dados Institucionais', 'Dados de Registro Login']

nome = 'Mikael'
idade = 20
genero = 'M'
cidade = 'Petrolina'
estado = 'Pe'

aba = ctk.CTkTabview(janela, width=600, height=500, segmented_button_selected_color='Green', corner_radius=50)
aba.pack()

aba.add(nome_abas[0])
aba.add(nome_abas[1])
aba.add(nome_abas[2])

aba.tab(nome_abas[0]).grid_columnconfigure(0, weight=1)
aba.tab(nome_abas[1]).columnconfigure(0, weight=1)
aba.tab(nome_abas[2]).columnconfigure(0, weight=1)

pessoais = ctk.CTkLabel(aba.tab(nome_abas[0]),
                        text=f'Nome: {nome}\nIdade: {idade}\nGenero: {genero}\n Cidade: {cidade}\nEstado: {estado}',
                        font=('arial', 20), text_color='Teal')
pessoais.pack()

institucioais = ctk.CTkLabel(aba.tab(nome_abas[1]),
                             text='Nome da Instituição: FACAPE\nCurso: Ciências da computação\nTurno: Noturno\nMátricula: 112345',
                             font=('arial', 20), text_color='Teal')
institucioais.pack()

login = ctk.CTkLabel(aba.tab(nome_abas[2]),
                     text='Matricula: 112345\nSenha: 254187963',
                     font=('arial', 20), text_color='Teal')
login.pack()

janela.mainloop()
