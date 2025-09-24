from typing import List, Tuple, Optional

def generate_round_robin_pairs(ids: List[str]) -> List[List[Tuple[str, str]]]:
    """
    Gera pares round-robin (método do círculo).
    Entrada: lista de IDs de jogadores.
    Saída: lista de rodadas, cada rodada é uma lista de pares (tuplas).
    """
    n = len(ids)
    if n < 2:
        return []

    ids = list(ids)
    if n % 2 == 1:
        ids.append(None)  # bye
        n += 1

    rounds = []
    arr = ids[:]
    for i in range(n - 1):
        pairs = []
        for j in range(n // 2):
            a, b = arr[j], arr[n - 1 - j]
            if a and b:
                pairs.append((a, b))
        arr = [arr[0]] + [arr[-1]] + arr[1:-1]
        rounds.append(pairs)
    return rounds


def determinar_vencedor(
    e1: Optional[int], e2: Optional[int],
    p1: Optional[float], p2: Optional[float],
    t1: Optional[float], t2: Optional[float]
) -> Optional[int]:
    """
    Determina vencedor baseado em estrelas -> porcentagem -> tempo.
    Retorna:
      1 -> jogador1 vence
      2 -> jogador2 vence
      0 -> empate/rematch
      None -> indefinido
    """
    if e1 is None or e2 is None:
        return None
    if e1 > e2:
        return 1
    if e2 > e1:
        return 2
    if p1 is None or p2 is None:
        return None
    if p1 > p2:
        return 1
    if p2 > p1:
        return 2
    if t1 is None or t2 is None:
        return None
    if t1 < t2:
        return 1
    if t2 < t1:
        return 2
    return 0
