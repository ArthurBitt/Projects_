import tkinter as tk
from tkinter import messagebox



class TriagemApp(tk.Tk):

    def __init__(self):

        numeroProcesso = None
        numeroCPF = None
        senhaPje = None

        super().__init__()

        Fonte = "Arial 15 bold"

        self.title("App Triagem")
        self.geometry("1080x720")
        self.config(background='#F0E68C')
        self.question_label = tk.Label(text="Qual o tipo de processo?", font="Arial 18 bold")
        self.question_label.place(x=410, y=220)
        self.question_label.config(background='#F0E68C')

        self.var_opcao = tk.StringVar(value="Opção1") # Variável de configuração que limita para apenas uma seleção de RadioButton
        self.option1 = tk.Radiobutton(text="Físico", variable=self.var_opcao, value="Opção1", font=Fonte)
        self.option1.config(bg='#F0E68C', activebackground='#F0E68C')
        self.option1.place(x=490, y=320)

        self.option2 = tk.Radiobutton(text="Digital", variable=self.var_opcao, value="Opção2", font=Fonte)
        self.option2.config(bg='#F0E68C', activebackground='#F0E68C')
        self.option2.place(x=490, y=380)

        self.submit_button = tk.Button(text="Próximo", font=Fonte, command=self.atualizarTela)
        self.submit_button.place(x=450, y=600, height=65, width=185)


    def limparTela(self):
        for widget in self.winfo_children():
            if isinstance(widget, tk.Label):
                widget.config(text="")
            elif isinstance(widget, tk.Radiobutton):
                widget.destroy()
            elif isinstance(widget, tk.Button):
                widget.destroy()
            elif isinstance(widget, tk.Entry):
                widget.destroy()

    def atualizarTela(self):
        opcao_selecionada = self.var_opcao.get()

        if opcao_selecionada == "Opção1":
            self.limparTela()
            #self.back_button.config(state=tk.NORMAL) # Ativa o botão voltar

            self.question_label = tk.Label(text="Informe o número de processo:", font="Arial 18 bold")
            self.question_label.place(x=390, y=125)
            self.question_label.config(background='#F0E68C')

            self.warning_label = tk.Label(text="Por gentileza, informe apenas os números no campo abaixo!", font="Helvetica 14")
            self.warning_label.place(x=330, y=50)
            self.warning_label.config(background='#F0E68C')

            self.numberProcess = tk.Entry()
            self.numberProcess.config(bg='#FFEFD5', bd=3, font='Helvetica 14', width=30)
            self.numberProcess.place(x=390, y=180)
            self.numberProcess.focus()

            self.question1_label = tk.Label(text="Login Pje:", font="Arial 18 bold")
            self.question1_label.place(x=390, y=250)
            self.question1_label.config(background='#F0E68C')

            self.question2_label = tk.Label(text="CPF:", font="Arial 18 bold")
            self.question2_label.place(x=390, y=290)
            self.question2_label.config(background='#F0E68C')

            self.numberCPF = tk.Entry()
            self.numberCPF.config(bg='#FFEFD5', bd=3, font='Helvetica 14', width=30)
            self.numberCPF.place(x=390, y=320)

            self.question3_label = tk.Label(text="Senha:", font="Arial 18 bold")
            self.question3_label.place(x=390, y=370)
            self.question3_label.config(background='#F0E68C')

            self.senhaPje = tk.Entry()
            self.senhaPje.config(bg='#FFEFD5', bd=3, font='Helvetica 14', width=30)
            self.senhaPje.place(x=390, y=400)


            self.next_button = tk.Button(text="Pesquisar", font='Arial 16 bold', command=self.realizar_triagem)
            self.next_button.place(x=450, y=520, height=65, width=185)

            self.back_button = tk.Button(text="Voltar", font='Arial 16 bold', command=self.iniciar_tela)
            self.back_button.place(x=20, y=660, height=50, width=185)
            self.back_button.config(state=tk.NORMAL)


            self.current_screen = 2 # Atualiza a tela

        elif opcao_selecionada == "Opção2":
            messagebox.showwarning("Aviso", "DEIXAR PARA OS PÚPILOS")

        # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

    def iniciar_tela(self):
            self.limparTela()
            Fonte = "Arial 15 bold"

            self.title("App Triagem")
            self.geometry("1080x720")
            self.config(background='#F0E68C')
            self.question_label = tk.Label(text="Qual o tipo de processo?", font="Arial 18 bold")
            self.question_label.place(x=410, y=220)
            self.question_label.config(background='#F0E68C')

            self.var_opcao = tk.StringVar(value="Opção1") # Variável de configuração que limita para apenas uma seleção de RadioButton
            self.option1 = tk.Radiobutton(text="Físico", variable=self.var_opcao, value="Opção1", font=Fonte)
            self.option1.config(bg='#F0E68C', activebackground='#F0E68C')
            self.option1.place(x=490, y=320)

            self.option2 = tk.Radiobutton(text="Digital", variable=self.var_opcao, value="Opção2", font=Fonte)
            self.option2.config(bg='#F0E68C', activebackground='#F0E68C')
            self.option2.place(x=490, y=380)

            self.submit_button = tk.Button(text="Próximo", font=Fonte, command=self.atualizarTela)
            self.submit_button.place(x=450, y=600, height=65, width=185)

            self.current_screen = 1 # Rastreia a tela atual

    def realizar_triagem(self):
        lista = list()
        TriagemApp.numeroProcesso = self.numberProcess.get()
        TriagemApp.numeroCPF = self.numberCPF.get()
        TriagemApp.senhaPje = self.senhaPje.get()

        lista.append(TriagemApp.numeroCPF)
        lista.append(TriagemApp.numeroProcesso)
        lista.append(TriagemApp.senhaPje)

        if len(TriagemApp.numeroProcesso) < 20 or len(TriagemApp.numeroProcesso) > 20: # colocar 20 numeros
            messagebox.showerror("Erro de digitação", "O número de processo está incorreto. \n\nCertifique-se de tirar os pontos(.) e traço(-) ao digitar.")

        else:
            self.limparTela()

            self.label_process = tk.Label(text = TriagemApp.numeroProcesso, font="Arial 18")
            self.label_process.place(x=750, y=100)
            self.label_process.config(background='#F0E68C')

            self.label_infoprocess = tk.Label(text="Processo que será consultado:", font="Arial 18")
            self.label_infoprocess.place(x=700, y=50)
            self.label_infoprocess.config(background='#F0E68C')

            self.back_button = tk.Button(text="Voltar", font='Arial 16 bold', command=self.atualizarTela)
            self.back_button.place(x=20, y=660, height=50, width=185)
            self.back_button.config(state=tk.NORMAL)

            self.current_screen = 2 # Atualiza a tela



            return lista

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = TriagemApp()
    app.run()
