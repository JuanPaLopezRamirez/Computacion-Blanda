
def operacion(minuto_malo):
    div = minuto_malo // 1
    rest = minuto_malo - div
    op = ((rest * 60) / 100)
    resultado = div+ op
    return resultado

