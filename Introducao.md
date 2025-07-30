# Laços de repetição
## For
```Python
print("Tabuada de 5")
for i in range(0, 51, 5):
    print(i)

```
```Python
texto = "Python is Fun!!!"
VOGAIS = "aeiou"
for letra in texto:
    if letra in VOGAIS:
        print(letra, end="")
```

## While
```Python
opcao = -1
while opcao != 0:
    opcao = int(input("Informe opção, 0 para sair! "))
    print(f"Opção escolhida: {opcao}")
```

# Listas
```Python
nomes = ['Alexander', 'Jessica', 'Bob']
for n in nomes:
    print(n)
```

# Tuplas
```Python
carros = ('Golf', 'Civic')
print(carros)
```

# Ternario
```Python
var = 10
resultado = 'verdadeiro' if var >= 10 else 'falso'
print(resultado)
```