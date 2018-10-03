def validate_age(fn):
    def wrapper():
        print('rubber baby buggy bumpers')
        fn()
    return wrapper
