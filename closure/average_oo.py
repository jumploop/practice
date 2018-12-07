class Averager():
    """计算移动平均值的类"""

    def __init__(self):
        self.series = []

    def __call__(self, new_value):
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)
avg=Averager()
ret=avg(10)
print(avg.series)

ret1=avg(11)
print(avg.series)

ret2=avg(12)
print(avg.series)
print(ret,ret2,ret1)
