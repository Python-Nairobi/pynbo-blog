Title: Faster python programs with pypy by Joannah Nanjekye
Date: 2017-03-06 18:11:00
Tags: pypy, python
Slug: pypy_by_joannah_nanjekye
Author: Joannah Nanjekye
Summary: A summary of the presentation on pypy Joannah Nanjekye gave.
email: nanjekyejoannah@gmail.com
about_author: <p> Software Engineer,  Aeronautical Engineer to be, Straight Outta 256 , I choose Results over Reasons, Passionate Aviator, Show me the code</p><p>I share my thoughts majorly here <a href="https://nanjekyejoannah.github.io/" target="_blank">https://nanjekyejoannah.github.io/</a></p>

pypy is an alternate implementation of the python programming language. Pypy started  out as a python interpreter written in python. It is aimed at being compatible with cpython and currently with experimental compatibility for CPython C API extensions.

Pypy originally refered to two things. one the python interpreter and Rpython Translation toolchain but currently pypy is always used torefer to the python interpreter. The translation framework is always refered to as the Rpython Translation Framework.

It is the distinct features embedded in pypy that give your python programs the magical performance. Lets have a look at some of them.

# Pypy Distinct Features

The pypy intepreter offers a couple of distinct features namely;

* Speed
* Compatibility
* Memory Usage
* Stackless python features

Speed 

Pypy is magically faster due to its high performance Just-in -time compiler and garbage collector.

It is therefore faster for programs that are JIT susceptible. This means that pypy may not always run faster , it may be for pure python code but actually run slower than Cpython where the JIT cant help. 

pypy may also not be as fast for small scripts that do not give the Just-in -time compiler enough warm up time.

I ran this [code]() on pypy and on normal python and the results show pypy is actually faster. I will go on share the outcomes below;

<img src="https://github.com/nanjekyejoannah/pynbo-blog/blob/jumbojet/content/img/pypy-vs_cpython.pypy1.PNG">

Alot of benchmarks have shown pypy performing better than Cpython and its not getting slower with time. Each new version of pypy is faster than its predecessor. The pypy team have shared good insight at their [speed center](http://speed.pypy.org/).


Compatibility 

Good news is pypy is compatible with most of the python Libraries. 

* Django
* Flask
* Bottle
* Pylons
* Pyramid
* Twisted
* lxml
* Beautiful Soup
* Sphinx
* IPyton
*  PIL/Pillow
* Psycopg2
* MySQL-Python
* pysqlite
* pymongo
* cx_Oracle
* SQLAlchemy
* Gunicorn
* Requests
* nose
* pytest
* celery
* Pip
* Numpy
*  Scipy
* Gevent

Pypy has Experimental support for Extension modules through cpyext. It can run most C extensions these days.

**Memory Usage**

Memory-intensive python programs take lesser space than when running on pypy . However this may not be the case always though due to some details.

**Stackless python Features**

Pypy exposes language features similar to the ones present in stackless python.

# Differences between Cpython and Python

Lets take a look at pypy and a reference python implementation called cpython.

<img src="https://github.com/nanjekyejoannah/pynbo-blog/blob/jumbojet/content/img/pypy-vs_cpython.png">


# Way Forward

“If you want your code to run faster, you should probably just use PyPy.” — Guido van Rossum (creator of Python)

# Installation

It is easy to install

<p>Linux</p>
	
	`sudo apt-get install pypy`

<p>Mac</p>
	
	`sudo brew install pypy`

<p> Windows </p>

There is rich [Documentation](http://pypy.org/download.html) on installation.


# Check these out for more pypy inspiration
* http://pypy.org/
* http://www.aosabook.org/en/pypy.html
* http://uk.dice.com/technews/a-look-at-pypy/
* http://slides.com/totalorder/what-is-pypy-and-why-should-i-use-it#/27