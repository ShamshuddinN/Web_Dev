def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Function Run Completed")
    return wrapper

@announce
def hello():
    print("Hello Mars")

hello()