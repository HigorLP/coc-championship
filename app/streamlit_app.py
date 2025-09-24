import streamlit as st
from core.classificacao import calcular_classificacao
from core.rodadas import generate_round_robin_pairs
from infra.firestore_repo import FirestorePlayerRepo
import firebase_init

def main():
    st.title("🏆 Coc-Championship - Refactor Demo")

    fb = firebase_init.init_firebase()
    db = fb["db"]
    repo = FirestorePlayerRepo(db)

    st.subheader("👥 Jogadores Ativos")
    players = repo.list_players()
    if not players:
        st.info("Nenhum jogador encontrado.")
    else:
        st.table(players)

    st.subheader("⚙️ Round Robin Demo")
    ids = [p["id"] for p in players]
    rounds = generate_round_robin_pairs(ids)
    st.write(rounds)

if __name__ == "__main__":
    main()
