import json
import os
import sys

def load_json_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Erro ao ler {filepath}: {e}")
        return []

def generate_foods_html(foods, output_path):
    html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cardápio de Comidas - Tabuleiro & Cerveja</title>
    <link rel="stylesheet" href="../style/style.css">
</head>
<body>
<header>
    <h1>Cardápio de Comidas</h1>
    <nav>
        <a href="index.html">Home</a>
        <a href="menu_foods.html">Cardápio</a>
        <a href="menu_games.html">Jogos</a>
    </nav>
</header>
<div class="cards-container">
"""
    for food in foods:
        html_content += f"""
    <div class="card">
        <img src="../{food['image']}" alt="{food['name']}">
        <h2>{food['name']}</h2>
        <p>{food['description']}</p>
        <p><strong>Ingredientes:</strong> {food['ingredients']}</p>
        <p><strong>Preço:</strong> R$ {food['price']}</p>
    </div>
"""
    html_content += """
</div>
<footer>
    <p>© 2025 Tabuleiro & Cerveja</p>
</footer>
</body>
</html>
"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

def generate_games_html(games, output_path):
    html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Jogos Disponíveis - Tabuleiro & Cerveja</title>
    <link rel="stylesheet" href="../style/style.css">
</head>
<body>
<header>
    <h1>Jogos Disponíveis</h1>
    <nav>
        <a href="index.html">Home</a>
        <a href="menu_foods.html">Cardápio</a>
        <a href="menu_games.html">Jogos</a>
    </nav>
</header>
<div class="cards-container">
"""
    for game in games:
        html_content += f"""
    <div class="card">
        <img src="../{game['image']}" alt="{game['name']}">
        <h2>{game['name']}</h2>
        <p>{game['description']}</p>
        <p><strong>Tipo:</strong> {game['type']}</p>
        <p><strong>Quantidade de jogadores:</strong> {game['players']}</p>
    </div>
"""
    html_content += """
</div>
<footer>
    <p>© 2025 Tabuleiro & Cerveja</p>
</footer>
</body>
</html>
"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

def main():
    data_dir = sys.argv[1] if len(sys.argv) > 1 else input("Digite o diretório dos arquivos de dados: ")
    while not os.path.isdir(data_dir):
        data_dir = input("Diretório inválido. Digite novamente: ")

    foods = load_json_file(os.path.join(data_dir, 'foods.json'))
    games = load_json_file(os.path.join(data_dir, 'games.json'))

    output_dir = os.path.join(os.path.dirname(__file__), '../output')
    os.makedirs(output_dir, exist_ok=True)

    generate_foods_html(foods, os.path.join(output_dir, 'menu_foods.html'))
    generate_games_html(games, os.path.join(output_dir, 'menu_games.html'))

if __name__ == "__main__":
    main()
