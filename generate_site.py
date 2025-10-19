#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur de site HTML pour "Les Équations de l'Espace"
Convertit les fichiers Markdown en pages HTML avec navigation
"""

import os
import re
from pathlib import Path

# Configuration
MARKDOWN_FILES = [
    ("index", "Introduction.md", "🏠 Introduction"),
    ("chapitre-1", "Chapitre_1_Intelligence_en_orbite.md", "Chapitre 1: L'intelligence en orbite"),
    ("chapitre-2", "Chapitre_2_Langage_trajectoires.md", "Chapitre 2: Le langage des trajectoires"),
    ("chapitre-3", "Chapitre_3_Calcul_vol_suborbital.md", "Chapitre 3: Le calcul du vol suborbital"),
    ("chapitre-4", "Chapitre_4_Geometrie_espace.md", "Chapitre 4: La géométrie de l'espace"),
    ("chapitre-5", "Chapitre_5_Vol_orbital_John_Glenn.md", "Chapitre 5: Le vol orbital de John Glenn"),
    ("chapitre-6", "Chapitre_6_Mathematiques_Lune.md", "Chapitre 6: Les mathématiques de la Lune"),
    ("chapitre-7", "Chapitre_7_Equations_retour_Terre.md", "Chapitre 7: Les équations du retour sur Terre"),
    ("chapitre-8", "Chapitre_8_Feuille_cosmos.md", "Chapitre 8: De la feuille au cosmos"),
    ("chapitre-9", "Chapitre_9_Heritage_transmission.md", "Chapitre 9: Héritage et transmission"),
    ("annexes", "Annexes.md", "📚 Annexes"),
    ("formules", "Annexes_Formules_Calculs.md", "📐 Formules et Calculs"),
]

def convert_markdown_to_html(markdown_content):
    """Conversion simple de Markdown en HTML"""
    html = markdown_content
    
    # Titres
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
    
    # Gras et italique
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    
    # Listes
    html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'(<li>.*</li>\n?)+', r'<ul>\g<0></ul>', html)
    
    # Citations
    html = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', html, flags=re.MULTILINE)
    
    # Équations inline \( \)
    html = re.sub(r'\\\((.+?)\\\)', r'<span class="math-inline">\(\1\)</span>', html)
    
    # Équations block \[ \]
    html = re.sub(r'\\\[([\s\S]+?)\\\]', r'<div class="math-block">\[\1\]</div>', html, flags=re.MULTILINE)
    
    # Paragraphes
    lines = html.split('\n')
    in_block = False
    result = []
    
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('<') or not stripped:
            result.append(line)
        else:
            if not in_block:
                result.append('<p>' + line)
                in_block = True
            else:
                result.append(line)
                
            if not lines[lines.index(line)+1:] or not lines[lines.index(line)+1].strip():
                if in_block:
                    result[-1] += '</p>'
                    in_block = False
    
    return '\n'.join(result)

def generate_menu(current_page):
    """Génère le menu de navigation"""
    menu_html = '<nav class="sidebar">\n'
    menu_html += '<div class="logo">\n'
    menu_html += '<h2>📖 Les Équations de l\'Espace</h2>\n'
    menu_html += '<p class="subtitle">L\'Héritage de Katherine Johnson</p>\n'
    menu_html += '</div>\n'
    menu_html += '<ul class="menu">\n'
    
    for page_id, _, title in MARKDOWN_FILES:
        active = 'class="active"' if page_id == current_page else ''
        menu_html += f'  <li><a href="{page_id}.html" {active}>{title}</a></li>\n'
    
    menu_html += '</ul>\n'
    menu_html += '<div class="footer">\n'
    menu_html += '<p>© 2025 Michael Germini</p>\n'
    menu_html += '<p><a href="https://github.com/michaelgermini/Les-Equations-de-l-Espace" target="_blank">GitHub</a></p>\n'
    menu_html += '</div>\n'
    menu_html += '</nav>\n'
    
    return menu_html

def generate_html_template(title, content, current_page):
    """Génère le template HTML complet"""
    menu = generate_menu(current_page)
    
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - Les Équations de l'Espace</title>
    <link rel="stylesheet" href="style.css">
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
</head>
<body>
    {menu}
    <main class="content">
        <article>
            {content}
        </article>
    </main>
</body>
</html>"""

