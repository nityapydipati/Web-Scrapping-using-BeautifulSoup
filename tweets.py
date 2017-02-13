from bs4 import BeautifulSoup
import urllib2

print "enter username:"
user=raw_input()
tweet_feed = "https://twitter.com/%s"
page=urllib2.urlopen(tweet_feed%user)

soup=BeautifulSoup(page, 'html.parser')
#used to understand the html structure that is obtained
#print(soup.prettify())
print("\n")
all_divs=soup.find_all("div", class_="js-tweet-text-container")
for div in all_divs:
    all_tweet=div.find_all("p", class_= "tweet-text")
    for tweet in all_tweet:
        print tweet.text
        