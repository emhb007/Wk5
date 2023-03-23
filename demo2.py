def my_func(file, dir, user='root'):
    print('file: {:}, dir: {:}, to: {:} '.
    format(file, dir, user))

my_func('one', 'two', 'three')
my_func('one', 'two')



def my_func(dir, *files):
    print('dir:', dir, 'files to process are:', files)
my_func('c:/stuff', 'f1.txt', 'f2.txt', 'f3.txt')

my_func('c:/stuff', 'f1.txt', 'f2.txt', 'f3.txt', 'f4.txt')
my_func('c:/stuff', 'f1.txt')
my_func('c:/stuff', 'f1.txt', 'f2.txt', 'f3.txt', 'f4.txt', 'f1.txt', 'f2.txt', 'f3.txt', 'f4.txt')

def print_vat(**kwargs):
    print(kwargs)
    print(kwargs['vatpc'])
print_vat(vatpc=15, gross=9.55, message='Summary', something_mad="blah")