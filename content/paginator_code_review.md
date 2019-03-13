---
Title: Pagination Review of Django's and Pelican's Implementation
Date: 2019-03-12 17:30
Categories: misc
Slug: pagination-review-of-django-pelican-implementation
Author: John Nduli
Summary: I discuss how pagination is implemented in both pelican and django, and how this implementation can generally be used
about_author: Linux enthusiast, Anime + Manga Fan, Audiophile, Tinkerer
email: yohanaizraeli@gmail.com
---

*I wrote this article earlier on my blog <a href="https://jnduli.co.ke/pagination-review-of-django-pelican-implementation.html" target="_blank">here</a>.*


Pagination is the process of dividing up a document into discrete pages
([wikipedia](https://en.wikipedia.org/wiki/Pagination)). Django and
Pelican have similar pagination implementations. This boils down to
having a class that has accepts a sliceable object as one of its params,
and returns a page containing list of items depending on number of items
per page. The django [paginator
docs](https://docs.djangoproject.com/en/2.1/topics/pagination/#required-arguments)
describe the object list as a list, tuple, QuerySet, or other sliceable
object with a count() or __len__() method.

```python
paginator = Paginator(object_list=list, per_page=10)
```


To get the contents of a particular page one calls the get_page method:

```python
paginator.get_page(2)
```

What this does is to first check if the number provided is valid using
the validate_number method. A number is valid if its an integer, it's
greater than 0 and is less that the total number of pages in the
paginator (if the alloy_empty_first_page parameter was set to True, 1
will be valid even if the total number of pages is 0).

If the number was valid the page method is called. This creates the
required start and end slices i.e.`start:end` on the object list, and
returns a Page object that only contains these elements.

The code below shows some boiler plate that can achieve this:

```python
class Paginator:

   def __init__(self, object_list, per_page,
                allow_empty_first_page=True):
       self.object_list = object_list
       self.per_page = int(per_page)
       self.orphans = int(orphans)
       self.allow_empty_first_page = allow_empty_first_page

   def validate_number(self, number):
       # Make sure number is integer, greater than 1 and less than
       # the total number of pages

  def get_page(self, number):
       # if number is valid, returns a page object.
       # This is done by getting range of items required
       # e.g. 11:20, and returning an object that one can iterate
       # through (called a Page object)

  def num_pages(self):
     # Returns the total number of pages

  def count(self):
     # Returns total number of objects
```

To loop over the page object with a for, the Page class implements the
__getitem__ for this. Pelican's implementation does not have this method
though. It also has some useful methods like:

+ `has_next`
+ `has_previous`
+ `has_other_pages`
+ `next_page_number`
+ `previous_page_number`

With these one can effectively get the contents of a page by looping
through the paginator (in django only) and have various logic on which
page numbers to display.

The example provided in the [django docs
here](https://docs.djangoproject.com/en/2.1/topics/pagination/#using-paginator-in-a-view)
shows a really good usage of the various methods.
