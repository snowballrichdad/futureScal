import symbolname

take_profit_order_id = ''
margin_trade_type = 0
exit_side = ''
symbol_trade = ''

# token読み込み
f = open(r'token.txt', 'r')
token = f.read()
f.close()

# symbolname読み込み
symbolname.symbolname_trade()
