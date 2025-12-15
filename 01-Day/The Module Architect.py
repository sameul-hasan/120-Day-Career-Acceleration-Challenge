second = input ("Enter seconds: ")
print (second)
Houres = int (second) // 3600
print (Houres)
remain_second = int (second) % 3600
print (remain_second)
Min = remain_second // 60
print (Min)
Sec = remain_second % 60
print (Houres, ":", Min, ":", Sec)