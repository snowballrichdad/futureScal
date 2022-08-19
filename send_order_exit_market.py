import urllib.request
import urllib.error
import pprint
import json
import sys

import password
import settings
import variables


def send_order_exit_market(side, qty):
    # 成行返済注文
    obj = {'Password': password.password,
           'Symbol': variables.symbol_trade,
           'Exchange': settings.exchange,
           'TradeType': 2,
           'TimeInForce': 2,
           'Side': side,
           'Qty': qty,
           'ClosePositionOrder': 0,
           'FrontOrderType': 120,
           'Price': 0,
           'ExpireDay': 0}
    json_data = json.dumps(obj).encode('utf-8')

    url = 'http://localhost:' + settings.port + '/kabusapi/sendorder/future'
    req = urllib.request.Request(url, json_data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', variables.token)

    try:
        print('###sendorder_exit_market')
        with urllib.request.urlopen(req) as res:
            print(res.status, res.reason)
            for header in res.getheaders():
                print(header)
            print()
            content = json.loads(res.read())
            pprint.pprint(content)
            # 注文ID
            order_id = content['OrderId']

            return order_id

    except urllib.error.HTTPError as e:
        print(e)
        content = json.loads(e.read())
        pprint.pprint(content)
    except Exception as e:
        print(e)

    sys.exit()
