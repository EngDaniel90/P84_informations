import os

def ler_dados_txt(caminho_arquivo):
    dados = []
    if os.path.exists(caminho_arquivo):
        with open(caminho_arquivo, 'r', encoding='utf-8') as f:
            for linha in f:
                if linha.strip() and '=' in linha:
                    chave, valor = linha.split('=', 1)
                    dados.append((chave.strip(), valor.strip()))
    else:
        print(f"Aviso: Arquivo {caminho_arquivo} não encontrado.")
    return dados

# Lê os arquivos de texto
informacoes = ler_dados_txt('informacoes.txt')
modulos = ler_dados_txt('modulos.txt')

# Monta os blocos de HTML dinamicamente com base no texto
html_info = ""
for chave, valor in informacoes:
    html_info += f'''
                    <div class="info-item">
                        <span class="label">{chave}</span>
                        <span class="value">{valor}</span>
                    </div>'''

html_modulos = ""
for chave, valor in modulos:
    html_modulos += f'''
                    <div class="info-item">
                        <span class="label">{chave}</span>
                        <span class="value">{valor}</span>
                    </div>'''

# Template HTML do site
html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>P84/P85 Information Portal</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header class="hero">
        <div class="hero-content">
            <h1 class="animate-on-load">P84/P85 Information Portal</h1>
            <p class="subtitle animate-on-load delay-1">Floating Production Storage and Offloading Unit</p>
        </div>
        <div class="hero-image-container animate-on-load delay-2">
            <img src="fpso.jpg" alt="FPSO Vessel" class="fpso-image">
        </div>
    </header>

    <main class="container">
        <div class="grid">
            <section class="card fade-in">
                <h2>General Information</h2>
                <div class="info-list">
                    {html_info}
                </div>
            </section>

            <section class="card fade-in">
                <h2>Topside Modules</h2>
                <div class="info-list">
                    {html_modulos}
                </div>
            </section>
        </div>
    </main>

    <footer>
        <div class="footer-content">
            <img src="profile.png" alt="Daniel Alves Anversi" class="profile-pic">
            <div class="developer-info">
                <h3>Developed by Daniel Alves Anversi</h3>
                <p>Electrical Engineer | PETROBRAS</p>
            </div>
        </div>
    </footer>
    <script src="script.js"></script>
</body>
</html>
"""

# Gera o arquivo final
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Sucesso! O arquivo 'index.html' foi gerado com os dados dos seus arquivos TXT.")
