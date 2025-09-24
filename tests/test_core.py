import pytest
from core.rodadas import generate_round_robin_pairs, determinar_vencedor
from core.classificacao import calcular_classificacao

def test_round_robin_even():
    ids = ["a", "b", "c", "d"]
    rounds = generate_round_robin_pairs(ids)
    assert len(rounds) == 3  # n-1 rounds
    flat = [pair for r in rounds for pair in r]
    assert all(isinstance(p, tuple) for p in flat)

def test_vencedor_por_estrelas():
    assert determinar_vencedor(3, 2, 0, 0, 0, 0) == 1
    assert determinar_vencedor(1, 2, 0, 0, 0, 0) == 2

def test_classificacao_basica():
    rodadas = [
        {
            'jogador1_id': 'a', 'jogador2_id': 'b',
            'jogador1': 'Alice', 'jogador2': 'Bob',
            'estrelas_j1': 2, 'estrelas_j2': 1,
            'porc_j1': 80.0, 'porc_j2': 60.0,
            'tempo_j1': 120.0, 'tempo_j2': 150.0
        }
    ]
    df = calcular_classificacao(rodadas)
    assert 'Alice' in df['jogador'].values
    assert df.loc[df['jogador']=='Alice','pontos'].iloc[0] == 1
