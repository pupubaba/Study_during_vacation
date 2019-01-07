def return_false():
    print("함수return_false")
    return False

def return_true():
    print("함수return_true")
    return True

print('test1')
a = return_false()
b = return_true()
if a and b :
    print(True)
else:
    print(False)

print('test2')
if return_false() and return_true():
    print(True)
else:
    print(False)

dic = {"Key2" : "Value1"}

if "Key1" in dic and dic["Key1"]=="Value1":
    print("Key1도 있고, 그 값은 Value1이네")
else:
    print("아니네")