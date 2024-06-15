subjects = ["I", "You"]
verbs = ["Play", "Love"]
objects = ["Cricket", "Ludo"]

for subject in subjects:
    for verb in verbs:
        for object in objects:
            sentence = f"{subject} {verb} {object}."
            print(sentence)