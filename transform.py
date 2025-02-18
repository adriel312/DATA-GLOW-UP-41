import os
import csv

# Diretório onde os arquivos CSV estão localizados
BASE_DIR = "csv_downloads"

# Função para detectar o delimitador do arquivo
def detectar_delimitador(file_path):
    encodings = ["utf-8", "ISO-8859-1"]  # Tenta diferentes encodings

    for encoding in encodings:
        try:
            with open(file_path, "r", encoding=encoding) as f:
                linha = f.readline()  # Lê a primeira linha
                if "," in linha:
                    return ",", encoding
                elif ";" in linha:
                    return ";", encoding
        except UnicodeDecodeError:
            continue  # Se der erro, tenta outro encoding

    print(f"Não foi possível detectar delimitador para {file_path}. Usando ',' como padrão.")
    return ",", "ISO-8859-1"  # Retorna padrão seguro

# Percorre os diretórios por ano e mês
for ano in range(2000, 2025):
    ano_dir = os.path.join(BASE_DIR, str(ano))

    if os.path.exists(ano_dir):  # Verifica se o diretório do ano existe
        for mes_csv in os.listdir(ano_dir):
            file_path = os.path.join(ano_dir, mes_csv)

            if file_path.endswith(".csv"):  # Confirma que é um arquivo CSV
                delimitador, encoding = detectar_delimitador(file_path)

                # Se o delimitador for ',', converte para ';'
                if delimitador == ",":
                    try:
                        with open(file_path, "r", encoding=encoding, newline="") as file:
                            reader = csv.reader(file, delimiter=",")
                            dados = [linha for linha in reader]

                        # Reescreve o arquivo com ';' como delimitador
                        with open(file_path, "w", encoding="utf-8", newline="") as file:
                            writer = csv.writer(file, delimiter=";", quoting=csv.QUOTE_MINIMAL)
                            writer.writerows(dados)

                        print(f"Convertido ',' para ';' em {file_path}")

                    except Exception as e:
                        print(f"Erro ao processar {file_path}: {e}")

print("Processo concluído!")
