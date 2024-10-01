# BeautifulSoup

import requests
from bs4 import BeautifulSoup  # allows us to grab the html/xml file
import pprint  # pretty print

res = requests.get('http://news.ycombinator.com/news')
res2 =requests.get('http://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')  # xml parsing also possible
soup2 = BeautifulSoup(res2.text, 'html.parser')
# soup is an object now , so we can extract items
# print(soup.body.contents) # all the list of items under body
# print(soup.find_all('div')) # all the div tags
# .find finds the first occurence unlike findall
links = soup.select('.titleline > a')  # css selectors
links2 = soup2.select('.titleline > a')
# for ids , #(id)
# for score or values/classes , .value
# for tags, string of that tag
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

mlinks = links+links2
msubtext = subtext + subtext2

def sort_stories_by_votes(hn):
    return sorted(hn, key = lambda k:k['score'],reverse = True) #key should be a function


def create_custom_hn(links, subtext):
    hn = []
    for i, item in enumerate(links):
        title = links[i].getText()
        href = links[i].get('href', None)
        votes = subtext[i].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points', ''))
            if points > 100:
                hn.append({'title': title, 'link': href, 'score': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(mlinks, msubtext))

# framework known as scrappy,
# much more powerful than beautifulsoup
