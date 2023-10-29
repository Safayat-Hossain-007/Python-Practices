# If a name is bound inside a function, it is by default accessible only within the function:
# def foo():
#     a = 5
#     print(a) # ok
# print(a) # NameError: name 'a' is not defined

def foo():
    if True:
        a = 5
        print(a) # ok
foo()

# b = 3
# def bar():
#     if False:
#         b = 5
#     print(b) # UnboundLocalError: local variable 'b' referenced before assignment
# bar()