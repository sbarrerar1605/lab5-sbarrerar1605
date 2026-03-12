def calc_avg(valores):
    return sum(valores) / len(valores)


def list_shift(valores, incremento):
    for i in range(len(valores)):
        valores[i] = valores[i] + incremento


def print_normalized(valores):
    avg = calc_avg(valores)
    list_shift(valores, -avg)