# Crie uma tabuada utilizando função e sem a entrada do usuário.
# Incrementei com for

def tabuada(numero):
    for c in range(1, 11):
        print(f'{c} x {numero}: {c*numero}.')

print(tabuada(4))
