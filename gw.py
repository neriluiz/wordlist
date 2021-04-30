# testar autenticação e confidencialidade
# ferramenta de força bruta
import itertools

string = input("String a ser permutada: ")

# Com o segundo argumento, a permutação vira combinação:
resultado = itertools.permutations(string)

for i in resultado:
    print(''.join(i))