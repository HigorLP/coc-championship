import pandas as pd
from typing import List, Dict
from .rodadas import determinar_vencedor

def calcular_classificacao(rodadas: List[Dict]) -> pd.DataFrame:
    """
    Calcula tabela de classificação a partir de uma lista de rodadas (dicts).
    Espera rodadas no formato:
      {
        'jogador1_id': str,
        'jogador2_id': str,
        'jogador1': str,
        'jogador2': str,
        'estrelas_j1': int,
        'estrelas_j2': int,
        'porc_j1': float,
        'porc_j2': float,
        'tempo_j1': float,
        'tempo_j2': float
      }
    Retorna DataFrame com colunas de pontos, vitórias, etc.
    """
    players = {}

    for row in rodadas:
        j1, j2 = row['jogador1_id'], row['jogador2_id']
        n1, n2 = row['jogador1'], row['jogador2']

        for pid, nome in [(j1, n1), (j2, n2)]:
            if pid not in players:
                players[pid] = {
                    'jogador': nome,
                    'pontos': 0,
                    'vitorias': 0,
                    'derrotas': 0,
                    'empates': 0,
                    'est_ataque_total': 0,
                    'est_defesa_total': 0,
                    'porc_ataque_list': [],
                    'tempo_ataque_list': [],
                    'partidas': 0
                }

        e1, e2 = row.get('estrelas_j1') or 0, row.get('estrelas_j2') or 0
        p1, p2 = row.get('porc_j1') or 0.0, row.get('porc_j2') or 0.0
        t1, t2 = row.get('tempo_j1') or 0.0, row.get('tempo_j2') or 0.0

        players[j1]['partidas'] += 1
        players[j2]['partidas'] += 1
        players[j1]['est_ataque_total'] += e1
        players[j1]['est_defesa_total'] += e2
        players[j2]['est_ataque_total'] += e2
        players[j2]['est_defesa_total'] += e1
        players[j1]['porc_ataque_list'].append(p1)
        players[j1]['tempo_ataque_list'].append(t1)
        players[j2]['porc_ataque_list'].append(p2)
        players[j2]['tempo_ataque_list'].append(t2)

        res = determinar_vencedor(e1, e2, p1, p2, t1, t2)
        if res == 1:
            players[j1]['pontos'] += 1
            players[j1]['vitorias'] += 1
            players[j2]['derrotas'] += 1
        elif res == 2:
            players[j2]['pontos'] += 1
            players[j2]['vitorias'] += 1
            players[j1]['derrotas'] += 1
        elif res == 0:
            players[j1]['empates'] += 1
            players[j2]['empates'] += 1

    rows = []
    for pid, d in players.items():
        porc_avg = sum(d['porc_ataque_list']) / len(d['porc_ataque_list']) if d['porc_ataque_list'] else 0.0
        tempo_avg = sum(d['tempo_ataque_list']) / len(d['tempo_ataque_list']) if d['tempo_ataque_list'] else 0.0
        saldo = d['est_ataque_total'] - d['est_defesa_total']
        rows.append({
            'jogador_id': pid,
            'jogador': d['jogador'],
            'pontos': d['pontos'],
            'vitorias': d['vitorias'],
            'derrotas': d['derrotas'],
            'empates': d['empates'],
            'saldo_estrelas': saldo,
            'porc_ataque_avg': round(porc_avg,2),
            'tempo_ataque_avg': round(tempo_avg,2),
            'partidas': d['partidas']
        })

    df = pd.DataFrame(rows)
    if df.empty:
        return df
    df = df.sort_values(by=['pontos','saldo_estrelas','porc_ataque_avg','tempo_ataque_avg'], ascending=[False, False, False, True])
    df.insert(0, 'Posição', range(1, len(df)+1))
    return df.reset_index(drop=True)
