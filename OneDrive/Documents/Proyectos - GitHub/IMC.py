Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> print("José María San Agustín Velasco")
José María San Agustín Velasco
>>> peso = int(input("Cuál es tu peso?: "))
Cuál es tu peso?: 60
>>> altura = float(input("Cuál es tu altura?: ))
...                      
SyntaxError: unterminated string literal (detected at line 1)
>>> altura = float(input("Cuál es tu altura?: "))
...                      
Cuál es tu altura?: 1.66
>>> imc = peso(altura**2)
...                      
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    imc = peso(altura**2)
TypeError: 'int' object is not callable
>>> imc = peso/(altura**2)
...                      
>>> 
>>> print("Tu Indice de Masa Corporal es: ", imc)
...                      
Tu Indice de Masa Corporal es:  21.773842357381334
