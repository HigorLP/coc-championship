from abc import ABC, abstractmethod
from typing import List, Dict, Optional

class PlayerRepo(ABC):
    @abstractmethod
    def list_players(self, only_active: bool = True) -> List[Dict]:
        pass

    @abstractmethod
    def add_player(self, nome: str, tag: Optional[str]) -> str:
        pass

    @abstractmethod
    def update_player(self, player_id: str, nome: str, tag: Optional[str]) -> None:
        pass

    @abstractmethod
    def soft_delete(self, player_id: str) -> None:
        pass


class TemporadaRepo(ABC):
    @abstractmethod
    def create_temporada(self, data: Dict) -> str:
        pass

    @abstractmethod
    def get_active_temporada(self) -> Optional[Dict]:
        pass

    @abstractmethod
    def list_temporadas(self) -> List[Dict]:
        pass


class RodadaRepo(ABC):
    @abstractmethod
    def add_rodada(self, temporada_id: str, data: Dict) -> str:
        pass

    @abstractmethod
    def get_rodadas_por_temporada(self, temporada_id: str) -> List[Dict]:
        pass

    @abstractmethod
    def update_rodada(self, rodada_id: str, data: Dict) -> None:
        pass


class UserRepo(ABC):
    @abstractmethod
    def create_user(self, email: str, password: str, is_admin: bool = False) -> str:
        pass

    @abstractmethod
    def get_user(self, user_id: str) -> Optional[Dict]:
        pass

    @abstractmethod
    def admin_exists(self) -> bool:
        pass
