def test_var_args(f_arg, *argv):
    print("f_arg:", f_arg)
    i = 0
    for arg in argv:
        print("argv[{}]={}".format(i, arg))
        i+=1

test_var_args('yasoob', 'python', 'eggs', 'test')

print("-------------------------------------")
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

greet_me(name="hello", surname="world")

print("-------------------------------------")
def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

args = (1, 2, 3)
test_args_kwargs(*args)

kwargs = {"arg3": "three", "arg2": "two", "arg1": "one"}
test_args_kwargs(**kwargs)