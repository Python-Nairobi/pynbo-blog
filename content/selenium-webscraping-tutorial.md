Title: Introduction to Web Scraping using Selenium
Date: 2017-09-05 09:00:00
Tags: python, webscraping, selenium, chromedriver
Category: Relevant_Category
Slug: selenium-webscraping-tutorial
Author: Roger Taracha
Summary: In this tutorial you’ll learn how to scrape websites with Selenium and ChromeDriver.
about_author: Taracha is a Software Developer & Mentor based in Nairobi. For more catch me on [Medium](https://medium.com/@NabweraTaracha) and on twitter @thedancercodes.  
email: rojtaracha@gmail.com


### Intoduction
Introduction to Web Scraping using Selenium

### What is Web Scraping?
As the name suggests, this is a data extraction technique used for extracting data from websites. It is an automated process where an application processes the HTML of a Web Page to extract data for manipulation such as converting the Web page to another format and copying into a local database or spreadsheet for later retrieval or analysis.

### What will we build?
In this tutorial we will build a web scraping program that will scrape a Github user profile and get the Repository names and the Languages for the pinned repositories.
If you would like to jump straight into the project, here is link to the repo on github.
https://github.com/TheDancerCodes/Selenium-Webscraping-Example

### What will we require?
We will also use the following packages and driver.
* [selenium package](https://pypi.python.org/pypi/selenium) — used to automate web browser interaction from Python
* [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) — provides a platform to open up and perform tasks in specified browser.
* [Virtualenv](https://virtualenv.pypa.io/en/stable/) — to create an isolated Python environment for our project.
* [Extras](http://selenium-python.readthedocs.io/) - Selenium-Python ReadTheDocs Resource.

### Steps
1. Setup project
2. Import Modules
3. Make The Request
4. Get the Response
5. Run the program


### Set up the project
Create a new project folder. Within that folder create an `setup.py` file.
In this file, type in our dependency `selenium`.

Open up your command line & create a virtual environment using the basic command:

`$ virtualenv webscraping_example`

Next, install the dependency into your virtualenv by running the following command in the terminal:

`$(webscraping_example) pip install -r setup.py`


### Import Required Modules
Specify the modules required for the project.


    :::python
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException


### Make The Request
When making the request we need to consider the following:
1. Pass in the desired website url.
2. Implement a Try and Except for handling a timeout situation should it occur.


    :::python
    # Specifying incognito mode as you launch your browser[OPTIONAL]
    option = webdriver.ChromeOptions()
    option.add_argument(“ — incognito”)

    # Create new Instance of Chrome in incognito mode
    browser = webdriver.Chrome(executable_path='/Library/Application Support/Google/chromedriver', chrome_options=option)

    # Go to desired website
    browser.get("https://github.com/TheDancerCodes")

    # Wait 20 seconds for page to load
    timeout = 20

    try:
        # Wait until the final element [Avatar link] is loaded.
        # Assumption: If Avatar link is loaded, the whole page would be relatively loaded because it is among
        # the last things to be loaded.
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='avatar width-full rounded-2']")))

    except TimeoutException:
        print("Timed out waiting for page to load")
        browser.quit()


### Get the Response
Once we make a request and it is successful, we need to get a response.
We will break the response into 2 and combine it at the end.
The response is the title and language of the pinned repositories of the Github profile.


    :::python
    # find_elements_by_xpath - Returns an array of selenium objects.
    titles_element = browser.find_elements_by_xpath("//a[@class='text-bold']")

    # List Comprehension to get the actual repo titles and not the selenium objects.
    titles = [x.text for x in titles_element]


    print('TITLES:')
    print(titles, '\n')


    # Get all of the pinned repo languages
    language_element = browser.find_elements_by_xpath("//p[@class='mb-0 f6 text-gray']")
    languages = [x.text for x in language_element] # same concept as for-loop/ list-comprehension above.

    print("LANGUAGES:")
    print(languages, '\n')

    # Pair each title with its corresponding language using zip function and print each pair
    for title, language in zip(titles, languages):
        print("RepoName : Language")
        print(title + ": " + language, '\n')


### Run the program
Finally run the program by using the following command or by running it directly in your IDE:


    :::python
    $ (webscraping_example) python webscraping_example.py


You can read more on Web Scraping here
[wikipedia page](https://en.wikipedia.org/wiki/Web_scraping).

[Here's](https://github.com/TheDancerCodes/Selenium-Webscraping-Example) the source code.

Also posted [here](https://medium.com/@NabweraTaracha/introduction-to-web-scraping-using-selenium-7ec377a8cf72)
