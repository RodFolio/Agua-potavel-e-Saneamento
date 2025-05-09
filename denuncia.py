from collections import deque
# import datetime

class Denuncia_bairro:
    def __init__(self, tipo, descricao, data, local, prioridade):
        self.tipo = tipo
        self.descricao = descricao
        self.data = data
        self.local = local
        self.prioridade = prioridade

    def __str__(self):
        return (f"[{self.data}] {self.tipo} em {self.local} - "
                f"Prioridade: {self.prioridade}\\n{self.descricao}")

historico = []
fila_atendimento = deque()
denuncias = []

class NoBairro:
    def __init__(self, bairro):
        self.bairro = bairro
        self.denuncias = []
        self.esq = None
        self.dir = None


def inserir_bairro(raiz, bairro, denuncia):
    if raiz is None:
        novo = NoBairro(bairro)
        novo.denuncias.append(denuncia)
        return novo
    if bairro < raiz.bairro:
        raiz.esq = inserir_bairro(raiz.esq, bairro, denuncia)
    elif bairro > raiz.bairro:
        raiz.dir = inserir_bairro(raiz.dir, bairro, denuncia)
    else:
        raiz.denuncias.append(denuncia)
    return raiz

def buscar_denuncias_bairro(raiz, bairro):
    if raiz is None:
        return []
    if bairro == raiz.bairro:
        return raiz.denuncias
    elif bairro < raiz.bairro:
        return buscar_denuncias_bairro(raiz.esq, bairro)
    else:
        return buscar_denuncias_bairro(raiz.dir, bairro)

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
    0. Sair
    """)

        opcao = input("\033[1;32mEscolha uma opção:\033[0m ")

        if opcao == "1":
            tipo = input("\033[1;33mTipo de problema:\033[0m ")
            descricao = input("\033[1;33mDescrição do Problema Ocorrido: \033[0m")
            data = input("\033[1;33mData (dd/mm/aaaa): \033[0m")
            local = input("\033[1;33mBairro: \033[0m")
            prioridade = int(input("\033[1;31mPrioridade (1=Alta, 2=Média, 3=Baixa): \033[0m"))


            d = Denuncia_bairro(tipo, descricao, data, local, prioridade)
            denuncias.append(d)
            fila_atendimento.append(d)
            historico.append(f"Denúncia cadastrada: {tipo} - {local}")
            raiz_bairros = inserir_bairro(raiz_bairros, local, d)
            print("Denúncia registrada com sucesso.")

        elif opcao == "2":
            print("\n--- \033[1;31mTodas as Denúncias\033[0m ---")
            for d in denuncias:
                print(d, "\n")

        elif opcao == "3":
            print("\n--- \033[1;36mFila de Atendimento\033[0m ---")
            for d in fila_atendimento:
                print(f"{d.tipo} - {d.local}")

        elif opcao == "4":
            print("\n--- Histórico de Ações ---")
            for h in historico:
                print(h)

        elif opcao == "5":
            bairro = input("\033[33mDigite o bairro:\033[0m ")
            resultados = buscar_denuncias_bairro(raiz_bairros, bairro)
            if resultados:
                print(f"\nDenúncias no bairro {bairro}:")
                for d in resultados:
                    print(d, "\n")
            else:
                print("Nenhuma denúncia encontrada para esse bairro.")

        elif opcao == "0":
            print("Encerrando o sistema.")
            break

        else:
            print("\033[1;31mOpção inválida. Tente novamente.\033[0m \n")
            # print(end="")

if __name__ == "__main__":
    sistema_denuncias()