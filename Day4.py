def Day4(start, end):
    nrValidCodes = 0

    for i in range(start, end, 1):
        if IsCodeValid(i):
            nrValidCodes += 1

    return nrValidCodes

def IsCodeValid(code):
    word = str(code)
    #Digits never decrease
    for index in range(5):
        if int(word[index]) <= int(word[index + 1]):
            pass
        else:
            return False

    #Check for duplicates
    hasDuplicate = False
    skipNumber = -1
    for index in range(5):
    
        if word[index] == skipNumber:
            continue
        else:
            skipNumber = -1

        if int(word[index]) == int(word[index + 1]):
            if index != 4:
                if int(word[index + 1]) == int(word[index + 2]):
                    skipNumber = word[index]
                else:
                    hasDuplicate = True
            else:
                hasDuplicate = True
    
    if hasDuplicate:
        return True

start = 137683
end = 596253
print(Day4(start, end))