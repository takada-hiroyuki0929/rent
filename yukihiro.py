import math
start = 9000000 + 404256 # マンションの値段 + 火災保険料、手数料
remaining = start
payment = 0

# 一ヶ月の利子 + 元本 (年利3.9%)
#month_rate = 1.0031933138078821
month_rate = 1 + 0.039/12
#開始日 2019/8
print("開始金額 : 建物代 + 手数料、火災保険料")
print("開始金額 : " + "{:,}".format(remaining))
#最初に120万支払い済み
# 2019/8
remaining = remaining - 1200000
payment += 1200000
print("開始時に120万円受け取る")
print("2019/8 : " + "{:,}".format(remaining))
# 2019/9
remaining = math.ceil(remaining * month_rate)
print("2019/9 : " + "{:,}".format(remaining))
# 2019/10
remaining = math.ceil(remaining * month_rate)
print("2019/10 : " + "{:,}".format(remaining))
# 2019/11
remaining = math.ceil(remaining * month_rate)
print("2019/11 : " + "{:,}".format(remaining))
# 2019/12
remaining = math.ceil(remaining * month_rate)
print("2019/12 : " + "{:,}".format(remaining))
# 2020/01
remaining = math.ceil(remaining * month_rate)
print("2020/01 : " + "{:,}".format(remaining))
# 2020/02
remaining = math.ceil(remaining * month_rate)
print("2020/02 : " + "{:,}".format(remaining))
# 2020/03
remaining = math.ceil(remaining * month_rate)
print("2020/03 : " + "{:,}".format(remaining))
# 2020/04
remaining = math.ceil(remaining * month_rate)
print("2020/04 : " + "{:,}".format(remaining))
# 2020/05
remaining = math.ceil(remaining * month_rate)
print("2020/05 : " + "{:,}".format(remaining))
# 2020/06
remaining = math.ceil(remaining * month_rate)
remaining = remaining - 1000000
payment += 1000000
print("2020/06に100万円繰越返済")
print("2020/06 : " + "{:,}".format(remaining))
# 2020/07
remaining = math.ceil(remaining * month_rate)
print("2020/07 : " + "{:,}".format(remaining))
# 2020/08
remaining = math.ceil(remaining * month_rate)
print("2020/08 : " + "{:,}".format(remaining))
# 2020/09
remaining = math.ceil(remaining * month_rate)
print("2020/09 : " + "{:,}".format(remaining))
# 2020/10
remaining = math.ceil(remaining * month_rate)
print("2020/10 : " + "{:,}".format(remaining))
# 2020/11
remaining = math.ceil(remaining * month_rate)
remaining = remaining - 1000000
payment += 1000000
print("2020/11に100万円繰越返済")
print("2020/11 : " + "{:,}".format(remaining))
# 2020/12
remaining = math.ceil(remaining * month_rate)
print("2020/12 : " + "{:,}".format(remaining))
# 2021/01
remaining = math.ceil(remaining * month_rate)
print("2021/01 : " + "{:,}".format(remaining))
# 2021/02
remaining = math.ceil(remaining * month_rate)
print("2021/02 : " + "{:,}".format(remaining))
# 2021/03
remaining = math.ceil(remaining * month_rate)
print("2021/03 : " + "{:,}".format(remaining))
# 2021/04
remaining = math.ceil(remaining * month_rate)
print("2021/04 : " + "{:,}".format(remaining))
# 2021/05
remaining = math.ceil(remaining * month_rate)
remaining = remaining - 1000000
payment += 1000000
print("2021/05に100万円繰越返済")
print("2021/05 : " + "{:,}".format(remaining))
# 2021/06
remaining = math.ceil(remaining * month_rate)
print("2021/06 : " + "{:,}".format(remaining))
# 2021/07
remaining = math.ceil(remaining * month_rate)
print("2021/07 : " + "{:,}".format(remaining))
# 2021/08
remaining = math.ceil(remaining * month_rate)
remaining = remaining - 1500000
payment += 1500000
print("2021/08に150万円繰越返済")
print("2021/08 : " + "{:,}".format(remaining))
# 2021/09
remaining = math.ceil(remaining * month_rate)
print("2021/09 : " + "{:,}".format(remaining))
# 2021/10
remaining = math.ceil(remaining * month_rate)
print("2021/10 : " + "{:,}".format(remaining))
# 2021/11
remaining = math.ceil(remaining * month_rate)
print("2021/11 : " + "{:,}".format(remaining))
# 2021/12
remaining = math.ceil(remaining * month_rate)
print("2021/12 : " + "{:,}".format(remaining))
# 2022/01
#print("2022/01に一部屋を5000,000で幸宏さんに移管")
#remaining = remaining + 5000000
remaining = math.ceil(remaining * month_rate)
print("2022/01 : " + "{:,}".format(remaining))
remaining = remaining - 1000000
payment += 1000000
print("2022/01に100万円繰越返済")
print("2022/01 : " + "{:,}".format(remaining))
# 2022/02
remaining = math.ceil(remaining * month_rate)
print("2022/02 : " + "{:,}".format(remaining))
# 2022/03
remaining = math.ceil(remaining * month_rate)
print("2022/03 : " + "{:,}".format(remaining))
# 2022/04
remaining = math.ceil(remaining * month_rate)
print("2022/04 : " + "{:,}".format(remaining))
# 2022/05
remaining = math.ceil(remaining * month_rate)
remaining = remaining - 1000000
payment += 1000000
print("2022/05に100万円繰越返済")
print("2022/05 : " + "{:,}".format(remaining))
# 2022/06
remaining = math.ceil(remaining * month_rate)
print("2022/06 : " + "{:,}".format(remaining))
# 2022/07
remaining = math.ceil(remaining * month_rate)
print("2022/07 : " + "{:,}".format(remaining))
# 2022/08
remaining = math.ceil(remaining * month_rate)
print("2022/08 : " + "{:,}".format(remaining))
# 2022/09
remaining = math.ceil(remaining * month_rate)
print("2022/09 : " + "{:,}".format(remaining))
# 2022/10
remaining = math.ceil(remaining * month_rate)
print("2022/10 : " + "{:,}".format(remaining))
# 2022/11
remaining = math.ceil(remaining * month_rate)
print("2022/11 : " + "{:,}".format(remaining))
# 2022/12
remaining = math.ceil(remaining * month_rate)
remaining = remaining - 1000000
payment += 1000000
print("2022/12に100万円繰越返済")
print("2022/12 : " + "{:,}".format(remaining))
print("---------------支払い済み金額-----------------------------" )
#payment = start - remaining
print("支払い金額合計 : " +"{:,}".format(payment) )
print("残債 : " +"{:,}".format(remaining) )
