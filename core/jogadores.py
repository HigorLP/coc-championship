from typing import Dict

def validar_jogador(data: Dict) -> bool:
    """
    Valida dados mínimos de jogador.
    """
    return bool(data.get("nome"))
