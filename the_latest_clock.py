def latest_clock(a, b, c, d):
    digits = sorted([a, b, c, d], reverse=True)

    
    # Hh:Mm

    # hours check
    if 2 in digits: # This checks if the H value can be 2
        for idx, digit in enumerate(digits): 
            if digit == 2:
                test = digits[:idx] + digits[idx+1:]
                for jdx, digit2 in enumerate(test): # checking for appropriate h value
                    if digit2 <= 3:
                        test2 = test[:jdx] + test[jdx+1:]

                        for kdx, digit3 in enumerate(test2):
                            if digit3 <= 5:
                                test3 = test2
                                test3.pop(kdx)
                                H = digit
                                h = digit2
                                M = digit3
                                m = (test2[:kdx] + test2[kdx:])[0]
                                return f"{H}{h}:{M}{m}"
    if 1 in digits:             
        for idx, digit in enumerate(digits): 
            if digit == 1:
                test = digits[:idx] + digits[idx+1:]
                for jdx, digit2 in enumerate(test):
                    if digit2 <= 9:
                        test2 = test[:jdx] + test[jdx+1:]
                        for kdx, digit3 in enumerate(test2):
                            if digit3 <= 5:
                                test3 = test2
                                test3.pop(kdx)
                                H = digit
                                h = digit2
                                M = digit3
                                m = (test2[:kdx] + test2[kdx:])[0]
                                return f"{H}{h}:{M}{m}"
    if 0 in digits:
        for idx, digit in enumerate(digits): 
            if digit == 0:
                test = digits[:idx] + digits[idx+1:]
                for jdx, digit2 in enumerate(test):
                    if digit2 <= 9:
                        test2 = test[:jdx] + test[jdx+1:]
                        for kdx, digit3 in enumerate(test2):
                            if digit3 <= 5:
                                test3 = test2
                                test3.pop(kdx)
                                H = digit
                                h = digit2
                                M = digit3
                                m = test3[0]
                                return f"{H}{h}:{M}{m}"

    
