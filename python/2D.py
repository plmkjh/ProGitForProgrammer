# 2維列表

nums = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [9]
]

print(nums[0][0])

# 巢狀迴圈
# row是行，col是列
for row in nums:
    for col in row:
        print(col)