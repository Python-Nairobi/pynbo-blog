---
Title: Lessons in DRYness - Decorators in Python
Date: 2017-08-30 09:00
Tags: decorators, dry code, python
Category: misc
Slug: decorators_in_python
Author: Mbithe Nzomo
Summary: What decorators are and how to use them for DRYer code
about_author: Mbithe is a software developer at Andela, and a co-organiser and coach at Django Girls Nairobi. She blogs at deCODEgirl.com and tweets at @mbithenzomo.
email: mbithe.nzomo@gmail.com
---
*This article first appeared <a href="http://www.decodegirl.com/lessons-in-dryness-decorators/" target="_blank">
on deCODEgirl.com</a>.*

<img src="/img/lessons-in-dryness.jpg" width="100%" alt="Troll Face" />

What do clothes and code (and my jokes) have in common? Answer: They're so
much better when they're dry. <img src="/img/troll-face.jpg" width="5%" style="vertical-align: middle;" alt="Troll Face" />

What does it mean for code to be **DRY**? Simple: **Don't Repeat Yourself**.
The DRY Principle is key when writing efficient code. It helps keep your
codebase smaller and less complex, saves you time, reduces redundancy... it's
basically sugar, spice, and everything nice. :) In this post, I'm going to demonstrate how decorators in Python can help keep
your code DRY.

Once upon a time, I was building a RESTful API with <a
href="http://flask.pocoo.org/" target="_blank">Flask</a> (which
you can check it out on GitHub <a
href="https://github.com/mbithenzomo/flask-bucketlist-api" target="_blank">
here</a>) for an online bucket list service. Users could:

1. Sign up and login
2. Create, edit, view, and delete bucket lists
3. Create, edit, view, and delete bucket list items

Some endpoints were protected and could only be accessed by authorized users.
For instance, only the user who created a bucket list or bucket list item could
edit, view, or delete it.

Here's how I initially tackled it. First, I created a method to display an
error message, with the default being "Error: You are not authorized to access
this resource."

``` python
def unauthorized(message=None):
    """
    Returns an error message.
    """
    if not message:
        message = "Error: You are not authorized to access this resource."
    return jsonify({
        "message": message
    }), 403
```

Then, I went ahead and wrote the methods for the endpoints:

``` python
class BucketListAPI(Resource):
      """
      URL: /api/v1/bucketlists/<id>
      Request methods: GET, PUT, DELETE
      """

      def get(self, id):
          """ Get a bucket list """
          bucketlist = Bucketlist.query.filter_by(id=id).first()
          if bucketlist:
              if bucketlist.created_by == g.user.id:
                  return marshal(bucketlist, bucketlist_serializer)
              else:
                  return unauthorized()
          else:
              return unauthorized("Error: The bucket list specified doesn't "
                                  "exist. Please try again!")

      def put(self, id):
          """ Edit a bucket list """
          bucketlist = Bucketlist.query.filter_by(id=id).first()
          if bucketlist:
              if bucketlist.created_by == g.user.id:
                  parser = reqparse.RequestParser()
                  parser.add_argument("title",
                                      required=True,
                                      help="No title provided.")
                  parser.add_argument("description", type=str, default="")
                  args = parser.parse_args()
                  title, description = args["title"], args["description"]
                  bucketlist.title = title
                  bucketlist.description = description
                  return edit_item(name="title",
                                   item=bucketlist,
                                   serializer=bucketlist_serializer,
                                   is_user=False,
                                   is_bucketlist=True,
                                   is_item=False)
              else:
                  return unauthorized()
          else:
              return unauthorized("Error: The bucket list you are trying to "
                                  "edit doesn't exist. Please try again!")

      def delete(self, id):
          """ Delete a bucket list """
          bucketlist = Bucketlist.query.filter_by(id=id).first()
          if bucketlist:
              if bucketlist.created_by == g.user.id:
                  return delete_item(bucketlist,
                                     bucketlist.title,
                                     is_user=False,
                                     is_bucketlist=True,
                                     is_item=False)
              else:
                  return unauthorized()
          else:
              return unauthorized("Error: The bucket list you are trying to "
                                  "delete doesn't exist. Please try again!")
```

