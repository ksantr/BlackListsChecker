# BlackListsChecker

Check if domain or ip addess is presented in spam black lists.
Requires Python 2.x.

Installation
    python setup.py install

Usage
* Use it from the commad line:
```    
    blcheck 10lbs2days.com
```
* As python's module:
```    
    >>> from blcheck import blcheck
    >>> ch = blcheck.BlackListsChecker(threads=20)
    >>> ch.is_spam('10lbs2days.com')
```
License
MIT
