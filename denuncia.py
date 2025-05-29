from dataclasses import dataclass,field #nova função python 3

# from collections import deque
# fila_atendimento = deque()

fila_atendimento = [] # adicionando as denúncias
vetor_historico = [] 
vetor_denuncias = [] 

@dataclass 
class Denuncia_bairro: 
    tipo: str 
    descricao: str
    data: str
    local: str
    prioridade: int

    def exibir(self):  
        return (f"[{self.data}] {self.tipo} em {self.local} -"
                f"Prioridade: {self.prioridade} - {self.descricao}")
    
    def __str__(self):
        return self.exibir()
    
@dataclass 
class NoBairro:
    bairro: str
    denuncias: list = field(default_factory=list) # inicializa com uma vetor/lista vazia
    esquerdo: 'NoBairro' = None 
    direito: 'NoBairro' = None

    def __post_init__(self):
        if self.denuncias is None: 
            self.denuncias = []

def inserir_bairro(raiz, bairro, denuncia):
    if raiz is None: 
        novo = NoBairro(bairro)
        novo.denuncias.append(denuncia)
        return novo
    if bairro < raiz.bairro:
        raiz.esquerdo = inserir_bairro(raiz.esquerdo, bairro, denuncia)
    elif bairro > raiz.bairro:
        raiz.direito = inserir_bairro(raiz.direito, bairro, denuncia)
    else:
        raiz.denuncias.append(denuncia)
    return raiz

def buscar_denuncias_bairro(raiz, bairro):
    if raiz is None:
        return [] # Retorna um vetor/lista vazia se o bairro não for encontrado
    
    if bairro == raiz.bairro:
        return raiz.denuncias
    elif bairro < raiz.bairro:
        return buscar_denuncias_bairro(raiz.esquerdo, bairro)
    else:
        return buscar_denuncias_bairro(raiz.direito, bairro)

def sistema_denuncias():
    raiz_bairros = None

    while True:
        print("=" * 34)
        print(f"\033[1;36mSistema de Denúncias de Saneamento\033[0m")
        print("=" * 34)
        print("""  
    1. Cadastrar nova denúncia
    2. Ver todas as denúncias
    3. Ver fila de atendimento
    4. Ver histórico de ações
    5. Buscar denúncias por bairro
    6. Atender próxima denúncia (Ao ser atendido ele é retirado da fila)
    0. Sair
    """)

        opcao = input("\033[1;32mEscolha uma opção:\033[0m ")

        if opcao == "1":
            tipo = input("\033[1;33mTipo de problema:\033[0m ")
            descricao = input("\033[1;33mDescrição do Problema Ocorrido: \033[0m")
            data = input("\033[1;33mData (dd/mm/aaaa): \033[0m")
            local = input("\033[1;33mBairro: \033[0m")
            prioridade = int(input("\033[1;31mPrioridade (1=Alta, 2=Média, 3=Baixa): \033[0m"))

            Denuncias = Denuncia_bairro(tipo, descricao, data, local, prioridade)
            vetor_denuncias.append(Denuncias)
            fila_atendimento.append(Denuncias)
            vetor_historico.append(f"Denúncia cadastrada: {tipo} - {local}")
            raiz_bairros = inserir_bairro(raiz_bairros, local, Denuncias)
            print("✅ \033[32mDenúncia registrada com sucesso.\033[0m")

        elif opcao == "2":
            if not vetor_denuncias:
                print("\033[1;31mNenhuma denúncia registrada.\033[0m")
                cadastrar = input("\033[1;33mDeseja cadastrar uma nova denúncia? (s/n): \033[0m").strip().lower()
                if cadastrar == 's' or cadastrar == 'sim':
                    tipo = input("\033[1;33mTipo de problema:\033[0m ")
                    descricao = input("\033[1;33mDescrição do Problema Ocorrido: \033[0m")
                    data = input("\033[1;33mData (dd/mm/aaaa): \033[0m")
                    local = input("\033[1;33mBairro: \033[0m")
                    prioridade = int(input("\033[1;31mPrioridade (1=Alta, 2=Média, 3=Baixa): \033[0m"))

                    Denuncias = Denuncia_bairro(tipo, descricao, data, local, prioridade)
                    vetor_denuncias.append(Denuncias)
                    fila_atendimento.append(Denuncias)
                    vetor_historico.append(f"Denúncia cadastrada: {tipo} - {local}")
                    raiz_bairros = inserir_bairro(raiz_bairros, local, Denuncias)
                    print("✅ \033[32mDenúncia registrada com sucesso.\033[0m")

                else:
                    for d in vetor_denuncias:
                        print(d)
            
            print("\n--- \033[1;36mLista de Denúncias Registradas\033[0m ---")
            for Denuncias in vetor_denuncias:
                print(Denuncias)

        elif opcao == "3":
            print("\n--- \033[1;36mFila de Atendimento (Classificada como prioridade)\033[0m ---")
            fila_ordenada = sorted(fila_atendimento, key=lambda x: x.prioridade) # Ordena a fila por prioridade
            for Denuncias in fila_ordenada:
                print(f"{Denuncias.tipo} - {Denuncias.local} - Prioridade: {Denuncias.prioridade}")

        elif opcao == "4":
            print("\n--- Histórico de Ações ---")
            for h in vetor_historico:
                print(h)

        elif opcao == "5":
            bairro = input("\033[33mDigite o bairro:\033[0m ")
            resultados = buscar_denuncias_bairro(raiz_bairros, bairro)
            if resultados:
                print(f"\nDenúncias no bairro {bairro} ({len(resultados)}):")
                for Denuncias in resultados:
                    print(Denuncias)
            else:
                print("Nenhuma denúncia encontrada para esse bairro. Tente novamente.")

        elif opcao == "6":
            if not fila_atendimento: # Verifica se a fila está vazia
                print("\n\033[33mNenhuma denúncia na fila de atendimento.\033[0m")
            else:

                print("\n--- \033[1;36mAtendendo próxima denúncia\033[0m ---")
                fila_ordenada = sorted(fila_atendimento, key=lambda x: x.prioridade) # Ordena a fila por prioridade
                denuncia_atendida = fila_ordenada[0]
                fila_atendimento.remove(denuncia_atendida)
                print("\n\033[1;32mDenúncia atendida com sucesso!\033[0m")
                print(denuncia_atendida)
                vetor_historico.append(f"Denúncia atendida: {denuncia_atendida.tipo} - {denuncia_atendida.local} ")

        elif opcao == "0":
            print("\n\033[1;34mSistema encerrado. Até mais!\033[0m")
            break

        else:
            print("\033[1;31mOpção inválida. Tente novamente.\033[0m \n")


# # Teste de execução do sistema
if __name__ == "__main__": # para garantir que o código só execute se for chamado diretamente 
    sistema_denuncias()