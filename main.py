# test1=[1,2,3,2,1]
# test2=test1.copy()
# test2.reverse()
#
#
# if test1==test2:
#     print("palindrome")
#
# else:
#     print("not a palindrome")



openerp = False
def testfun():
    result={
        "dict1" : "None",
        "hint" : "hello"
    }
    try:
        if openerp is True:
            print("Great")
            result.update({"hint":"hi"})
            print(result)



    except Exception as e:
        print("hello1")


a= testfun()