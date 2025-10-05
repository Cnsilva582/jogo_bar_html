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
    
def generate_contact_html(output_path):
    html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="../style/style.css">
  <title>Contato</title>
</head>
<body>
  <header>
    <img src="../style/img/logot.png" alt="" style="height: 90px; width: auto;">
    <nav>
      <a href="index.html">Home</a>
      <a href="menu_foods.html">Cardápio</a>
      <a href="menu_games.html">Jogos</a>
      <a href="contact.html">Contato</a>
    </nav>
  </header>
    <div class="ajustar_footer" > 
    <div class="centralizar">
      <h1 >Contato</h1>
      <form onsubmit="enviarMensagem(event)">
        <label for="mensagem">Digite sua mensagem:</label><br>
        <textarea id="mensagem" required></textarea><br>
        <button type="submit">Enviar</button>
      </form>
      <h2>Mensagens</h2>
      <ul id="lista-mensagens"></ul>
      <button onclick="limparMensagens()">Apagar todas</button>
    </div>
  </div>
  <script>
    // Envia e salva mensagem no localStorage
    function enviarMensagem(event) {
      event.preventDefault();
      let mensagem = document.getElementById("mensagem").value.trim();
      if (mensagem === "") return;

      let mensagens = JSON.parse(localStorage.getItem("mensagens")) || [];
      mensagens.push(mensagem);
      localStorage.setItem("mensagens", JSON.stringify(mensagens));

      document.getElementById("mensagem").value = "";
      carregarMensagens();
    }

    // Carrega mensagens na lista
    function carregarMensagens() {
      let mensagens = JSON.parse(localStorage.getItem("mensagens")) || [];
      let lista = document.getElementById("lista-mensagens");
      lista.innerHTML = "";

      if (mensagens.length === 0) {
        lista.innerHTML = "<li>Nenhuma mensagem ainda.</li>";
        return;
      }

      mensagens.forEach((m, i) => {
        let li = document.createElement("li");
        li.textContent = m + " ";

        // Botão para excluir individualmente
        let btn = document.createElement("button");
        btn.textContent = "Excluir";
        btn.onclick = () => apagarMensagem(i);

        li.appendChild(btn);
        lista.appendChild(li);
      });
    }

    // Apaga mensagem específica
    function apagarMensagem(index) {
      let mensagens = JSON.parse(localStorage.getItem("mensagens")) || [];
      mensagens.splice(index, 1);
      localStorage.setItem("mensagens", JSON.stringify(mensagens));
      carregarMensagens();
    }

    // Apaga todas as mensagens
    function limparMensagens() {
      localStorage.removeItem("mensagens");
      carregarMensagens();
    }

    // Carrega ao abrir a página
    carregarMensagens();
  </script>

  <footer>
    <p>© 2025/2 Tabuleiro & Cerveja</p>
    
  </footer>
</body>
</html>"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

def generate_index_html(output_path):
    html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tabuleiro & Cerveja</title>
    <link rel="stylesheet" href="../style/style.css">
</head>
<body>
    <header>
        <h1><img src="../style/img/logot.png" alt="" style="height: 90px; width: auto;"></h1>
        <nav>
            <a href="index.html">Home</a>
            <a href="menu_foods.html">Cardápio</a>
            <a href="menu_games.html">Jogos</a>
            <a href="contact.html">Contato</a>
        </nav>
    </header>
    <main>
        <section id="bem-vindo">
            <h2>Bem-Vindo ao Tabuleiro & Cerveja!</h2>
            <p>Aqui Tem um espaço para voçê Comer, Beber e se divertir</p>
            <p>com os melhores jogos de Tabuleiros.</p>
            <p>“Onde a diversão encontra o sabor.”</p>
        </section>
    <h2><strong>Nosso Espaço</strong></h2>
        <section id="galeria">
            <div class="galeria">
                <img src="../style/img/img1.png" alt="">
                <img src="../style/img/img2.png" alt="">
                <img src="../style/img/img3.png" alt="">
                <img src="../style/img/img3.png" alt="">
            </div>
        </section>
        <section id="promo-video">
            <h2><strong>Assista e Conheça!</strong></h2>
            <div class="video-container">
                <video controls>
                    <source src="../style/video/video0.mp4" type="video/mp4">
                    Seu navegador não suporta vídeos.
                </video>
            </div>
        </section> 
    </main>
    <footer>
        <p>© 2025/2 Tabuleiro & Cerveja</p>
    </footer>
</body>
</html>
"""
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

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
        <a href="contact.html">Contato</a>
    </nav>
</header>
<div class="mensagem-comanda">
    <p><strong>A comanda segue ao final dessa página!</strong></p>
</div>
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
        <button onclick="adicionarComanda('{food['name']}', {food['price']})">Adicionar à Comanda</button>
    </div>
"""
    # Comanda (visível no fim da página)
    html_content += """
</div>

<section>
    <div class="centralizar_comanda">
        <h2> Sua Comanda</h2>
            <ul id="comanda-lista"></ul>
                <p><strong>Total:</strong> R$ <span id="comanda-total">0.00</span></p>
            <button onclick="limparComanda()"> Limpar Comanda</button>
        <footer>
            <p>© 2025 Tabuleiro & Cerveja</p>
        </footer>
    </div>

<script>
let comanda = JSON.parse(localStorage.getItem("comanda")) || [];

function salvarComanda() {
    localStorage.setItem("comanda", JSON.stringify(comanda));
}

function atualizarComanda() {
    const lista = document.getElementById("comanda-lista");
    const totalSpan = document.getElementById("comanda-total");
    lista.innerHTML = "";

    let total = 0;

    if (comanda.length === 0) {
        lista.innerHTML = "<li>Nenhum item na comanda.</li>";
    } else {
        comanda.forEach((item, i) => {
            total += item.price;

            const li = document.createElement("li");
            li.textContent = `${item.name} - R$ ${item.price.toFixed(2)} `;

            const btn = document.createElement("button");
            btn.textContent = "Remover";
            btn.onclick = () => {
                comanda.splice(i, 1);
                salvarComanda();
                atualizarComanda();
            };

            li.appendChild(btn);
            lista.appendChild(li);
        });
    }

    totalSpan.textContent = total.toFixed(2);
}

function adicionarComanda(nome, preco) {
    comanda.push({ name: nome, price: preco });
    salvarComanda();
    atualizarComanda();
}

function limparComanda() {
    comanda = [];
    salvarComanda();
    atualizarComanda();
}

atualizarComanda();
</script>

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
        <a href="contact.html">Contato</a>
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

    generate_index_html(os.path.join(output_dir, 'index.html')) 
    generate_foods_html(foods, os.path.join(output_dir, 'menu_foods.html'))
    generate_games_html(games, os.path.join(output_dir, 'menu_games.html'))
    generate_contact_html(os.path.join(output_dir,'contact.html'))

if __name__ == "__main__":
    main()
