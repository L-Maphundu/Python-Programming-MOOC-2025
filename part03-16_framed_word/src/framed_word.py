# Write your solution here
word = input("Word: ").strip()
print('*'*30)

frame = (30 - len(word))//2

if len(word) % 2 == 0:
    print('*' + ' '*(frame-1) + word + ' '*(frame-1) + '*')
else:
    print('*' + ' '*(frame-1) + word + ' '*(frame) + '*')

print('*'*30)