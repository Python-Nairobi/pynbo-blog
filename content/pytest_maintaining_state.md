---
Title: Maintaining states while using Pytest
Date: 2018-09-10 9:30
Tags: python, pytest
Category: unit testing
Slug: test_states
Author: Michael Bukachi
Summary: Maintaining states while using pytest
about_author: Michael is a Software Engineer at Mobidev Kenya Limited
email: michaelbukachi@gmail.com
---

## Pre-requisites
 > - Beginner level Python
 > - Python2* or Python3* installed
 > - Basic knowledge on TDD and python UnitTesting
 > - Pytest installed
 
 
 #Intro
 
 ![alt text](https://cdn-images-1.medium.com/max/1600/1*7dFF3N2BwzlPz5MHA3_eyA.gif "When things go wrong")
 
 Ah, testing, a topic many devs don't like hearing. I really don't blame them. Testing is _tricky_.
 It's difficult to get it right and it's always evolving. I personally struggled with it for quite
 some time before I got the hang of it. But it is **necessary**. These days I can't start a project  before making sure 
 that there are testing frameworks available for the specific language I am using.
 
 **Disclaimer:** This guide is not an introduction to testing using pytest. For that, just open 
 [our friendly search engine](https://www.google.com) and search "getting started with pytest". Trust me, you won't 
 regret it.
 
 ![](https://data.whicdn.com/images/86201703/original.gif "You're welcome")
 
 #Getting started
 For this guide, I'll be using flask for demonstration. The demo project is available 
 [here](https://github.com/michaelbukachi/flask_pystest_state.git). The basic structure of the project as follows:
 ```
 ├── app
│   ├── __init__.py
│   └── views.py
├── requirements.txt
└── test
    ├── conftest.py
    ├── __init__.py
    └── test_token.py

 ```
 
**app/__init__.py**
```
from flask import Flask


def create_app():
    app = Flask(__name__)
    from .views import auth
    app.register_blueprint(auth)
    return app

```
Notice that I've used the lazy pattern so that it is easy to test.

**app/views.py**
```
from uuid import uuid4

from flask import Blueprint, jsonify, request

auth = Blueprint('auth', __name__)

TOKEN = str(uuid4())


@auth.route('/token')
def get_token():
    return jsonify(TOKEN)


@auth.route('/secure', methods=['POST'])
def secure_page():
    args = request.get_json(force=True)
    if 'token' in args:
        if args['token'] == TOKEN:
            return jsonify('This is a secure page')

    res = jsonify('Unauthorized')
    res.status_code = 401
    return res

```

**test/conftest.py**
```
import json

import pytest
from flask import Response
from flask.testing import FlaskClient
from werkzeug.utils import cached_property

from app import create_app


class JSONResponse(Response):

    @cached_property
    def json(self):
        return json.loads(self.get_data(as_text=True))


@pytest.fixture('session')
def flask_app():
    app = create_app()
    yield app


@pytest.fixture('session')
def client(flask_app):
    app = flask_app
    ctx = flask_app.test_request_context()
    ctx.push()
    app.test_client_class = FlaskClient
    app.response_class = JSONResponse
    return app.test_client()

```

**test/test_token.py**
```
import pytest
from flask.testing import FlaskClient


@pytest.fixture('module')
def token():
    return __name__ + ':token'


def test_get_token(client: FlaskClient, token, request):
    res = client.get('/token')
    assert res.status_code == 200
    token_ = res.json
    request.config.cache.set(token, token_)


def test_secure_page(client: FlaskClient, token, request):
    token_ = request.config.cache.get(token, None)
    res = client.post('/secure', json={})
    assert res.status_code == 401
    res = client.post('/secure', json={'token': token_})
    assert res.status_code == 200

```

For those who have not used pytest before, pytest basically uses dependency injection to 
provide dependencies to tests. This has numerous applications, from providing dummy data to providing
configurations and constants. If you take a look at `test/conftest.py` you'll notice that the dependencies to be injected
have been defined.

All the magic happens in `test/test_token.py` in the following lines of code:
```
@pytest.fixture('module')
def token():
    return __name__ + ':token'
```

The name of the function can be anything. What's important to note is the use of `__name__ + ':token:`. Since state changes
are persisted into a file, using `__name__` enables creation of unique files in case multiple test are being run in parallel.

The `request` dependency is provided by pytest and is used to store and retrieve persisted data

I find state persistence very useful in situations why I need to share data between tests. Yes, yes. I know. Test are supposed
to be unique and independent. But sometimes it's necessary. For instance, when a token is required to access an api, like in 
the example above or, if you want to maintain data from a response for use in future requests.


![alt text](https://orig00.deviantart.net/6ef3/f/2015/092/e/7/that_s_all_folks_by_shootersp-d8o2m64.gif "That's all folks!")