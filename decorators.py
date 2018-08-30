from functools import wraps

print('-> Blueprint:')

def decorator_name(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not can_run:
            return "Function will not run"
        return f(*args, **kwargs)
    return decorated


@decorator_name
def func_name():
    return("Function is running")


can_run = True
print(func_name())

can_run = False
print(func_name())

##########

print('-> Authorise:')

def decorator_authorise(func):

    def wrapper(request):
        if request['user'] == 'admin':
            print('User is not admin. Request can not be handled.')
            return
        print('User is admin.x§')
        func(request)

    return wrapper


@decorator_authorise
def handle_request(request):
    print('Handle reques from user {}.'.format(request['user']))

handle_request({'user': 'admin'})
handle_request({'user': 'john'})

##########
print('-> Decorator with arguments:')

def log(logfile='out.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            func()
            log_string = func.__name__ + " была исполнена"
            print(log_string)
            with open(logfile, 'a') as opened_file:
                opened_file.write(log_string + '\n')
        return wrapped_function
    return logging_decorator


@log('default.log')
def func_log():
    print('Execute some logic')

func_log()
