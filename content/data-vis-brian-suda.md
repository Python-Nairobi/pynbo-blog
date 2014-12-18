Title: Data Vizualizations by Brian Suda
Date: 2014-12-16 18:11:00
Tags: data viz, python, deterministic design, iceland, brian suda
Slug: data_viz_by_brian_suda
Author: Brian Suda
Summary: A round up and links from the presentation Brian Suda gave about data vizualizations
email: brian@suda.co.uk
about_author: <p>Brian Suda is an informatician currently residing in Reykjavík, Iceland. He has spent a good portion of each day connected to Internet after discovering it back in the mid-1990s.</p><p>Most recently, he has been focusing more on the mobile space and future predictions, how smaller devices will augment our every day life and what that means to the way we live, work and are entertained.</p><p>His own little patch of Internet can be found at <a href="http://suda.co.uk" target="_blank">http://suda.co.uk</a> where many of his past projects and crazy ideas can be found.</p>

Thanks to everyone who came on their Saturday to listen to me talk about data visualisations through a computer screen several timezones and many kilometres away. I know sitting through online presentations can be boring, so I hope mine was interesting enough that not many people fell asleep or left. It doesn’t matter, I could only see my slides and hear the shuffling of chairs every once and awhile, so I knew people were still there.

On Saturday, December 13th, I ran through my presentation about the basics of charts & graphs and how build-up to more complex data visualizations. It was a great group to chat with because it was the a Python meet-up. Most of the event I attend it is a mix of disciplines, so you can never get too technical, or even worse, it is a group of designers who you at you with a blank expression when you start to talk about code and scripts.

Getting to share some ideas with the folks in Nairobi was an exciting experience, and I know you are the types of people who get it. You’ll take apart the code and understand what’s happening.

# Deterministic Design

One of the topics I’m really interested in is this idea of Deterministic Design.

This is the sort of design that you do once, up front, then feed in the data and see how it looks. Then if you need to update the design, you don’t do it for that particular instance, but back upstream at the source where the code is written. That way, next time the run the code, all future designs will benefit.

At the moment, I’m calling this Deterministic Design, because if you feed in the same data, you’ll get the same results every time. Much like the color picking example I showed in the presentation. Using the MD5 function, we can get a hex string, which we take the first 6 characters and use that to generate a unique color that is fully reproducible on any system or language.

    import hashlib
    hh = hashlib.md5()
    hh.update(“Hello World”)
    hh.hexdigest()[:6]

I use this equation everywhere. It saves time and thought, but the downside is that you are bound by the color that it returns, even if it isn’t pretty! This little snippet of code needs a friend to help make sure you have the highest color contrast possible. I wrote about this on [24ways Calculating Color Contrast](http://24ways.org/2010/calculating-color-contrast/). You’ll have to port the code to Python yourself.

I love a lot of these little projects, to convert small ideas into some code that is repeatable over and over again. I also like the UNIX philosophy of small, reusable pieces. This means I tend to write small programs which take a CSV as data and create small SVG files as output. Then I can bring those into more complex programs to edit, annotate and layout the data. If the CSV changes, it is easy for me to reproduce the charts & graphs, because it is all done in code.

Most of the simple tools that I have written are available on [GitHub](https://github.com/briansuda/Deterministic-Design). There is a lot to wade through and you’ll have to port it to Python, but they are simple, useful utilities.

# Starting Small and Growing Bigger
When starting off, it is important to just start small. Rather than trying to dig into a massive amount of social media data, why not track your hours each week. How much is spent at work, at home, a sleep. Then try to visualize that in an interesting way. With some practice you’ll figure out what works, what doesn’t and what tools you like to use in your workflow.

After that you can begin to progress to more complex data sets. Start off with some you like and understand, build-up a small portfolio of interesting examples and then take on bigger and bigger projects. You’ll quickly see that even the biggest project is just a series of smaller ones that you probably have some experience or tools to deal with.

# Inspiration
To stay fresh, you need to keep an eye on interesting people in the field. There are a lot of resources out there and these are a few to get you started.

* [http://datastori.es](http://datastori.es)
* [https://eagereyes.org](https://eagereyes.org)
* [http://www.informationisbeautiful.net](http://www.informationisbeautiful.net)
* [http://dataviz.tumblr.com](http://dataviz.tumblr.com)

If anyone has any questions, they can always contact me on twitter [@briansuda](https://twitter.com/briansuda) or follow along with what I write on [(optional.is)](http://optional.is/required) and [join the mailing list](http://optional.is/newsletter). I can’t guarantee that everything will be Data viz related, but it will be interesting!
