# Flask no Vercel - Exemplo Básico

Este é um exemplo mínimo de uma aplicação Flask configurada para deploy no Vercel, que retorna uma mensagem simples "Hello, Clancy".

## 📋 Pré-requisitos

- Conta no [Vercel](https://vercel.com)
- Git instalado localmente (opcional)
- Python 3.6+ instalado localmente (para testes)

## 🚀 Como fazer deploy no Vercel

### Método 1: Via interface web

1. Faça um fork deste repositório ou crie um novo com os arquivos
2. Acesse o [Vercel Dashboard](https://vercel.com/dashboard)
3. Clique em "Add New" > "Project"
4. Conecte seu repositório GitHub
5. Selecione o repositório com este projeto
6. Nas configurações:
   - Certifique-se que o Python está selecionado como runtime
   - Não é necessário alterar outras configurações
7. Clique em "Deploy"

### Método 2: Via Vercel CLI

1. Instale o Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Faça login:
   ```bash
   vercel login
   ```

3. No diretório do projeto, execute:
   ```bash
   vercel
   ```
4. Siga as instruções no terminal

## 🏗 Estrutura do Projeto

```
/flask-vercel
│   app.py            # Aplicação Flask principal
│   requirements.txt  # Dependências do Python
│   vercel.json       # Configuração do Vercel
│   wsgi.py           # Ponte WSGI para o Vercel
```

## 🔧 Arquivos Explicados

### app.py
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, Clancy"

if __name__ == '__main__':
    app.run()
```

### requirements.txt
```
flask==2.0.1
```

### vercel.json
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

### wsgi.py
```python
from app import app

if __name__ == "__main__":
    app.run()
```

## ⚠️ Limitações

- O Vercel tem suporte limitado para aplicações Flask (é mais otimizado para funções serverless)
- Para aplicações mais complexas, considere serviços como Render, Railway ou Heroku
- O cold start pode ser perceptível em aplicações pouco acessadas

