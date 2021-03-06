from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    # browser = init_browser()
    executable_path = {'executable_path' : 'chromedriver.exe'}
    browser = Browser('chrome',**executable_path,headless = False)

    listings = {}

    url = "https://redplanetscience.com/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    listings["title"] = soup.find("div", class_="content_title").get_text()
    listings["subtitle"] = soup.find("div", class_="article_teaser_body").get_text()

    # Quit the browser
    browser.quit()

    return listings