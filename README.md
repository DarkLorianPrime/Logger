# Logger
Error or info logger in the func 
```Python
@logger('Info for logs')
def print_lower(text):
  return text.lower()
  
print(print_lower('I KNOW YOU WILL SAY HI TO ME IF WE MEET AGAIN'))

```
# If your function works correctly, in logs you'll get:
```
==========
/THIS IS TIME/ [INFO] Info for logs #args from decorator
==========
==========
/THIS IS TIME/ [LOADED] print_lower successful execute. #func name.
==========
```
# In file you'll get:
```
i know you will say hi to me if we meet again
```
If you leave the decorator argument empty, the INFO field will not be added to the logs.

# If you function works not correctly, in logs you'll get:
```
==========
/THIS IS TIME/ [INFO] Info for logs #Args in decorator
==========
==========
/THIS IS TIME/ [ERROR] Function [print_lower] Loading error: division by zero in line 18 #Error, she give you a function, line, where have error
==========
```
If args for decorator is empty - It will not return [info]

# I have python 3.10, with convenient traceback support. So I'll move on to this.
[If you want to feel this code online]: https://replit.com/@DarkLorianPrime/Logger-1#main.py
[If you want to feel this code online]
