# Par ou ímpar

def par_ou_impar(numero):
    resto_da_divisão = numero % 2
    if resto_da_divisão == 0:
        return(print('Esse número é par!'))
    else:
        return(print('Esse número é ímpar!'))

print(par_ou_impar(3))
