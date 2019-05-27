count = {}

def find_substring():
    string = input("Enter the sring : ")
    for i in string:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return len(count.keys())

print(find_substring())
