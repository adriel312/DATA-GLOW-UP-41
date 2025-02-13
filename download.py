import os
import requests

# Base URL do servidor
BASE_URL = "https://siros.anac.gov.br/siros/registros/diversos/vra/"

# Definição de anos e meses disponíveis
anos = []  # Adapte conforme necessário
for i in range(2000, 2025):
    anos.append(i)

meses = []
for i in range(1,13):
    meses.append(i)

# Criar diretório base para os downloads
DOWNLOAD_DIR = "csv_downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

for ano in anos:
    # Criar pasta para o ano
    ano_dir = os.path.join(DOWNLOAD_DIR, str(ano))
    os.makedirs(ano_dir, exist_ok=True)

    for mes in meses:
        # Construir a URL do arquivo
        if ano <= 2009:
            file_url = f"{BASE_URL}/{ano}/VRA_{ano}{mes}.csv"
        else:
            if mes<10:
                file_url = f"{BASE_URL}/{ano}/VRA_{ano}_0{mes}.csv"
            else:
                file_url = f"{BASE_URL}/{ano}/VRA_{ano}_{mes}.csv"

        file_path = os.path.join(ano_dir, f"{mes}.csv")

        try:
            print(f"Baixando {file_url} ...")
            response = requests.get(file_url, timeout=10)
            response.raise_for_status()  # Lança um erro se o download falhar

            # Salvar o arquivo
            with open(file_path, "wb") as file:
                file.write(response.content)
            print(f"Salvo em {file_path}")

        except requests.exceptions.RequestException as e:
            print(f"Erro ao baixar {file_url}: {e}")