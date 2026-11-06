let BreakVar = false
let Teller = 0
input.onButtonPressed(Button.A, function () {
    BreakVar = false
    while (BreakVar == false) {
        Teller += 1
        basic.showNumber(Teller)
        if (false) {
            break;
        }
    }
})
input.onButtonPressed(Button.B, function () {
    BreakVar = true
})
