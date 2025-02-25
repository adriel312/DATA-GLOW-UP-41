import pandas as pd
import os

# Diretório principal onde estão as pastas dos anos
diretorio_principal = "csv_downloads"

# Nome correto das colunas e ordem padronizada
colunas_padrao = [
    "Sigla ICAO Empresa Aérea", "Número Voo", "Código DI", "Código Tipo Linha",
    "Sigla ICAO Aeroporto Origem", "Partida Prevista", "Partida Real",
    "Sigla ICAO Aeroporto Destino", "Chegada Prevista", "Chegada Real", "Situação Voo"
]

# Mapeamento de colunas diferentes para o nome padrão
mapeamento_colunas = {
    "ICAO Empresa Aérea": "Sigla ICAO Empresa Aérea",
    "Sigla ICAO Empresa Aérea": "Sigla ICAO Empresa Aérea",
    "Código Autorização (DI)": "Código DI",
    "Código DI": "Código DI",
    "ICAO Aeródromo Origem": "Sigla ICAO Aeroporto Origem",
    "Sigla ICAO Aeroporto Origem": "Sigla ICAO Aeroporto Origem",
    "ICAO Aeródromoo Destino": "Sigla ICAO Aeroporto Destino",
    "Sigla ICAO Aeroporto Destino": "Sigla ICAO Aeroporto Destino"
}

# Percorre os anos de 2000 a 2024
for ano in range(2000, 2025):
    pasta_ano = os.path.join(diretorio_principal, str(ano))

    # Verifica se a pasta do ano existe
    if os.path.exists(pasta_ano):
        print(f"Processando arquivos do ano {ano}...")

        # Percorre os 12 arquivos dentro da pasta do ano
        for mes in range(1, 13):
            arquivo_nome = f"{ano}_{mes:02d}.csv"  # Ajuste se necessário
            arquivo_path = os.path.join(pasta_ano, arquivo_nome)

            if os.path.exists(arquivo_path):  # Verifica se o arquivo existe
                try:
                    # Ler CSV sem perder informações (tudo como string para evitar dtype issues)
                    df = pd.read_csv(arquivo_path, delimiter=";", encoding="ISO-8859-1", dtype=str)

                    # Renomear colunas para o padrão definido
                    df.rename(columns=mapeamento_colunas, inplace=True)

                    # Garantir que todas as colunas existam, adicionando vazias caso faltem
                    for coluna in colunas_padrao:
                        if coluna not in df.columns:
                            df[coluna] = ""

                    # Manter apenas as colunas na ordem padronizada
                    df = df[colunas_padrao]

                    # Salvar de volta no mesmo local
                    df.to_csv(arquivo_path, sep=";", index=False, encoding="ISO-8859-1")

                    print(f"{arquivo_nome} processado com sucesso!")

                except Exception as e:
                    print(f"Erro ao processar {arquivo_nome}: {e}")
            else:
                print(f"Arquivo não encontrado: {arquivo_path}")

print("Normalização concluída para todos os arquivos!")