You can see the problem already: in each of these methods, I basically repeated
the same chunk of code to ensure that:

1. The bucket list existed
2. The current user was authorized to access the endpoint
3. Appropriate error messages were displayed if the above conditions were false

``` python
# Check whether bucket list exists
if bucketlist:
    # Check whether bucket list was created by the current user
    if bucketlist.created_by == g.user.id:
        # Do something here
    else:
        # Return unauthorized error message
        return unauthorized()
else:
    # Return non-existent bucket list error message
    return unauthorized("Error: The bucket list you are trying to "
                        "delete doesn't exist. Please try again!")
```

Not DRY at all. Fret not, though: decorators to the rescue!

A decorator is basically a function that takes a callable (a function or a
class) as a parameter, modifies it, and returns it. You could also say that decorators wrap a callable, modifying its behavior.

Here's how I used a decorator to eliminate my duplicate code. First, I wrote
the decorator function:

``` python
def authorized_user_bucketlist(function):
    def auth_wrapper(*args, **kwargs):
        g.bucketlist = Bucketlist.query.filter_by(id=kwargs["id"]).first()
        try:
            if g.bucketlist.created_by == g.user.id:
                return function(*args, **kwargs)
            return unauthorized()
        except:
            return unauthorized("Error: The bucket list specified doesn't "
                                "exist. Please try again!")
    return auth_wrapper
```

So here's what's going on in there: The decorator is
`authorized_user_bucketlist`, and it takes some function as a parameter. It has
another function, `auth_wrapper`, where a variable `g.bucketlist` is defined as
the bucket list whose ID is passed to the function as a key word argument. It
then checks if the bucket list was created by the current user. If so, it
invokes the function and returns the result. If not, it returns an unauthorized error message. If the bucket list doesn't exist, it returns a non-existent
bucket list error message. Basically, it does the same thing my duplicated
chunk of code was doing, but with a little more finesse (like, using a
try-except block as opposed to an if-else block, because it's better to ask for forgiveness than to ask for permission).

The refactored code:

``` python
from base import authorized_user_bucketlist

class BucketListAPI(Resource):
    """
    URL: /api/v1/bucketlists/<id>
    Request methods: GET, PUT, DELETE
    """
    @authorized_user_bucketlist
    def get(self, id):
        """ Get a bucket list """
        return marshal(g.bucketlist, bucketlist_serializer)

    @authorized_user_bucketlist
    def put(self, id):
        """ Edit a bucket list """
        parser = reqparse.RequestParser()
        parser.add_argument("title",
                            required=True,
                            help="No title provided.")
        parser.add_argument("description", type=str, default="")
        args = parser.parse_args()
        title, description = args["title"], args["description"]
        g.bucketlist.title = title
        g.bucketlist.description = description
        return edit_item(name="title",
                         item=g.bucketlist,
                         serializer=bucketlist_serializer,
                         is_user=False,
                         is_bucketlist=True,
                         is_item=False)

    @authorized_user_bucketlist
    def delete(self, id):
        """ Delete a bucket list """
        return delete_item(g.bucketlist,
                           g.bucketlist.title,
                           is_user=False,
                           is_bucketlist=True,
                           is_item=False)
```

I imported the decorator function, and then called the decorator using the `@`
symbol before each method. This is some <a
href="https://en.wikipedia.org/wiki/Syntactic_sugar" target="_blank">
syntactic sugar</a> that Python provides,
making the calling of decorators much simpler than it otherwise would be.

The code is much DRYer now! Mission accomplished! It's not perfect, but it's
way better than it was. :) This project is several months old now, and no longer
being maintained, but feel free to <a
href="https://github.com/mbithenzomo/flask-bucketlist-api"
target="_blank">clone the repo</a> and test my API!

Also, you can learn more about decorators in Python <a href="https://realpython.com/blog/python/primer-on-python-decorators/"
target="_blank">here</a> and <a
href="http://thecodeship.com/patterns/guide-to-python-function-decorators/"
target="_blank">here</a>.
