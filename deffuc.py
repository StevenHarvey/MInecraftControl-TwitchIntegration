from ahk import AHK, Hotkey
import time
ahk = AHK()
global target
target = []


def forward():
    ahk.key_down('w')
    time.sleep(5)
    ahk.key_up('w')
    print('FORWARD DONE')


def left():
    ahk.key_down('a')
    time.sleep(2)
    ahk.key_up('a')
    print('LEFT DONE')


def right():
    ahk.key_down('d')
    time.sleep(2)
    ahk.key_up('d')
    print('LEFT DONE')


def back():
    ahk.key_down('s')
    time.sleep(5)
    ahk.key_up('s')
    print('LEFT DONE')


def start_break():
    ahk.click('down')
    time.sleep(5)
    ahk.key_up('a')
    print('LEFT DONE')


def stop_break():
    ahk.key_down('a')
    time.sleep(5)
    ahk.key_up('a')
    print('LEFT DONE')


def place():
    ahk.right_click()
    print('Print DONE')


def inventory(foo, argu1):
    ahk = AHK()
    if "active" not in target:
        if "tog" not in foo:
            if "a1" in foo:
                op = 2586, 589
            elif "a2" in foo:
                op = 2664, 593
            elif "a3" in foo:
                op = 2734, 591
            elif "a4" in foo:
                op = 2806, 583
            elif "a5" in foo:
                op = 2898, 583
            elif "a6" in foo:
                op = 2950, 577
            elif "a7" in foo:
                op = 3030, 580
            elif "a8" in foo:
                op = 3171, 586
            elif "a9" in foo:
                op = 3171, 586
            elif "b1" in foo:
                op = 2591, 646
            elif "b2" in foo:
                op = 2664, 645
            elif "b3" in foo:
                op = 2735, 647
            elif "b4" in foo:
                op = 2809, 645
            elif "b5" in foo:
                op = 2880, 646
            elif "b6" in foo:
                op = 2955, 646
            elif "b7" in foo:
                op = 3024, 646
            elif "b8" in foo:
                op = 3099, 647
            elif "b9" in foo:
                op = 3168, 646
            elif "c1" in foo:
                op = 2591, 719
            elif "c2" in foo:
                op = 2663, 717
            elif "c3" in foo:
                op = 2737, 717
            elif "c4" in foo:
                op = 2806, 717
            elif "c5" in foo:
                op = 2881, 718
            elif "c6" in foo:
                op = 2952, 717
            elif "c7" in foo:
                op = 3025, 717
            elif "c8" in foo:
                op = 3096, 720
            elif "c9" in foo:
                op = 3169, 720
            else:
                None
            if argu1 == "1":
                po = 1
            if argu1 == "2":
                po = 2
            if argu1 == "3":
                po = 3
            if argu1 == "4":
                po = 4
            if argu1 == "5":
                po = 5
            if argu1 == "6":
                po = 6
            if argu1 == "7":
                po = 7
            if argu1 == "8":
                po = 8
            if argu1 == "9":
                po = 9
            ahk.key_press('e')
            ahk.mouse_move(2121, 241)
            ahk.mouse_drag(op)
            ahk.key_press(str(po))
            ahk.key_press('e')
        else:
            ahk.key_press('e')
            target.append('active')
            print(target)
    else:
        if "active" in target:
            ahk.key_press('e')
            target.clear()
            print(target)
