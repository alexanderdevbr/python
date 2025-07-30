# Trabalhando com Strings
https://docs.python.org/pt-br/3/library/string.html
https://docs.python.org/pt-br/3/library/stdtypes.html#textseq

```Python
curso = "pyThOn"
print(curso.upper())           # PYTHON
print(curso.lower())           # python
print(curso.title())           # Python

curso = "  pyThOn "
print(curso.strip()  + ".")    # pyThOn.
print(curso.rstrip() + ".")    #   pyThOn.
print(curso.lstrip() + ".")    # pyThOn .

curso = "Python"
print(curso.center(10, "*"))   # **Python**
print(".".join(curso))         # P.y.t.h.o.n
```
## Interpolação de Strings
### Old Styl -> Depreciado
```Python
nome = "Alexander"
idade = 43
profissao = "Servidor Público"

print("Olá, me chamo %s. Eu tenho %d anos de idade, atualmente sou %s." % (nome, idade, profissao))
# Olá, me chamo Alexander. Eu tenho 43 anos de idade, atualmente sou Servidor Público.
```
### Método Format
```Python
nome = "Alexander"
idade = 43
profissao = "Servidor Público"

print("Olá, me chamo {}. Eu tenho {} anos de idade, atualmente sou {}.".format(nome, idade, profissao))
# Olá, me chamo Alexander. Eu tenho 43 anos de idade, atualmente sou Servidor Público.

print("Olá, me chamo {1}. Eu tenho {0} anos de idade, atualmente sou {2}.".format(idade, nome, profissao))
# Olá, me chamo Alexander. Eu tenho 43 anos de idade, atualmente sou Servidor Público.

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, atualmente sou {profissao}.".format(idade=idade, nome=nome, profissao=profissao))
# Olá, me chamo Alexander. Eu tenho 43 anos de idade, atualmente sou Servidor Público.

dados = {"nome": "Alexander", "idade": 43}
print("Nome: {nome}. Eu tenho {idade} anos de idade.".format(**dados))
# Nome: Alexander. Eu tenho 43 anos de idade.
```

### f-string
```Python
nome = "Alexander"
idade = 43
profissao = "Servidor Público"
salario = 1234.567

print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, atualmente sou {profissao}, meu salário é {salario:10.2f}.")
# Olá, me chamo Alexander. Eu tenho 43 anos de idade, atualmente sou Servidor Público, meu salário é    1234.57.
```

## Utilizando diversos comandos aninhados
```Python
titulo = ("[Alexander Moreira de Morais]" 
            .replace("[", "")   
            .replace("]", "")   
            .title()            
            .center(40, "*"))
print(titulo)
# ******Alexander Moreira De Morais*******
```

## Fatiamento de String
```Python
>>> nome = "Alexander Moreira de Morais"
>>> nome[0]
'A'
>>> nome[:9]
'Alexander'
>>> nome[10:]
'Moreira de Morais'
>>> nome[10:17]
'Moreira'
>>> nome[10:17:2]
'Mria'
>>> nome[:]
'Alexander Moreira de Morais'
>>> nome[::-1]
'siaroM ed arieroM rednaxelA'
```

## Strings Multiplas Linhas / triplas
```Python
nome = "Alexander"
msg = f"""
    Olá meu nome é {nome},
Eu estou aprendendo Python.
        Essa mensagem tem diferentes recuos.
"""

print(msg)
#    Olá meu nome é Alexander,
#Eu estou aprendendo Python.
#        Essa mensagem tem diferentes recuos.
```