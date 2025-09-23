from pathlib import Path
import json

# Diretório do script
base_dir = Path(__file__).parent

# Caminho para foods.json
arquivo_foods = base_dir.parent / "data" / "foods.json"
arquivo_games = base_dir.parent / "data" / "games.json"

# Saídas dos HTMLs
saida_cardapio = base_dir.parent / "output" / "menu_foodes.html"
saida_jogos = base_dir.parent / "output" / "menu_games.html"

with open(arquivo_foods, "r", encoding="utf-8") as f:
    dados = json.load(f)
print("=== MENU DE FOODS ===")
print(json.dumps(dados, indent=4, ensure_ascii=False))

with open(arquivo_games, "r", encoding="utf-8") as f:
    dados = json.load(f)
print("\n=== LISTA DE GAMES ===")
print(json.dumps(dados, indent=4, ensure_ascii=False))