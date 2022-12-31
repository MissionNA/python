#자료구조의 변경
#type=어떤 집합인지 알려줌

menu={'커피','우유','주스'}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu=set(menu)
print(menu, type(menu))
