import os
import pandas as pd

# Diretório onde estão as pastas dos anos
BASE_DIR = "csv_downloads"

# Nome das colunas que devem ser removidas
colunas_para_remover = ["Empresa Aérea", "Modelo Equipamento", "Número de Assentos", "Descrição Aeroporto Origem", "Descrição Aeroporto Destino", "Referência", "Situação Partida", "Situação Chegada", "Justificativa", "Empresa AÃ©rea", "NÃºmero de Assentos", "DescriÃ§Ã£o Aeroporto Origem", "DescriÃ§Ã£o Aeroporto Destino", "DescriÃ§Ã£o Aeroporto Destino", "ReferÃªncia", "CÃ³digo Justificativa", "SituaÃ§Ã£o Partida", "SituaÃ§Ã£o Chegada"]

# Percorre todas as pastas (anos)
for ano in os.listdir(BASE_DIR):
    ano_path = os.path.join(BASE_DIR, ano)
    
    if os.path.isdir(ano_path):  # Confirma se é uma pasta
        # Percorre todos os arquivos CSV dentro da pasta do ano
        for arquivo in os.listdir(ano_path):
            if arquivo.endswith(".csv"):  # Confirma se é um arquivo CSV
                arquivo_path = os.path.join(ano_path, arquivo)
                
                try:
                    # Lendo o CSV
                    df = pd.read_csv(arquivo_path, delimiter=";", encoding="ISO-8859-1", dtype=str)
                    
                    # Remove as colunas se existirem
                    df = df.drop(columns=[col for col in colunas_para_remover if col in df.columns], errors='ignore')
                    
                    # Salva o CSV atualizado no mesmo local
                    df.to_csv(arquivo_path, index=False, sep=";", encoding="ISO-8859-1")
                    
                    print(f"Arquivo atualizado: {arquivo_path}")
                
                except Exception as e:
                    print(f"Erro ao processar {arquivo_path}: {e}")
