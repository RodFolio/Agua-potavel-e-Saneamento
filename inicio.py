import sys
from dataclasses import dataclass,field
import time as tempo
from denuncia import Denuncia_bairro, NoBairro, inserir_bairro, buscar_denuncias_bairro,sistema_denuncias

@dataclass
class LoadingAnimado:
    roda_roda_jequiti: list = field(default_factory=lambda: ['|', '/', '-', '\\', '|', '/', '-', '\\']) 
    barra_total: int = 25

    def iniciar(self):
        print("\033[34m")
        print("=" * 57)
        print("🚰 Sistema de denúncias e saneamento básico.|ALPHA 1.0 🚰".upper())
        print("=" * 57)
        print("\033[0m")
        print("\033[33mIniciando sistema... Aguarde!\033[0m\n")

        for i in range(self.barra_total + 1):
            porcentagem = int((i / self.barra_total) * 100)
            barra = '\033[32m█\033[0m' * i + '\033[37m█\033[0m' * (self.barra_total - i) 
            spinner_char = self.roda_roda_jequiti[i % len(self.roda_roda_jequiti)] # faz a animação girar

            sys.stdout.write(f"\r{spinner_char} \033[1m\033[33mCarregando\033[0m: {barra} {porcentagem}% ")
            sys.stdout.flush()
            tempo.sleep(0.2)

        print("\n\033[32m✅ Sistema carregado com Sucesso!\033[0m\n")

LoadingAnimado().iniciar()
sistema_denuncias()
        
# if __name__ == "__main__": # 
#     loading = LoadingAnimado()
#     loading.iniciar()
#     sistema_denuncias()