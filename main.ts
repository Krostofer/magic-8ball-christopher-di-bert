let text_list: string[] = []
input.onGesture(Gesture.Shake, function () {
    text_list = [
    "Yes.",
    "No.",
    "Possibly.",
    "The outcome is unlikely.",
    "Cannot determine."
    ]
    basic.showString("" + (text_list._pickRandom()))
})
