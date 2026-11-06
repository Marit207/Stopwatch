BreakVar = False
Teller = 0

def on_button_pressed_a():
    global BreakVar, Teller
    BreakVar = False
    while BreakVar == False:
        Teller += 1
        basic.show_number(Teller)
        if False:
            break
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global BreakVar
    BreakVar = True
input.on_button_pressed(Button.B, on_button_pressed_b)
