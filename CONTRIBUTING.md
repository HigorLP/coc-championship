# 📘 CONTRIBUTING.md

# 🤝 Guia de Contribuição

Obrigado pelo interesse em contribuir para o **Coc-Championship** 🏆  
Este documento define as práticas e padrões adotados no projeto.

---

## 🚀 Como começar

### 1. Fork e clone
```bash
git clone https://github.com/<seu-repo>/coc-championship.git
cd coc-championship
````

### 2. Escolha a branch base

* `main` → produção estável
* `deploy` → branch de deploy/testes
* `refactor/clean-architecture` → **branch de refatoração atual**

Sempre crie suas features a partir da branch **refactor/clean-architecture**:

```bash
git checkout refactor/clean-architecture
git pull
git checkout -b feature/<nome>
```

---

## 📦 Setup do ambiente

### Dependências

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Firebase

Crie um arquivo `firebase_init.py` (já existe no projeto).
Defina as credenciais no formato:

```python
cred = credentials.Certificate("path/to/cred.json")
```

### Pre-commit hooks

```bash
pre-commit install
```

Agora **black**, **isort** e **flake8** rodam em cada commit.

---

## 🧪 Testes

Rodar todos os testes:

```bash
pytest
```

Rodar com mais detalhes:

```bash
pytest -v --maxfail=1 --disable-warnings
```

---

## ✍️ Padrão de commits

Usamos [Conventional Commits](https://www.conventionalcommits.org/):

* `feat:` → nova funcionalidade
* `fix:` → correção de bug
* `refactor:` → refatoração sem mudar comportamento
* `docs:` → documentação (README, comentários)
* `test:` → testes adicionados ou corrigidos
* `chore:` → manutenção (deps, CI, configs)

Exemplo:

```
feat(core): adicionar cálculo de classificação de rodadas
```

---

## 🔀 Pull Requests

Checklist antes de abrir PR:

* [ ] Branch criada a partir de `refactor/clean-architecture`
* [ ] Código formatado com black (`black .`)
* [ ] Imports organizados com isort (`isort .`)
* [ ] Linter sem erros (`flake8 .`)
* [ ] Testes escritos/atualizados (`pytest`)
* [ ] Checklist preenchido no PR template
* [ ] Revisão solicitada a pelo menos 1 dev

---

## 📂 Estrutura de pastas (resumida)

```
app/            -> Interface (Streamlit)
core/           -> Regras de negócio puras
infra/          -> Acesso a dados (Firestore, Auth)
tests/          -> Testes unitários
.github/        -> Workflows CI/CD
```

---

## 💡 Boas práticas de código

* Regra de negócio **nunca** deve importar diretamente Firebase ou Streamlit.
* Use **tipagem (type hints)** sempre que possível.
* Escreva funções **pequenas e coesas**.
* Prefira **funções puras** em `core/`.
* Escreva **testes unitários** para cada função adicionada ou alterada.

---

## 📅 Fluxo de trabalho recomendado

1. Escolher issue / abrir nova issue.
2. Criar branch a partir de `refactor/clean-architecture`.
3. Implementar feature + testes.
4. Rodar linters e testes localmente.
5. Abrir PR com descrição clara.
6. Aguardar revisão de outro dev.
7. Merge feito apenas após aprovação.

---

## 🧭 Roadmap (alto nível)

1. Refatoração → Clean Architecture
2. Autenticação → Firebase Auth
3. Integração API Supercell
4. Notificações (Discord)
5. Multi-tenant (suporte a múltiplos clãs)

---

## 📣 Dúvidas / Suporte

Abra uma issue com a label **question** ou pergunte diretamente no grupo de devs do projeto.

```

---

# 📝 Commit sugerido

Assunto:
```

docs: adicionar guia CONTRIBUTING.md

```

Mensagem:
```

* Criado documento CONTRIBUTING.md com instruções de contribuição
* Explica setup de ambiente, fluxo de trabalho, padrões de commit e PR
* Define boas práticas de código e estrutura do projeto

```