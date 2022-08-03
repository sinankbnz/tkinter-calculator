def check_scope():
    def local():
        test="local test"
    def non_local():
        nonlocal test
        test="non local test"
    def _global():
        global test
        test="Global test"
    test="Default test"
    local()
    print("After calling local Variable",test)
    non_local()
    print("After calling non local Variable",test)
    _global()
    print("After calling Gloabel Variable",test)
check_scope()
print("After calling Global Variable",test)