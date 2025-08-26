# Write your solution here
while True:
    editor = input("Editor: ").strip().lower()

    if editor in ['emacs','vim','atom']:
        print("not good")
    elif editor in ['word','notepad']:
        print("awful")
    elif editor == 'visual studio code':
        print("an excellent choice!")
        break
    