from twython import Twython
import csv

CONSUMER_KEY = 'TTouHDLZ8P2hq3xnUL2uSHKw8'
CONSUMER_SECRET = 'KSl3OHRZPsnvl33b0duYwgQx5ZfCHlKuB6snLN6cezUfwnJF2X'
ACCESS_TOKEN = '839154501324050434-X35lr0JMr0laIUkr1gRzJ9AkbauJrnE'
ACCESS_TOKEN_SECRET = 'mN64TvAdHrE1E4KK8XHXFM260KKzLae8FlLP9332cOypr'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

search = twitter.search(q='YOUR SEARCH TERM HERE', count="100")
tweets = search['statuses']

with open ('data.csv', 'w') as fp:
    a = csv.writer(fp)
    # add a header row
    a.writerow(('Search Term', 'Tweet Text', 'URL'))

    for result in tweets:
        try:
            url = result['entities']['urls'][0]['expanded_url']
        except:
            url = None
        text=[['propublica', result['text'].encode('utf-8'), url]]
        a.writerows((text))
from twython import Twython
import csv
CONSUMER_KEY = 'TTouHDLZ8P2hq3xnUL2uSHKw8'
CONSUMER_SECRET = 'KSl3OHRZPsnvl33b0duYwgQx5ZfCHlKuB6snLN6cezUfwnJF2X'
ACCESS_TOKEN = '839154501324050434-X35lr0JMr0laIUkr1gRzJ9AkbauJrnE'
ACCESS_TOKEN_SECRET = 'mN64TvAdHrE1E4KK8XHXFM260KKzLae8FlLP9332cOypr'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

search = twitter.search(q='GW Colonials', count="100")
tweets = search['statuses']


with open ('data.csv', 'w') as fp:
    a = csv.writer(fp)
    # add a header row
    a.writerow(('GW Colonials', 'Tweet Text', 'URL'))
    
       for result in tweets:
        try:
            url = result['entities']['urls'][0]['expanded_url']
        except:
            url = None
        text=[['propublica', result['text'].encode('utf-8'), url]]
        a.writerows((text))
        
        