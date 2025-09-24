from typing import List, Dict, Optional
from firebase_admin import firestore
from .repositories import PlayerRepo, TemporadaRepo, RodadaRepo, UserRepo

class FirestorePlayerRepo(PlayerRepo):
    def __init__(self, db: firestore.Client):
        self.db = db

    def list_players(self, only_active: bool = True) -> List[Dict]:
        query = self.db.collection("jogadores")
        if only_active:
            query = query.where("ativo", "==", True)
        docs = list(query.stream())
        return [doc.to_dict() | {"id": doc.id} for doc in docs]

    def add_player(self, nome: str, tag: Optional[str]) -> str:
        data = {"nome": nome, "tag": tag, "ativo": True}
        doc_ref = self.db.collection("jogadores").document()
        doc_ref.set(data)
        return doc_ref.id

    def update_player(self, player_id: str, nome: str, tag: Optional[str]) -> None:
        self.db.collection("jogadores").document(player_id).update(
            {"nome": nome, "tag": tag}
        )

    def soft_delete(self, player_id: str) -> None:
        self.db.collection("jogadores").document(player_id).update({"ativo": False})


class FirestoreTemporadaRepo(TemporadaRepo):
    def __init__(self, db: firestore.Client):
        self.db = db

    def create_temporada(self, data: Dict) -> str:
        doc_ref = self.db.collection("temporadas").document()
        doc_ref.set(data)
        return doc_ref.id

    def get_active_temporada(self) -> Optional[Dict]:
        docs = self.db.collection("temporadas").where("ativa", "==", True).limit(1).stream()
        for doc in docs:
            return doc.to_dict() | {"id": doc.id}
        return None

    def list_temporadas(self) -> List[Dict]:
        docs = self.db.collection("temporadas").stream()
        return [doc.to_dict() | {"id": doc.id} for doc in docs]


class FirestoreRodadaRepo(RodadaRepo):
    def __init__(self, db: firestore.Client):
        self.db = db

    def add_rodada(self, temporada_id: str, data: Dict) -> str:
        doc_ref = self.db.collection("temporadas").document(temporada_id).collection("rodadas").document()
        doc_ref.set(data)
        return doc_ref.id

    def get_rodadas_por_temporada(self, temporada_id: str) -> List[Dict]:
        docs = self.db.collection("temporadas").document(temporada_id).collection("rodadas").stream()
        return [doc.to_dict() | {"id": doc.id} for doc in docs]

    def update_rodada(self, rodada_id: str, data: Dict) -> None:
        # OBS: estamos assumindo que rodada está em subcoleção única
        raise NotImplementedError("Atualização de rodadas precisa do temporada_id.")


class FirestoreUserRepo(UserRepo):
    def __init__(self, db: firestore.Client):
        self.db = db

    def create_user(self, email: str, password: str, is_admin: bool = False) -> str:
        data = {"email": email, "password": password, "is_admin": is_admin}
        doc_ref = self.db.collection("usuarios").document()
        doc_ref.set(data)
        return doc_ref.id

    def get_user(self, user_id: str) -> Optional[Dict]:
        doc = self.db.collection("usuarios").document(user_id).get()
        if doc.exists:
            return doc.to_dict() | {"id": doc.id}
        return None

    def admin_exists(self) -> bool:
        docs = self.db.collection("usuarios").where("is_admin", "==", True).limit(1).stream()
        return any(True for _ in docs)
