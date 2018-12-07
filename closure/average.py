def make_averager():
    series=[]
    def averager(new_value):
        series.append(new_value)
        total=sum(series)
        return total/len(series)
    return averager

avg=make_averager()
ret=avg(10)

ret1=avg(11)

ret2=avg(12)

print(ret,ret2,ret1)