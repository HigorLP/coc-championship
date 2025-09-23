# Sistema de Gerenciamento de Liga Interna para Clash of Clans (13º Pelotão)

## Descrição

Coc-Championship é um sistema web simples e eficiente para gerenciar ligas internas de Clash of Clans no formato de pontos corridos (round-robin). Desenvolvido para o 13º Pelotão, o aplicativo permite a criação de temporadas, geração automática de confrontos, registro de resultados de batalhas (baseado em estrelas, porcentagem de destruição e tempo), cálculo de classificação com desempates e visualização pública de rankings e rodadas.

O sistema é construído com **Streamlit** para a interface frontend, **Python** para a lógica de negócios e **Firebase Firestore** como banco de dados NoSQL para armazenamento persistente. A autenticação é baseada em usuários armazenados no Firestore (com hash de senha), com suporte a roles de administrador para operações sensíveis.

**Versão atual:** 1.0.0 (consulte `version.py` para atualizações).

**Objetivo principal:** Facilitar a organização de torneios internos, promovendo engajamento e competição amigável entre jogadores.

## Funcionalidades Principais

- **Autenticação e Roles:**
  - Login simples com usuário e senha (armazenados no Firestore com hash SHA-256).
  - Role de administrador para CRUD de jogadores, criação de temporadas e registro de resultados.

- **Gerenciamento de Jogadores:**
  - Adicionar, editar e excluir (soft-delete) jogadores com nome e TAG opcional.
  - Lista pública de jogadores ativos.

- **Temporadas:**
  - Criação e ativação de temporadas (apenas uma ativa por vez).
  - Geração automática de confrontos round-robin (método do círculo para equilibrar rodadas).
  - Opção de recriar confrontos com backup automático.

- **Confrontos e Resultados:**
  - Visualização de rodadas e confrontos por temporada.
  - Registro de resultados por admin: estrelas (0-3), porcentagem de ataque (0-100%), tempo em segundos.
  - Determinação automática de vencedor com desempates: Estrelas > Porcentagem > Tempo (menor é melhor).
  - Tratamento de empates exatos (marca como "rematch" para refazer).

- **Classificação:**
  - Cálculo automático de pontos (1 por vitória, 0 por derrota).
  - Desempates: Saldo de estrelas > Média de porcentagem de ataque > Tempo médio de ataque (menor é melhor).
  - Visualização em tabela com posição, pontos, vitórias/derrotas/empates, etc.

- **Histórico Individual:**
  - Visualização de confrontos e resultados por jogador na temporada ativa.

- **Segurança e Backup:**
  - Backup automático de rodadas antes de recriação.
  - Soft-delete para jogadores para preservar histórico.

## Requisitos

- **Python:** 3.8+ (testado em 3.10+).
- **Bibliotecas:** 
  - `streamlit` (frontend e UI).
  - `pandas` (manipulação de dados e tabelas).
  - `firebase-admin` (integração com Firestore).
  - `hashlib` e `datetime` (nativos do Python para hash e timestamps).
- **Firebase:** Conta no Google Firebase com projeto configurado (Firestore ativado).
- **Ambiente:** Desenvolvimento local ou deploy em Streamlit Cloud (recomendado para produção).

## Instalação

1. Clone o repositório:
   ```
   git clone https://github.com/seu-usuario/coc-championship.git
   cd coc-championship
   ```

2. Crie e ative um ambiente virtual:
   ```
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
   (Se `requirements.txt` não existir, instale manualmente: `pip install streamlit pandas firebase-admin`).

4. Configure o Firebase (veja seção abaixo).

5. Execute localmente:
   ```
   streamlit run app.py
   ```
   Acesse em `http://localhost:8501`.

## Configuração do Firebase

O sistema usa Firebase Firestore para persistência. Para configurar:

1. Crie um projeto no [Firebase Console](https://console.firebase.google.com/).
2. Gere uma chave de conta de serviço (Service Account Key) em **Project Settings > Service Accounts > Generate New Private Key**.
3. **Localmente:** Salve o JSON como `serviceAccountKey.json` na raiz do projeto (não commitar no git!).
4. **Em produção (Streamlit Cloud):** Use **Streamlit Secrets** para armazenar as credenciais. No arquivo `.streamlit/secrets.toml` ou via interface do Streamlit Cloud, adicione:
   ```
   FIREBASE_TYPE = "service_account"
   FIREBASE_PROJECT_ID = "seu-project-id"
   FIREBASE_PRIVATE_KEY_ID = "seu-private-key-id"
   FIREBASE_PRIVATE_KEY = "-----BEGIN PRIVATE KEY-----\nSUA_CHAVE_PRIVADA\n-----END PRIVATE KEY-----\n"
   FIREBASE_CLIENT_EMAIL = "seu-client-email@project.iam.gserviceaccount.com"
   FIREBASE_CLIENT_ID = "seu-client-id"
   FIREBASE_AUTH_URI = "https://accounts.google.com/o/oauth2/auth"
   FIREBASE_TOKEN_URI = "https://oauth2.googleapis.com/token"
   FIREBASE_AUTH_PROVIDER_X509_CERT_URL = "https://www.googleapis.com/oauth2/v1/certs"
   FIREBASE_CLIENT_X509_CERT_URL = "https://www.googleapis.com/robot/v1/metadata/x509/seu-client-email@project.iam.gserviceaccount.com"
   FIREBASE_UNIVERSE_DOMAIN = "googleapis.com"
   ```
   O código em `firebase_init.py` carrega essas variáveis de ambiente.

5. Crie o primeiro usuário admin executando `create_admin.py`:
   ```
   python create_admin.py
   ```
   Siga as instruções para definir usuário e senha.

**Nota de Segurança:** Rotacione chaves periodicamente. Considere migrar para Firebase Authentication para autenticação mais robusta em futuras versões.

## Uso

- **Login:** Use a barra lateral para autenticar. Admins veem opções extras.
- **Menus Principais:**
  - **Classificação:** Veja o ranking da temporada ativa.
  - **Rodadas:** Lista de confrontos por rodada.
  - **Cadastrar Resultados:** (Admin) Registre resultados de batalhas.
  - **Jogadores:** (Admin) Gerencie jogadores.
  - **Temporadas:** (Admin) Crie e gerencie temporadas, gere/recrie confrontos.
  - **Histórico Individual:** Veja resultados por jogador.
- **Logout:** Botão na barra lateral.

Para mais detalhes sobre fluxos, consulte `projeto_co_c_championship_spec.md`.

## Contribuição

1. Fork o repositório.
2. Crie uma branch: `git checkout -b feature/nova-funcionalidade`.
3. Commit suas mudanças: `git commit -m 'Adiciona nova funcionalidade'`.
4. Push para a branch: `git push origin feature/nova-funcionalidade`.
5. Abra um Pull Request.

Relate issues no GitHub Issues. Siga o CHANGELOG.md para rastrear versões.

## Licença

© 13º Pelotão. Todos os direitos reservados. Desenvolvido por Cabo ~ Loki ~ Necrod.

Este software é de uso interno e não deve ser redistribuído sem permissão. Para mais informações, contate os mantenedores.
