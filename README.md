# 📝 ToDo List - Flask App

Aplicativo web simples de lista de tarefas criado com [Flask](https://flask.palletsprojects.com/), utilizando uma arquitetura organizada por blueprints e templates.

## 🔧 Funcionalidades
- Adicionar, listar e remover tarefas
- Organização modular com Blueprints
- Interface com HTML, CSS e JS
- Banco de dados SQLite integrado

## 🚀 Tecnologias
- Python 3.x
- Flask
- SQLite
- HTML5 + CSS3 + JavaScript

## 📁 Estrutura do Projeto
```
📦 ToDoList\
│
├── app\
│   ├── blueprint\
│   │   ├── atividades\
│   │   ├── atividadesform\
│   │   └── home\
│   ├── config\
│   └── __init__.py
│
├── static\
│   ├── css\
│   └── js\
├── templates\
│   └── [subpastas]
│
├── database.db
├── main.py
├── requirements.txt
└── .gitignore
```

## ▶️ Como rodar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repo.git
   cd nome-do-repo
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv env
   source env/bin/activate  # Linux/macOS
   env\Scripts\activate     # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Rode o app:
   ```bash
   python main.py
   ```

## 📸 Imagens (opcional)
Adicione prints da tela inicial, lista de tarefas e formulário.

## 📄 Licença
Este projeto é de uso livre para fins educacionais e de portfólio.
