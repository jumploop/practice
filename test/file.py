with open('cafe.txt', 'w', encoding='utf-8') as f:
    f.write('cafe')
with open('cafe.txt',encoding='utf-8') as f:
    msg = f.read()
    print(msg)
