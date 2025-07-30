# Trabalhando com memória

```Python
>>> var_nome = 'Alexander Moreira de Morais'
>>> id(var_nome)
1211256222976
>>> hex(id(var_nome))
'0x11a047f3500'
>>> import ctypes
>>> ctypes.cast(1211256222976, ctypes.py_object).value
'Alexander Moreira de Morais'
```