Title: Scraping The Python Nairobi Blog

Date: 2017-09-7 00:00

Tags: scrapy, web, spiders

Category: Web Scraping

Slug: scraping-the-python-nairobi-blog

Author: Gideon Kimutai (https://github.com/gr1d99)

Summary: This post will show you how to scrape the Python Nairobi blog using scrapy framework. 

about_author: A freelance Django web developer

email: [gravar](gideonkimutai9@gmail.com)

Scrapy is an application framework for crawling web sites and extracting structured data which can be used for a wide
range of useful applications, like data mining, information processing or historical archival.


so lets get started.

Requirements
------------
1. you need to have python installed on your computer. here is the link to the official site [python.org](https://www.python.org/downloads/)
2. create a virtual enviroment, steps can be found here [click me](https://virtualenv.pypa.io/en/stable/)
3. activate your created virtualenvironment and install scrapy framework by running the command
```pip install scrapy```.

**NB** if everything is installed correctly you are good to start scraping some data.

>**In this tutorial we will be scraping the Python Nairobi Blog, you may apply the concepts in this tutorial to scrape 
other websites too. You will also have to read further on your own since i will only cover the basics**


1. step one.

check again if `scrapy` is available in your current environment by typing `scrapy` in your terminal. If you see some 
bunch of help options then you are good to go.

> we are going to create our project. to do that type 
>```bash
>$ scrapy createproject naiblog
>```
>after creating the project minimize your terminal and you should see a directory named `naiblog`.
>
>the directory structure of naiblob should look like this.
>
>```
>naiblog/
>    scrapy.cfg
>    naiblog/
>        __init__.py # deploy configuration file project's Python module, you'll import your code from here
>        items.py # project items definition file
>        pipelines.py # project pipelines file
>        settings.py # project settings file
>        spiders/
>            __init__.py # a directory where you'll later put your spiders

create a file named `naiblog_spider.py` inside the folder `naiblog/spiders/naiblog_spider.py`

>now copy the contents below to the new file.
>
>```python
>import scrapy
> 
> 
>
>class NailblogSpider(scrapy.Spider):
>    name = 'naiblog'
>    
>    start_urls = [
>        'http://blog.pynbo.or.ke/'
>    ]
>    
>
>    def parse(self, response):
>        pass
>```

you need to note some few things here.

>* our spider subcalsses `scrapy.Spider`.
>* `name=naiblog` this is the name of our spider, it should be unique within this project.
>* `start_urls[]` is a class attribute and this where you write a list of urls that you will crawl. **this is just one of 
>the ways**.
>* `parse()` is a method that will be called to handle response download from each request.

now you atleast have the basics, so change the contents of the `parse()` method to be the same as the one below.

>```python
>class NaiblogSpider(spider.Spider):
>   ...
>   
>    def parse(self, response):
>        sub_header = response.xpath("//div//h1[@class='content-subhead']/text()").extract_first()
>        print sub_header
>```

on your terminal navigate to the root/base directory of the `naiblog` project and type
>```bash
>$ scrapy crawl naiblog --nolog
>````

output
>```bash
>$ Latest posts
>```

**yeey you just extracted the content subheading of the [http://blog.pynbo.or.ke/](http://blog.pynbo.or.ke/)**

just open the above url in your browser and right click on the heading `Latest Posts` then select the option inspect.
you will see that the `Post List` is wrapped inside 
>```html
><div class="posts"
>    <h1 class="content-subhead">
>        Latest posts
>    </h1>
>    ...
>```

**NB:** when extracting contents from a response we use `css` or `xpath` Selectors to select elements from the downloaded
response.

I find `xpath` more powerful rather than using `css`, you will also have to read more on yourself to understand `Xpath`
expressions.

now to the final part of our spider, comments on the code will help you get the idea of what is happening

>```python
>import scrapy
> 
> 
>class NaiblogSpider(scrapy.Spider):
>    name = 'naiblog'
> 
>    start_urls = [
>        'http://blog.pynbo.or.ke/'
>    ]
> 
>    def parse(self, response):
>        # lets start by extracting the root node /html
>        # from the response.
>        html = response.xpath("/html")
> 
>        # select the body element which is inside
>        # the root node html
>        body = html.xpath("//body")
> 
>        # lets now get the content element
>        content = body.xpath("//div[@class='content']")
> 
>        # extract the posts element
>        posts = content.xpath("//div[@class='posts']")
> 
>        # iterate over the posts element in order to get
>        # each individual post by extracting section node
> 
>        for post in posts.xpath("section[@class='post']"):
> 
>            # get the node header
>            header = post.xpath("header[@class='post-header']")
>            # finally get the title text
>            title = header.xpath("h3 /a/text()").extract_first()
>
>            # to get the description is the hardest part, if you inspect the element
>            # of the page you will notice that there are two <p class='post-meta'> and there
>            # is a <p> element without any attribute between them which holds a simple description
>            # of the post. Basically it makes it hard to extract the description of the post.
>            # I suggest the developers of the web app should look into it.
>            # with that issue in mind I did some tweak below in order to get the empty <p>
>            # tag.
>            description = header.xpath("p[@class='post-meta']|p/text()").extract()[1]
> 
>            # extract post category
>            category = header.xpath("p[@class='post-meta'] /a/text()").extract_first()
> 
>            # extract post date
>            date = header.xpath("p[@class='post-meta'] /text()")[-1].extract()
> 
>            # finally lets return some data
>            yield {
>                  'description': description, 'category': category, 'title': title, 'date': date
>            }
>```

lets execute our spider
>```bash
>$ scrapy crawl naiblog -o posts.json
>```

you will see lots of logs being displayed on your terminal, when there are no more logs displayed navigate to the root of 
`naiblog` project and you will see a file named `posts.json`, open it and you will see all the posts in `pynbo blog`.

Thats all!!

find the entire project on my git repo [naiblog](https://github.com/gr1d99/naiblog-spider.git).