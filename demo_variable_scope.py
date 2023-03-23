result = 3
def scope_test1():
    result = 42
    print("inside the function: (local scope)",result)

scope_test1()
#print("outside the function", result)

def scope_test2():
    global result
    result = 42
    print("inside the function: (global scope)", result)

scope_test2()
print(result)