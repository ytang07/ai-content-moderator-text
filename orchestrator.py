# imports
from webscraper import scrape_page_text
from content_moderator import moderate
# function
def orchestrate():
    # ask user for website URL
    url = input("What URL would you like to moderate? ")
    # call webscraper on the URL
    print("Scraping Page Text ...")
    text = scrape_page_text(url)
    # call content moderator on the scraped data
    print("Moderating Page Text ...")
    rating, trigger = moderate(text)
    # return verdict
    return rating, trigger

print(orchestrate())