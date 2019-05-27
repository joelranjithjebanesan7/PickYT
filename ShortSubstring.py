count = {}

def find_substring(string):
    for i in string:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return len(count.keys())

string = 'bcaacbc'
print(find_substring(string))
