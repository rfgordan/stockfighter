import requests
import json
import time

#tracks a position in a specific stock
class position:
    def addOrder(res):
        r_json = res.json()
        if(res.status_code and r_json['ok']):
            pos += r_json['totalFilled']
            if r_json['type'] in ('limit','market') and r_json['open']:
                order = {'id':r_json['id'],'qty':r_json['qty'],'direction':r_json['direction'],'price':r_json['price']}
                orders[str(id)] = order

    def __init__(self,symbol,position = 0):
        self.sym = symbol
        self.pos = position
        self.orders = {}

#account information and utility methods
class account:
    key = '2e09d3ef27b6b8e06bc4ce2ca9628fb1acf41b65'
    headers = {'X-Starfighter-Authorization':key}

    #get quote price based on "bid", "ask", or "last", -1 if none exists
    def get_quote(basis):
        r = requests.get(base_url+'/quote',headers=headers)
        if r.status_code and r.json()['ok'] and basis in r.json():
            quote = r.json()[basis]
            return quote
        else:
            return -1

    #move block of stock given direction, order type, price and quantity
    def mov_block(q,p,dir,type,pos):
        params = {'account':acc,'venue':ven,'stock':pos.sym,'price':p,'qty':q,'direction':dir,'orderType':type}
        r = requests.post(base_url+'/orders',data=json.dumps(params),headers=headers)

        pos.addOrder(r)
        return r
    
    #takes position and updates orders therein
    def poll(self,pos):
        for (id,order) in pos.orders.iteritems():
            params = {'id':order['id'],'venue':self.ven,'stock':order.sym}
            r = requests.get(base_url+'/orders/'+str(order['id'],data=json.dumps(params),headers=headers)
            r_json = r.json()
            if r.status_code and r_json['ok']:
                                 if r_json['qty'] != order['qty']:
                                 

    def __init__(self,v,a):
        self.ven = v
        self.acc = a
        self.base_url = 'https://api.stockfighter.io/ob/api/venues/'+ven+'/stocks/'+sym
        self.positions = []
