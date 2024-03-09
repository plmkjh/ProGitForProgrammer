# if判斷句
hungry=True
if hungry:
    print("我就去吃飯")

rainy=True
if rainy:
    print("我就開車上班")
else:
    print("我走路上班")

# ==用於判斷是否相等，!=用於判斷是否不相等
grades=100
if grades==100:
    print("我給你一千")
elif grades>=80:
    print("我給你五百")
elif grades>=60:
    print("我給你一百")
else:
    print("你給我三百")

# and
grades=100
rainy=True
if grades==100 and rainy:
    print("我給你一千")
else:
    print("你給我三百")

# or
grades=100
rainy=True
if grades==100 or rainy:
    print("我給你一千")
else:
    print("你給我三百")

# or not
grades=100
rainy=True
if grades==100 or not(rainy):
    print("我給你一千")
else:
    print("你給我三百")