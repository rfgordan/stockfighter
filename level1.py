import requests
import json
import time
import random
import math

acc = 'HEJ57026523'
sym = 'AUEH'
ven = 'HFHEX'

base_url = 'https://api.stockfighter.io/ob/api/venues/'+ven+'/stocks/'+sym 
headers = {"X-Starfighter-Authorization":"2e09d3ef27b6b8e06bc4ce2ca9628fb1acf41b65"}

def get_quote():
    r = requests.get(base_url+'/quote',headers=headers)
    print '\n' + r.text + '\n'
    if(r.status_code and r.json()['ok'] and 'ask' in r.json()):

        quote = r.json()['ask']
        return quote
    else:
        return -1

def mov_block(q,p,dir):
    params = {'account':acc,'venue':ven,'stock':sym,'price':p,'qty':q,'direction':dir,'orderType':'limit'}
    r = requests.post(base_url+'/orders',data=json.dumps(params),headers=headers)
    print '\n' + r.text + '\n'
    return r


#get quote, only accept stock prices w/in certain range of quote

target = 3616
# while 1:
#     init_quote = get_quote()
#     if init_quote != -1:
#         break

# print '\n %d \n' % init_quote  

total = 0

# r = buy_block(100,init_quote)
# print r.text
# print r.headers

#buy in blocks of 100
# while total < 100:
#     x = get_quote()
#     while x > init_quote*1.1 or x == -1:
#         if(x!=0):time.sleep(random.random())
#         x = get_quote()
#     r = mov_block(100,x,'buy')
#     r_json = r.json()
#     if(r.status_code and r_json['ok'] and r_json['totalFilled']):
#         filled = r_json['totalFilled']
#         print '\n Qty filled: %d \n' % filled 
#         total+=filled
#     time.sleep(random.random())

while total < 100000:
    time.sleep(random.random()*0.5)
    x = get_quote()
    print '%d' % x
    r = 0
    if x >= target * 1.05:
        r = mov_block(100,int(0.95*x),'sell')
    elif x <= target and x > 0:
        r = mov_block(1000,x,'buy')
    else:
        continue
    total+=r.json()['totalFilled']
