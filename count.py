from flask import Flask
import os

app = Flask(__name__)

# Nome do arquivo para salvar o contador
counter_file = 'count.txt'

# Função para carregar o contador do arquivo
def load_counter():
    if os.path.exists(counter_file):
        with open(counter_file, 'r') as file:
            try:
                return int(file.read().strip())
            except ValueError:
                return 0
    return 0

# Função para salvar o contador no arquivo
def save_counter(count):
    with open(counter_file, 'w') as file:
        file.write(str(count))

# Rota principal
@app.route('/')
def index():
    # Carregar o contador
    count = load_counter()

    # Incrementar o contador
    count += 1

    # Salvar o contador atualizado
    save_counter(count)
    rets=f"<html><head><title>Visits</title></head><body style='background-color:#000000;color:#ffffff'>visits: {count} times<body></html>"
    return rets

if __name__ == '__main__':
    app.run(debug=True)

