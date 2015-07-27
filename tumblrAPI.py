import oauth2
import pytumblr
import json

REQUEST_TOKEN_URL = 'http://www.tumblr.com/oauth/request_token'
AUTHORIZATION_URL = 'http://www.tumblr.com/oauth/authorize'
ACCESS_TOKEN_URL = 'http://www.tumblr.com/oauth/access_token'
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
AUTH_KEY=''
AUTH_SECRET=''
client = pytumblr.TumblrRestClient(
  CONSUMER_KEY,
  CONSUMER_SECRET,
  AUTH_KEY,
  AUTH_SECRET
)

off =0
while True:
   my_dict = client.following(offset =off)
   print my_dict
   res = my_dict['blogs']
   for rs in res:
       print(rs['name'] + "...."+ rs['title'])
       #print "hi"
 
   off+=20
#pprint(data)    
