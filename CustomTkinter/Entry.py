import customtkinter as ctk

altura = 400
largura = 320
alt_entry = round(altura/8)
larg_entry = round(largura/2)

janela = ctk.CTk()
janela.title('ENTRY')
janela.geometry(f'{altura}x{largura}')
janela._set_appearance_mode('SYSTEM')

entry1 = ctk.CTkEntry(master=janela, width=larg_entry, height=alt_entry, corner_radius=100, border_width=2, border_color='#0031F5',
                      font=('ARIAL', 12), text_color='#FFF', placeholder_text='DIGITE O TEXTO',
                      placeholder_text_color='#25E698')
entry1.pack(padx=5, pady=5)

entry2 = ctk.CTkEntry(master=janela, width=larg_entry, height=alt_entry, corner_radius=100, border_width=2, border_color='#0031F5',
                      font=('ARIAL', 12), text_color='#FFF', placeholder_text='COLOQUE A ALTURA DA JANELA',
                      placeholder_text_color='#25E698')
entry2.pack(padx=5, pady=5)

entry3 = ctk.CTkEntry(master=janela, width=larg_entry, height=alt_entry, corner_radius=100, border_width=2, border_color='#0031F5',
                      font=('ARIAL', 12), text_color='#FFF', placeholder_text='COLOQUE A LARGURA DA JANELA',
                      placeholder_text_color='#25E698')
entry3.pack(padx=5, pady=5)


def call():
    tamanho = f'{entry2.get()}x{entry3.get()}'
    altera(tamanho)


def altera(tamanho):
    janela.geometry(f'{tamanho}')


botao = ctk.CTkButton(master=janela, width=300, height=50, text='ALTERAR TAMANHO', command=call)
botao.pack(padx=10, pady=10)

janela.mainloop()
