#1.加入例外處理
#2.重複輸入 直到a=>exit 離開. 使用while true



a=eval(input("請輸入a:"))
b=eval(input("請輸入b:"))

if a==b:
    print("a=b")
elif a>b:
    print(f"a>b, 相差:{a-b}")
else:
    print(f"a<b, 相差:{b-a}")
