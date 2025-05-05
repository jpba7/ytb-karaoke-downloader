import customtkinter as ctk
from tkinter import filedialog
import os

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Inicializa variáveis de controle
        self.caminho_arquivo_var = None
        self.numero_inicial_var = None
        
        # Configuração da janela principal
        self.title("Download de Karaokês")
        self.geometry("900x700")
        
        # Configuração do tema
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Inicializa as páginas
        self.pagina_atual = None
        self.mostrar_boas_vindas()
    
    def limpar_tela(self):
        """Remove todos os widgets da tela"""
        for widget in self.winfo_children():
            widget.destroy()
    
    def mostrar_boas_vindas(self):
        """Primeira página - Boas vindas"""
        self.limpar_tela()
        
        # Frame central
        frame = ctk.CTkFrame(self)
        frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Título
        titulo = ctk.CTkLabel(
            frame, 
            text="Olá, Marica!\nBem-vindo ao Baixador de Karaokês!\n\n",
            font=("Arial", 24, "bold"),
            text_color="white"
        )
        titulo.pack(pady=30)
        
        # Descrição
        descricao = ctk.CTkLabel(
            frame,
            text="Para o terror dos vizinhos, este programa permite baixar\nkaraokês do YouTube de forma fácil e rápida.\n\n ",
            font=("Arial", 14)
        )
        descricao.pack(pady=20)
        
        # Botão Iniciar
        btn_iniciar = ctk.CTkButton(
            frame,
            text="Iniciar",
            command=self.mostrar_selecao_arquivo,
            width=200,
            height=40,
            font=("Arial", 14, "bold")
        )
        btn_iniciar.pack(pady=30)
    
    def mostrar_selecao_arquivo(self):
        """Segunda página - Seleção de arquivo"""
        self.limpar_tela()
        
        # Criar StringVar para armazenar o caminho
        self.caminho_arquivo_var = ctk.StringVar()
        
        frame = ctk.CTkFrame(self)
        frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        # Título
        titulo = ctk.CTkLabel(
            frame,
            text="Selecione o arquivo de músicas",
            font=("Arial", 20, "bold")
        )
        titulo.pack(pady=20)

        instrucoes = ctk.CTkLabel(
            frame,
            text="1. Abra o bloco de notas\n\n 2. Digite as músicas que deseja baixar separadas por ponto e vírgula (As músicas devem ter o nome do cantor e\n o nome da música para minimizar erros).\n\n Ex.: Gustavo Lima - Chorei largado; Chitãozinho e Chitãozinho - Dormi na praça; Xororó e Xororó - Dormi em casa;\n\n 3. Salve o arquivo em algum lugar do computador. \n\n 4. Clique no botão abaixo e selecione o arquivo que você criou.\n\n",
            font=("Arial", 14)
        )
        instrucoes.pack(pady=10)
        
        # Frame para agrupar entrada e botão
        input_frame = ctk.CTkFrame(frame)
        input_frame.pack(pady=20)
        
        # Campo do arquivo usando StringVar
        self.caminho_arquivo = ctk.CTkEntry(
            input_frame,
            width=350,
            placeholder_text="Caminho do arquivo .txt",
            textvariable=self.caminho_arquivo_var
        )
        self.caminho_arquivo.pack(side="left", padx=(0, 10))
        
        # Botão procurar
        btn_procurar = ctk.CTkButton(
            input_frame,
            text="Procurar arquivo",
            command=self.selecionar_arquivo,
            width=200
        )
        btn_procurar.pack(side="left")
        
        # Botão próximo
        self.btn_proximo = ctk.CTkButton(
            frame,
            text="Próximo",
            command=self.mostrar_numero_inicial,
            width=200,
            state="disabled"
        )
        self.btn_proximo.pack(pady=10)
        
        # Botão voltar
        btn_voltar = ctk.CTkButton(
            frame,
            text="Voltar",
            command=self.mostrar_boas_vindas,
            width=200,
            fg_color="transparent",
            border_width=2
        )
        btn_voltar.pack(pady=20)
    
    def selecionar_arquivo(self):
        """Abre diálogo para selecionar arquivo"""
        arquivo = filedialog.askopenfilename(
            title="Selecione o arquivo de músicas",
            filetypes=[("Arquivo de texto", "*.txt")]
        )
        if arquivo:
            self.caminho_arquivo_var.set(arquivo)
            self.btn_proximo.configure(state="normal")

    def mostrar_numero_inicial(self):
        """Terceira página - Seleção do número inicial"""
        self.limpar_tela()
        
        # Criar StringVar para armazenar o número
        self.numero_inicial_var = ctk.StringVar(value="1")
        
        frame = ctk.CTkFrame(self)
        frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        titulo = ctk.CTkLabel(
            frame,
            text="Número inicial",
            font=("Arial", 20, "bold")
        )
        titulo.pack(pady=20)
        
        instrucoes = ctk.CTkLabel(
            frame,
            text="Digite o número a partir do qual a listagem deve começar:",
            font=("Arial", 14)
        )
        instrucoes.pack(pady=10)
        
        # Campo do número usando StringVar
        self.numero_inicial = ctk.CTkEntry(
            frame,
            width=200,
            placeholder_text="Número inicial",
            textvariable=self.numero_inicial_var
        )
        self.numero_inicial.pack(pady=20)
        
        btn_iniciar = ctk.CTkButton(
            frame,
            text="Iniciar Download",
            command=self.iniciar_downloads,
            width=200
        )
        btn_iniciar.pack(pady=10)
        
        btn_voltar = ctk.CTkButton(
            frame,
            text="Voltar",
            command=self.mostrar_selecao_arquivo,
            width=200,
            fg_color="transparent",
            border_width=2
        )
        btn_voltar.pack(pady=20)

    def abrir_pasta_downloads(self):
        """Abre o explorador de arquivos na pasta de downloads"""
        output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "Karaokes baixados")
        os.startfile(output_dir)

    def mostrar_progresso(self):
        """Quarta página - Progresso dos downloads"""
        self.limpar_tela()
        
        frame = ctk.CTkFrame(self)
        frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        titulo = ctk.CTkLabel(
            frame,
            text="Download em Andamento",
            font=("Arial", 20, "bold")
        )
        titulo.pack(pady=20)
        
        self.progresso = ctk.CTkTextbox(frame, width=600, height=200)
        self.progresso.pack(pady=20)
        
        # Frame para os botões
        botoes_frame = ctk.CTkFrame(frame)
        botoes_frame.pack(pady=20)
        
        # Botão mostrar pasta
        self.btn_mostrar_pasta = ctk.CTkButton(
            botoes_frame,
            text="Mostrar pasta",
            command=self.abrir_pasta_downloads,
            width=200,
            height=30,
            font=("Arial", 14, "bold"),
            state="disabled"
        )
        self.btn_mostrar_pasta.pack(side="left", padx=10)
        
        # Botão concluir
        self.btn_concluir = ctk.CTkButton(
            botoes_frame,
            text="Concluir",
            command=self.mostrar_boas_vindas,
            width=200,
            height=30,
            font=("Arial", 14, "bold"),
            state="disabled"
        )
        self.btn_concluir.pack(side="left", padx=10)

    def atualizar_progresso(self, mensagem):
        """Atualiza o log de progresso"""
        self.progresso.insert("end", mensagem + "\n")
        self.progresso.see("end")
        self.update()

    def iniciar_downloads(self):
        """Inicia o processo de download"""
        try:
            from main import process_music_list
            
            # Obter valores das variáveis
            arquivo = self.caminho_arquivo_var.get()
            numero = int(self.numero_inicial_var.get())
            
            if not arquivo or not os.path.exists(arquivo):
                raise ValueError("Arquivo não selecionado ou inválido")
                
            if numero < 1:
                raise ValueError("Número inicial deve ser maior que zero")
            
            self.mostrar_progresso()
            
            def finalizar_downloads(falhas):
                if falhas:
                    self.atualizar_progresso("\nFalhas nos downloads:")
                    for falha in falhas:
                        self.atualizar_progresso(f"❌ {falha}")
                else:
                    self.atualizar_progresso("\n✅ Todos os downloads concluídos com sucesso!")
                # Habilita ambos os botões quando concluir
                self.btn_concluir.configure(state="normal")
                self.btn_mostrar_pasta.configure(state="normal")
            
            import threading
            thread = threading.Thread(
                target=lambda: finalizar_downloads(
                    process_music_list(arquivo, numero, self.atualizar_progresso)
                )
            )
            thread.start()
            
        except ValueError as e:
            import tkinter.messagebox as messagebox
            messagebox.showerror("Erro", str(e))
        except Exception as e:
            import tkinter.messagebox as messagebox
            messagebox.showerror("Erro", f"Erro inesperado: {str(e)}")

if __name__ == "__main__":
    app = App()
    app.mainloop()