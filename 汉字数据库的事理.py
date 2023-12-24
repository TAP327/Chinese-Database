import json

file = open("汉字数据库.json", "r")
data = json.load(file)
print("correctly read")


def zhsearch():
    result = []
    for entry in data:
        if input in entry["character"]:
            result = result + [x for x in data]
            # I feel like return shouldn't be indented so much.  I think it should be in like with the for loop.
            return result
