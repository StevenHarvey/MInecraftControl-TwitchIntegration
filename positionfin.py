from ahk import AHK, Hotkey
num = 0
def main():
    ahk = AHK()
    ahk.key_wait('p')
    print(ahk.mouse_position)
    num + 1
    main()
main()
