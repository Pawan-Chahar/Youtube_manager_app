list = [{'name': 'chai', 'time': '2min'} ,{'name': 'code' , 'time': '3 min'}]

enumerate(list , start=1)

for i in enumerate(list, start=1):
    print(i)

print('/n  ')

for i , video in enumerate(list, start=1):
    print(f"{i},   {video['name']}")