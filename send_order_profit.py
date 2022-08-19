import urllib.request
import urllib.error
import json
import pprint
import settings
import password
import variables


def sendorder_takeprofit(exit_side, qty, exit_price):
    # まずは利食い注文
    obj = {'Password': password.password,
           'Symbol': variables.symbol_trade,
           'Exchange': settings.exchange,
           'TradeType': 2,
           'TimeInForce': 1,
           'Side': exit_side,
           'Qty': qty,
           'ClosePositionOrder': 0,
           'FrontOrderType': 20,
           'Price': exit_price,
           'ExpireDay': 0}
    json_data = json.dumps(obj).encode('utf-8')

    url = 'http://localhost:' + settings.port + '/kabusapi/sendorder/future'
    req = urllib.request.Request(url, json_data, method='POST')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', variables.token)

    try:
        print('###sendorder_takeprofit')
        with urllib.request.urlopen(req) as res:
            print(res.status, res.reason)
            for header in res.getheaders():
                print(header)
            print()
            content = json.loads(res.read())
            pprint.pprint(content)

            # 利食い注文IDを保存
            exit_order_id = content['OrderId']
            pprint.pprint(exit_order_id)

            return exit_order_id

    except urllib.error.HTTPError as e:
        print('###kabusapi_sendorder2:HTTPError')
        print(e)
        content = json.loads(e.read())
        pprint.pprint(content)
    except Exception as e:
        print('###kabusapi_sendorder2:Exception')
        print(e)
