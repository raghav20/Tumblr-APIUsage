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
ind = 0
f = open('out.txt','w')
while off <40:
   my_dict = client.following(offset =off)
   res = my_dict['blogs']
   
   for rs in res:
       rest = []
       data =  rs['title']
       #r = duckduckgo.query(data)
       w = data.split(' ')
       for wq in w:
           check_word(wq)
       
       noun = ' '.join(rest)
       
       
       #print r.related[0].text
       f.write(rs['title'] + "            " +noun +"\n")
       #print(rs['name'] + "...."+ rs['title'] +"\n")
       #print "hi"
 
   off+=20