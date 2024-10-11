minAno = 60*24*365

nasc = int(input("Frequência de nascimentos (minutos): "))
falec = int(input("Frequência de falecimentos (minutos): "))
emigre = int(input("Frequência de emigração (minutos): "))

popInicial = 10000000

res = "Resumo dos dados:"
print(res)
print("-"*len(res))

print("Frequência de nascimentos: ", nasc)
print("Frequência de mortes: ", falec)
print("Frequência de emigrantes: ", emigre)
print("População Inicial: ", popInicial)
est = "Estimativa:"
print(est)
print("-"*len(est))

popFinal = popInicial + nasc*minAno - falec*minAno - emigre*minAno

print("A população ao fim de um ano: ", popFinal)
