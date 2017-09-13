---
Title: Implementing Lisp pairs in Python 3.6.1
Date: 2017-09-07 09:00
Categories: misc
Slug: lisp_pairs_in_python
Author: Bonface K. Munyoki
Summary: I discuss how to implement Scheme's basic pair data structure in Python for fun using Message Passing [Scheme is a Lisp dialect]
about_author: Linux enthusiast. Audiophile. Huge anime fan. "Retired" amateur competitive swimmer. Tinkeror. Former typography nerd.
email: bonfacemunyoki@gmail.com

---

*I wrote this article earlier on my blog <a href="https://bonfacemunyoki.com/post/2017-08-28-implementing-scheme-pairs-in-python/" target="_blank"> here</a>.*

I've come to like Python. It makes rapid prototyping things way easier. I also appreciate that it treats functions as first class citizens, something that (maybe) many Python hackers do not know. I thought it'd be cool to implement one of Scheme's(Scheme is a Lisp variant) basic structures, the ***pair***, in Python. I'll use a form of Message Passing to do this(more on this later).

First, here's what a pair looks like in Scheme:

``` lisp
;; We define a as a pair comprising 1 and 3
(def a (cons 1 3))

;; We access the first element of a pair by
;; running (car <element>). In our case, this
;; would give: 1
(car a)

;; We access the second element of a pair by
;; running (cdr <element>). This will give: 3
(cdr a)
```

Here's how our implementation of `cons`, `car`, `cdr` looks like:

```
def cons(x, y):
    def dispatch(m):
        if m == "car":
            return x
        elif m == "cdr":
            return y
        else:
            print("error dude")
    return dispatch
```

Here, we define an internal procedure `dispatch` that receives some "message" and acts on it. If the "message" is a `car` it will return the first element of cons' arguments. If it's a `cdr`, it'll return the second element; otherwise, a simple error message is printed. Our `cons` function returns a procedure as its return value. As we shall see later, our "message" will be passed to this return value. Now let's create our `car` and `cdr` functions.

```
def car(z):
    return z("car")

def cdr(z):
    return z("cdr")
```

Both `car` and `cdr` take a pair(a cons object) as it's arguments. The right value is returned depending on the "message passed". The name "message passing" comes from the image that a data object(in our case the pairs) is an entity that receives the requested operation name as a "message". Let's create some fancy pairs :)
```
x = cons(2, 3)

# Let's print the first element of x:
print(car(x))

# Let's print the second element of x:
print(cdr(x))
```
