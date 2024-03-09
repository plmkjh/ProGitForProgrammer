# 檔案讀取、寫入

open("檔案路徑", mode="開啟模式")
# 絕對路徑 ex: C:/Users/hibyby/Desktop/python/123.txt
# 相對路徑 以程式的位置做延伸

# mode="r" 讀取
# mode="w" 覆寫
# mode="a" 在原先的資料後寫東西

file = open("檔案路徑", mode="開啟模式", encoding="編碼格式") #ex.utf-8
print(file.read()) # readline讀取一行，readlines讀取多行
file.close() # 關閉檔案
file.write() # 寫入檔案
# 上下皆可，下方無須關閉檔案
with open("檔案路徑", mode="開啟模式", encoding="編碼格式") as file:
    file.write()
