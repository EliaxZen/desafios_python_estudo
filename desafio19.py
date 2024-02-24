# Crie uma função chamada diff_tempo, que aceita dois strings no formato HH:MM:SS e retorna a
# diferença de tempo entre eles em um string de mesmo formato.
# Exemplodeuso:
import datetime


inicio = '08:34:21'
fim = '13:55:09'

def diff_tempo(inicio, fim):
    formato = '%H:%M:%S'
    dt_inicio = datetime.datetime.strptime(inicio, formato)
    dt_fim = datetime.datetime.strptime(fim, formato)
    delta = dt_fim - dt_inicio
    delta_seconds = delta.total_seconds()
    h = delta_seconds // 3600
    m = (delta_seconds % 3600) // 60
    s = delta_seconds % 60
    return f'{int(h)}:{int(m)}:{int(s)}'

diff = diff_tempo(inicio, fim)
print(diff)
# output:
# 5:20:48