#import

# user functions
def demo_no_params():
    print("-"*20)

def make_list(val="Test", times=2):
    demo_no_params()
    res = str(val) * times
    return res


my_function_value = make_list("Test", 5)
my_function_value = make_list(5, 5)
print(make_list("blah ", 3))
demo_no_params()
print(my_function_value)
demo_no_params()


def change_list(inlist, val, times):
    inlist += str(val) * times

mylist=[]
change_list(mylist, 'h', 8)
print(mylist)


def print_vat(gross, vatpc=17.5, message='Summary:'):
    net = gross/(1 + (vatpc/100))
    vat = gross - net
    print(message, 'Net: {0:5.2f} Vat: {1:5.2f}'.format(net, vat))
print_vat(9.55)
print_vat(159.55, vatpc=20, message="Your bill is")

print(make_list())
print(make_list(times=4))