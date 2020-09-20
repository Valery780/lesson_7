def count_words(function):
    func = function()
    print(func.split())
    return func


@count_words
def string():
    return input("Enter the string:")
