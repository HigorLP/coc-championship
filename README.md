# 📘 README.md (versão para branch `refactor/clean-architecture`)

# 🏆 Coc-Championship

Projeto de **organização de campeonatos internos de Clash of Clans**, com:
- Painel administrativo para jogadores, temporadas e rodadas
- Classificação automática
- Controle de resultados e transparência
- Interface pública em **Streamlit**
- Persistência em **Firestore**

---

## 🚀 Tecnologias
- [Python 3.10+](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Firebase Admin SDK](https://firebase.google.com/docs/admin/setup)
- [Firestore](https://firebase.google.com/docs/firestore)
- [Pytest](https://docs.pytest.org/) para testes
- Ferramentas de qualidade: **Black**, **Isort**, **Flake8**, **Pre-commit**
- CI/CD via **GitHub Actions**

---

## 📂 Estrutura (Clean Architecture leve)

```

project-root/
│
├── app/                # Interface Streamlit
│   └── streamlit\_app.py
│
├── core/               # Regras de negócio puras
│   ├── rodadas.py
│   ├── classificacao.py
│   ├── jogadores.py
│   └── temporadas.py
│
├── infra/              # Adapters (repos Firestore, auth, etc)
│   ├── repositories.py
│   ├── firestore\_repo.py
│   └── **init**.py
│
├── tests/              # Testes unitários
│   ├── test\_core.py
│   ├── test\_infra.py
│   └── test\_temporada\_repo.py
│
├── .github/
│   └── workflows/ci.yml   # Lint + testes
│
├── requirements.txt
├── requirements-dev.txt
├── pyproject.toml
├── .flake8
├── .pre-commit-config.yaml
└── README.md

````

---

## 🛠️ Setup de Desenvolvimento

### 1. Clone e instale dependências
```bash
git clone https://github.com/<seu-repo>/coc-championship.git
cd coc-championship
git checkout refactor/clean-architecture

# dependências principais
pip install -r requirements.txt

# dependências de dev
pip install -r requirements-dev.txt
````

### 2. Configure o Firebase

Crie um arquivo `firebase_init.py` (já existe no projeto) com as credenciais.
Exemplo mínimo:

```python
import firebase_admin
from firebase_admin import credentials, firestore

def init_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate("path/to/cred.json")
        firebase_admin.initialize_app(cred)
    db = firestore.client()
    return {"db": db}
```

### 3. Pre-commit hooks

```bash
pre-commit install
```

Agora sempre que fizer `git commit`, serão rodados automaticamente:

* `black` (formatador)
* `isort` (organização de imports)
* `flake8` (linter)

---

## ▶️ Rodando o app

```bash
streamlit run app/streamlit_app.py
```

---

## 🧪 Rodando testes

```bash
pytest
```

---

## 🤝 Contribuindo

### Branches

* `main` → produção estável
* `deploy` → versão de deploy/testes
* `refactor/clean-architecture` → branch de refatoração atual

Crie branches a partir de `refactor/clean-architecture`:

```bash
git checkout refactor/clean-architecture
git pull
git checkout -b feature/<nome>
```

### Padrão de commits

Adotar **Conventional Commits**:

* `feat:` nova funcionalidade
* `fix:` correção
* `chore:` manutenção (CI, docs, dependências)
* `refactor:` refatoração sem mudar comportamento

Exemplo:

```
feat(core): adicionar cálculo de classificação de rodadas
```

### PR Checklist

* [ ] Código formatado com black
* [ ] Imports organizados com isort
* [ ] Flake8 sem erros
* [ ] Testes escritos/atualizados
* [ ] Revisado por pelo menos 1 dev

---

## 🧭 Roadmap (alto nível)

1. Refatoração para Clean Architecture (em andamento)
2. Autenticação via Firebase Auth
3. Integração com API Supercell
4. Notificações em Discord
5. Multi-tenant (suporte a múltiplos clãs)

```