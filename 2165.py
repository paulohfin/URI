while True:
    try:
        l = input()
        if len(l) > 140:
            print("MUTE")
        else:
            print('TWEET')
    except EOFError:
        break