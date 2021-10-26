text_list: List[str] = []

def on_gesture_shake():
    global text_list
    text_list = ["Yes.",
        "No.",
        "Possibly.",
        "The outcome is unlikely.",
        "Cannot determine."]
    basic.show_string("" + (text_list._pick_random()))
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
