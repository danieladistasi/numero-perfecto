Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> def es_perfecto(n):
...     if n <= 1:
...         return False
...     suma = 1
...     for i in range(2, int(n ** 0.5) + 1):
...         if n % i == 0:
...             suma += i
...             if i != n // i:
...                 suma += n // i
...     return suma == n
...
