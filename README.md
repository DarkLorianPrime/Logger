# Logger
Error or info logger in the func 
```Python
@logger('Info for logs')
def print_lower(text):
  return text.lower()
  
print(print_lower('I KNOW YOU WILL SAY HI TO ME IF WE MEET AGAIN'))
```
If your function works correctly, in logs you'll get:
```
==========
/THIS IS TIME/ [INFO] Info for logs #args from decorator
==========
==========
/THIS IS TIME/ [LOADED] print_lower successful execute. #func name.
==========
```
In file you'll get:
```
i know you will say hi to me if we meet again
```
If you leave the decorator argument empty, the INFO field will not be added to the logs.
this example