def generate_css():
    """Génère le fichier CSS"""
    css = """/* Style pour Les Équations de l'Espace */
:root {
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    --accent-color: #e74c3c;
    --bg-color: #ecf0f1;
    --text-color: #2c3e50;
    --sidebar-width: 300px;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    line-height: 1.6;
    color: var(--text-color);
    background-color: var(--bg-color);
    display: flex;
}

/* Sidebar Navigation */
.sidebar {
    width: var(--sidebar-width);
    height: 100vh;
    position: fixed;
    left: 0;
    top: 0;
    background: linear-gradient(135deg, var(--primary-color) 0%, #34495e 100%);
    color: white;
    padding: 20px;
    overflow-y: auto;
    box-shadow: 2px 0 10px rgba(0,0,0,0.1);
}

.logo h2 {
    font-size: 1.4em;
    margin-bottom: 5px;
    color: white;
}

.subtitle {
    font-size: 0.9em;
    color: #bdc3c7;
    margin-bottom: 30px;
    font-style: italic;
}

.menu {
    list-style: none;
}

.menu li {
    margin-bottom: 8px;
}

.menu a {
    display: block;
    color: #ecf0f1;
    text-decoration: none;
    padding: 12px 15px;
    border-radius: 8px;
    transition: all 0.3s ease;
    font-size: 0.95em;
}

.menu a:hover {
    background-color: rgba(255, 255, 255, 0.1);
    padding-left: 20px;
    color: var(--secondary-color);
}

.menu a.active {
    background-color: var(--secondary-color);
    color: white;
    font-weight: bold;
}

.footer {
    margin-top: 30px;
    padding-top: 20px;
    border-top: 1px solid rgba(255,255,255,0.2);
    font-size: 0.85em;
}

.footer a {
    color: var(--secondary-color);
    text-decoration: none;
}

/* Main Content */
.content {
    margin-left: var(--sidebar-width);
    padding: 40px 60px;
    width: calc(100% - var(--sidebar-width));
    max-width: 1200px;
}

article {
    background: white;
    padding: 50px;
    border-radius: 12px;
    box-shadow: 0 2px 20px rgba(0,0,0,0.08);
}

/* Typography */
h1 {
    color: var(--primary-color);
    font-size: 2.5em;
    margin-bottom: 20px;
    border-bottom: 3px solid var(--secondary-color);
    padding-bottom: 15px;
}

h2 {
    color: var(--primary-color);
    font-size: 2em;
    margin-top: 40px;
    margin-bottom: 20px;
    padding-left: 15px;
    border-left: 5px solid var(--secondary-color);
}

h3 {
    color: var(--primary-color);
    font-size: 1.5em;
    margin-top: 30px;
    margin-bottom: 15px;
}

h4 {
    color: var(--secondary-color);
    font-size: 1.2em;
    margin-top: 25px;
    margin-bottom: 10px;
}

p {
    margin-bottom: 15px;
    text-align: justify;
}

strong {
    color: var(--accent-color);
    font-weight: 600;
}

em {
    color: var(--secondary-color);
}

/* Lists */
ul, ol {
    margin: 15px 0 15px 40px;
}

li {
    margin-bottom: 8px;
}

/* Blockquotes */
blockquote {
    background: #f8f9fa;
    border-left: 4px solid var(--secondary-color);
    padding: 15px 20px;
    margin: 20px 0;
    font-style: italic;
    color: #555;
}

/* Math */
.math-inline {
    color: var(--secondary-color);
    font-family: 'Cambria Math', 'Times New Roman', serif;
}

.math-block {
    background: #f8f9fa;
    padding: 20px;
    margin: 25px 0;
    border-radius: 8px;
    overflow-x: auto;
    text-align: center;
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 25px 0;
}

th, td {
    padding: 12px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}

th {
    background-color: var(--primary-color);
    color: white;
    font-weight: 600;
}

tr:hover {
    background-color: #f5f5f5;
}

/* Responsive */
@media (max-width: 768px) {
    .sidebar {
        width: 250px;
    }
    
    .content {
        margin-left: 250px;
        padding: 20px;
        width: calc(100% - 250px);
    }
    
    article {
        padding: 30px;
    }
}

@media (max-width: 576px) {
    .sidebar {
        width: 100%;
        height: auto;
        position: relative;
    }
    
    .content {
        margin-left: 0;
        width: 100%;
        padding: 15px;
    }
    
    article {
        padding: 20px;
    }
}
"""
    return css

def generate_site():
    """Génère tout le site HTML"""
    output_dir = Path("www")
    output_dir.mkdir(exist_ok=True)
    
    # Génère le CSS
    css_path = output_dir / "style.css"
    css_path.write_text(generate_css(), encoding='utf-8')
    print(f"✅ Créé: {css_path}")
    
    # Génère chaque page HTML
    for page_id, markdown_file, title in MARKDOWN_FILES:
        md_path = Path(markdown_file)
        
        if not md_path.exists():
            print(f"⚠️  Fichier non trouvé: {markdown_file}")
            continue
        
        # Lit le contenu Markdown
        markdown_content = md_path.read_text(encoding='utf-8')
        
        # Convertit en HTML
        html_content = convert_markdown_to_html(markdown_content)
        
        # Génère la page complète
        full_html = generate_html_template(title, html_content, page_id)
        
        # Écrit le fichier HTML
        html_path = output_dir / f"{page_id}.html"
        html_path.write_text(full_html, encoding='utf-8')
        print(f"✅ Créé: {html_path}")
    
    print(f"\n🎉 Site généré avec succès dans le dossier 'www'")
    print(f"📂 Ouvrez www/index.html dans votre navigateur")

if __name__ == "__main__":
    generate_site()

