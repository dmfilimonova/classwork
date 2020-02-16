import json
with open(r'C:\Users\Никитос\PycharmProjects\classwork\work\list.json', 'r') as f:
    data = json.load(f)
    for item in data:
        banana_list = list()
        strawberry_list = list()
        apple_list = list()
        fruits = item.get('favoriteFruit')
        if item.get('favoriteFruit') == 'banana':
            banana_list.append(item.get('name'))
        if item.get('favoriteFruit') == 'strawberry':
            strawberry_list.append(item.get('name'))
        else:
            apple_list.append(item.get('name'))
        print('banana:', banana_list)
        print('strawberry:', strawberry_list)
        print('apple:', apple_list)