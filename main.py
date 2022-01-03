import subprocess
import tempfile
from PySide6.QtCore import Qt
from PySide6.QtWidgets import *
from ui import Ui_MainWindow
import db


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.curData = None

        try:
            self.db = db.DB()
            self.refreshList()
        except Exception as err:
            return self.errMsg(err)

    def refreshList(self):
        self.ui.listStrategy.clear()
        rows = self.db.list()
        for row in rows:
            item = QListWidgetItem(row["name"])
            item.setData(Qt.UserRole, row["id"])
            item.setData(Qt.UserRole+1, row["content"])
            self.ui.listStrategy.addItem(item)

    def quit(self):
        self.close()

    def listStrategyItemChange(self):
        cur = self.ui.listStrategy.currentItem()
        if not cur:
            return
        self.curData = {"id": cur.data(
            Qt.UserRole), "name": cur.text(), "content": cur.data(Qt.UserRole+1)}
        self.ui.textName.setText(self.curData["name"])
        self.ui.textContent.setText(self.curData["content"])

    def btnNewClicked(self):
        self.curData = {"id": None, "name": "new script",
                        "content": """
import os.path
import backtrader as bt
import pandas as pd
import akshare as ak


cacheFile = "/tmp/600000.csv"

class TestStrategy(bt.Strategy):
    def log(self, txt, dt=None):
        dt = dt or self.datas[0].datetime.date(0)
        print("%s, %s" % (dt.isoformat(), txt))

    def __init__(self):
        # 保存收盘价的引用
        self.dataclose = self.datas[0].close
        # 跟踪挂单
        self.order = None
        # 买入价格和手续费
        self.buyprice = None
        self.buycomm = None
        # 加入均线指标
        self.sma5 = bt.indicators.SimpleMovingAverage(self.datas[0], period=5)
        self.sma10 = bt.indicators.SimpleMovingAverage(self.datas[0], period=10)
        self.cs = bt.indicators.CrossOver(self.sma5, self.sma10)

    # 订单状态通知，买入卖出都是下单
    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # broker 提交/接受了，买/卖订单则什么都不做
            return

        # 检查一个订单是否完成
        # 注意: 当资金不足时，broker会拒绝订单
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log(
                    "已买入, 价格: %.2f, 费用: %.2f, 佣金 %.2f"
                    % (
                        order.executed.price,
                        order.executed.value,
                        order.executed.comm,
                    )
                )

                self.buyprice = order.executed.price
                self.buycomm = order.executed.comm
            elif order.issell():
                self.log(
                    "已卖出, 价格: %.2f, 费用: %.2f, 佣金 %.2f"
                    % (
                        order.executed.price,
                        order.executed.value,
                        order.executed.comm,
                    )
                )
            # 记录当前交易数量
            self.bar_executed = len(self)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log("订单取消/保证金不足/拒绝")

        # 其他状态记录为：无挂起订单
        self.order = None

    # 交易状态通知，一买一卖算交易
    def notify_trade(self, trade):
        if not trade.isclosed:
            return
        self.log("交易利润, 毛利润 %.2f, 净利润 %.2f" % (trade.pnl, trade.pnlcomm))

    def next(self):
        # 如果有订单正在挂起，不操作
        if self.order:
            return

        # 如果没有持仓则买入
        if not self.position:
            # 今天的收盘价在均线价格之上
            # if self.dataclose[-1] > self.sma[0]:
            if self.cs > 0:
                # 买入
                self.log("买入单, %.2f" % self.dataclose[0])
                # 跟踪订单避免重复
                self.order = self.buy()
        else:
            # 如果已经持仓，收盘价在均线价格之下
            # if self.dataclose[-1] < self.sma[0]:
            if self.cs < 0:
                # 全部卖出
                self.log("卖出单, %.2f" % self.dataclose[0])
                # 跟踪订单避免重复
                self.order = self.sell()


def getData(code, start, end):
    if os.path.exists(cacheFile):
        return pd.read_csv(cacheFile, parse_dates=True, index_col=0)
    df = ak.stock_zh_a_hist(
        symbol=code,
        period="daily",
        start_date=start,
        end_date=end,
        adjust="qfq",
    )

    ok = pd.DataFrame(
        df.drop(
            columns=[
                "振幅",
                "涨跌幅",
                "涨跌额",
                "换手率",
            ]
        )
    )
    ok.columns = [
        "datetime",
        "open",
        "close",
        "high",
        "low",
        "volume",
        "openinterest",
    ]
    ok.to_csv(cacheFile, index=False)
    return ok


if __name__ == "__main__":
    cerebro = bt.Cerebro()
    cerebro.addstrategy(TestStrategy)

    data = getData("601012", "20210730", "20211231")
    data = bt.feeds.PandasData(dataname=data)

    cerebro.adddata(data)
    cerebro.broker.setcash(1000)

    print("组合期初资金: %.2f" % cerebro.broker.getvalue())
    cerebro.run()
    print("组合期末资金: %.2f" % cerebro.broker.getvalue())
    # cerebro.plot(style="candle")

                        """}
        try:
            self.db.save(None, self.curData["name"], self.curData["content"])
        except Exception as err:
            return self.errMsg(err)

        self.refreshList()
        self.ui.listStrategy.setCurrentRow(self.ui.listStrategy.count()-1)
        self.listStrategyItemChange()

    def btnRemoveClicked(self):
        r = QMessageBox.warning(
            self, "提示", "确定要删除吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if r == QMessageBox.No:
            return

        try:
            self.db.remove(self.curData["id"])
        except Exception as err:
            return self.errMsg(err)

        self.refreshList()
        self.ui.textContent.clear()

    def btnRefreshClicked(self):
        self.refreshList()

    def errMsg(self, msg: Exception):
        QMessageBox.about(self, "错误", str(msg))

    def infoMsg(self, msg: str):
        QMessageBox.about(self, "提示", msg)

    def btnSaveClicked(self):
        r = QMessageBox.warning(
            self, "提示", "确定要保存吗？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if r == QMessageBox.No:
            return
        try:
            self.db.save(self.curData["id"], self.ui.textName.text(
            ), self.ui.textContent.toPlainText())
            self.infoMsg("保存成功")
        except Exception as err:
            return self.errMsg(err)

        i = self.ui.listStrategy.currentRow()
        self.refreshList()
        self.ui.listStrategy.setCurrentRow(i)

    def btnRunClicked(self):
        self.ui.textLog.setText("请稍后...")
        f = tempfile.NamedTemporaryFile()
        f.write(bytes(self.curData["content"], encoding="utf8"))
        f.flush()
        try:
            res = subprocess.Popen(
                ["python3", f.name], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            self.ui.textLog.setText(bytes.decode(
                res.stdout.read(), encoding="utf8"))
            # for line in res.stdout.readlines():
            #     print(line)
            # res.stdout.close()
        finally:
            f.close()


if __name__ == '__main__':
    app = QApplication([])
    # app.setWindowIcon(QIcon("logo.png"))    # 添加图标
    w = Window()
    w.show()
    app.exec()
