from typing import Dict

def validar_temporada(data: Dict) -> bool:
    """
    Valida dados mínimos de temporada.
    """
    return bool(data.get("nome"))
