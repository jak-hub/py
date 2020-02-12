a,b=5,4

try:
    print("RESOURCE OPENED")
    print(a/b)
    QQ=(int)(input("ENTER: "))
    print(QQ)
except ZeroDivisionError as e:
    print("can't be divided-",e)

except TypeError as q:
    print("Invalid type-",q)

except Exception as w:
    print(w)

finally:
    print("RESOURCE CLOSED")
