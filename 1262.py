while True:
    try:
        rastro = input()
        p = int(input())
        
        contR = 0
        contp = 0
        for i in rastro:
            if i == 'W':
                contp += 1
                contR = 0
            else:
                if contR == 0:
                    contp+=1
                    
                contR+=1
                if contR > p:
                    contp += 1
                    contR = 1
        print(contp)
    except EOFError:
        break