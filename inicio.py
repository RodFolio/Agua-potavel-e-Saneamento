import sys
import time as tempo
from denuncia import Denuncia_bairro, NoBairro, inserir_bairro, buscar_denuncias_bairro,sistema_denuncias

class LoadingAnimado:
    def __init__(self):
        self.roda_roda_jequiti = ['|', '/', '-', '\\', '|', '/', '-', '\\']
        self.barra_total = 20

    def iniciar(self):
        print("\033[34m")
        print("=" * 42)
        print("🚰 SISTEMA DE AGUA | Versão: ALPHA 1.0 🚰")
        print("=" * 42)
        print("\033[0m")

        print("\033[33mIniciando sistema... Aguarde\033[0m\n")

        for i in range(self.barra_total + 1):
            porcentagem = int((i / self.barra_total) * 100)
            barra = '█' * i + '░' * (self.barra_total - i)
            spinner_char = self.roda_roda_jequiti[i % len(self.roda_roda_jequiti)]

            sys.stdout.write(f"\r{spinner_char} Carregando: [{barra}] {porcentagem}% ")
            sys.stdout.flush()
            tempo.sleep(0.2)

        print("\n\033[32m✅ Sistema carregado com sucesso!\033[0m\n")

if __name__ == "__main__":
    loading = LoadingAnimado()
    loading.iniciar()
    sistema_denuncias()