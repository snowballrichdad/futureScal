import time
from tkinter import messagebox

import send_order_entry
import order_info
import send_order_profit
import variables


def entry(side, qty, take_profit_margin):
    # 初期化
    variables.take_profit_order_id = ''
    variables.exit_side = ''

    # noinspection PyUnusedLocal
    exit_price = 0
    if side == "2":
        # 買いエントリ
        variables.exit_side = "1"

    else:
        # 売りエントリ
        variables.exit_side = "2"

    # エントリ
    entry_order_id = send_order_entry.send_order_entry(side, qty)

    # noinspection PyUnusedLocal
    order_price = 0
    while True:
        # 全約定するまで待つ
        order_price = order_info.orders_info(entry_order_id)
        if order_price > 0:
            break
        if order_price is None:
            # Noneの場合は発注失敗
            messagebox.showinfo('エラー', 'エントリ失敗')
            return
        time.sleep(0.2)

    if side == "2":
        # 買いエントリ
        exit_price = order_price + take_profit_margin

    else:
        # 売りエントリ
        exit_price = order_price - take_profit_margin

    # 利食い注文
    variables.take_profit_order_id = \
        send_order_profit.sendorder_takeprofit(variables.exit_side, qty, exit_price)
