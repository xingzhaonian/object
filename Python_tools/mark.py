def mark(data):
    def master(function):
        def warper():
            for i in data:
                function(i)
        return warper
    return master


@mark([1, 2, 3, 4, 5])
def testCase(data=None):
    print(data)
testCase()

#mark([1, 2, 3, 4, 5])(testCase)()
