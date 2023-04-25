Python 3.8.5 (default, Jan 27 2021, 15:41:15) 
[GCC 9.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> print "hola"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("hola")?
>>> print ("hola")
hola
>>> print (hola)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print (hola)
NameError: name 'hola' is not defined
>>> hola = 1
>>> print hola
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(hola)?
>>> print (hola)
1
>>> print ("hola") ; print ("adios")
hola
adios
>>> #comentario
>>> 