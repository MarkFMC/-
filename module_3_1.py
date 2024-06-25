calls = 0
def count_calls():
    global calls
    calls +=1

def string_info(string):
    count_calls()
    a = len(string)
    b = string.lower()
    c = string.upper()
    return (a, b, c)

def is_contains(string, *list_to_search):
    count_calls()
    for i in list_to_search:
        if string.lower() in i.lower():
            return True
        else:
            return False

print(string_info("Атракцион"))
print(string_info('СупермегаБАЙКЕР'))
print(is_contains('сНег', 'снеговиК', 'Снежный', 'сНЕгурочка'))
print(is_contains('дождь', 'снеговик', 'снежный', 'снегурочка'))
print(calls)