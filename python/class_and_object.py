# 類別，物件

class Phone:
    def __init__(self,os,number,is_waterproof):
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof

phone1 = Phone("ios",123,True)

print(phone1.os)

# 物件函式

class Phone:
    def __init__(self,os,number,is_waterproof):
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof
    
    def is_ios(self):
        if self.os == "ios":
            return True
        else:
            return False
    def add(self,num1,num2):
        return num1+num2
print(phone1.is_ios())

# 繼承，自別的類別引入函式加入另一個類別
from 模組名稱 import 繼承類別名稱
class Phone(繼承類別名稱):
    def __init__(self,os,number,is_waterproof):
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof