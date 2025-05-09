from denuncia import Denuncia_bairro,NoBairro,inserir_bairro,buscar_denuncias_bairro,sistema_denuncias
import time
import sys

def loading_animado():
    roda_roda_jequiti = ['|', '/', '-', '\\', '|', '/', '-', '\\']
    barra_total = 20

    print("\033[34m")
    print("=" * 42)
    print("🚰 SISTEMA DE AGUA | Versão: ALPHA 1.0 🚰")
    print("=" * 42)
    print("\033[0m")

    print("\033[33mIniciando sistema... Aguarde\033[0m\n")

    for i in range(barra_total + 1):
        porcentagem = int((i / barra_total) * 100)
        barra = '█' * i + '░' * (barra_total - i)
        spinner_char = roda_roda_jequiti[i % len(roda_roda_jequiti)]
        sys.stdout.write(f"\r{spinner_char} Carregando: [{barra}] {porcentagem}% ")
        sys.stdout.flush()
        time.sleep(0.2)

    print("\n\033[32m✅ Sistema carregado com sucesso!\033[0m\n")

loading_animado()
sistema_denuncias()