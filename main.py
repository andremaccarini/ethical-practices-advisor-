import json
import os

# Caminho para o arquivo JSON

DATA_PATH = os.path.join("data", "complinace_data.json")

def carregar_dados():
    """Carrega as recomendações de compliance do arquivo JSON."""
    try:
        with open(DATA_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Erro: Arquivo de dados não encontrado.")
        return {}

def exibir_setores(dados):
    """Exibe os setores disponíveis para consulta."""
    print("\nSetores disponíveis:")
    for setor in dados.keys():
        print(f"- {setor.capitalize()}")

def obter_recomendacoes(dados, setor):
    """Obtém as recomendações para um setor específico."""
    return dados.get(setor.lower(), None)

def main():
    """Função principal que gerencia a interação com o usuário."""
    print("📌 Bem-vindo ao Guia de Compliance 📌")
    
    dados = carregar_dados()
    
    if not dados:
        print("Erro ao carregar os dados. Verifique o arquivo JSON.")
        return

    while True:
        exibir_setores(dados)
        setor = input("\nDigite o nome do setor desejado (ou 'sair' para encerrar): ").strip().lower()
        
        if setor == "sair":
            print("Encerrando o programa. Obrigado por usar o Guia de Compliance!")
            break
        
        recomendacoes = obter_recomendacoes(dados, setor)
        
        if recomendacoes:
            print(f"\n🔹 Recomendações para o setor {setor.capitalize()}:")
            for i, recomendacao in enumerate(recomendacoes, 1):
                print(f"{i}. {recomendacao}")
        else:
            print("❌ Setor não encontrado. Tente novamente.")

if __name__ == "__main__":
    main()
