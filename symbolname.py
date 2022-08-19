import urllib.request
import urllib.parse
import urllib.error
import json
import pprint
import settings
import variables


def symbolname_trade():
    url = 'http://localhost:' + settings.port + '/kabusapi/symbolname/future'
    params = {'FutureCode': settings.future_code_trade,
              'DerivMonth': settings.drive_month}
    req = urllib.request.Request('{}?{}'.format(url, urllib.parse.urlencode(params)), method='GET')
    req.add_header('Content-Type', 'application/json')
    req.add_header('X-API-KEY', variables.token)

    try:
        print('###symbolname')
        with urllib.request.urlopen(req) as res:
            print(res.status, res.reason)
            for header in res.getheaders():
                print(header)
            print()
            content = json.loads(res.read())
            pprint.pprint(content)

            # 取引銘柄コードを保存
            variables.symbol_trade = content['Symbol']
            pprint.pprint(variables.symbol_trade)

    except urllib.error.HTTPError as e:
        print(e)
        content = json.loads(e.read())
        pprint.pprint(content)
    except Exception as e:
        print(e)


if __name__ == "__main__":

    symbolname_trade()
