def Day5(puzzleInput, inputValue):
    index = 0
    series = puzzleInput
    output = []

    while index < len(series):
        word = str(series[index])
        if len(word) == 4:
            instruction = int(word[2:]) #Addition/Multiplication, etc
            firstMode = int(word[1]) # Position Mode / Immediate Mode for Parameter 1
            secondMode = int(word[0]) # Position Mode / Immediate Mode for Parameter 2
        elif len(word) == 3:
            instruction = int(word[1:]) #Addition/Multiplication, etc
            firstMode = int(word[0]) # Position Mode / Immediate Mode for Parameter 1
            secondMode = 0 # Position Mode / Immediate Mode for Parameter 2
        elif len(word) <= 2:
            instruction = series[index] #Addition/Multiplication, etc
            firstMode = 0 # Position Mode / Immediate Mode for Parameter 1
            secondMode = 0 # Position Mode / Immediate Mode for Parameter 2

        if instruction == 1:
            #addition
            if firstMode == 0:
                firstValue = series[series[index + 1]]
            elif firstMode == 1:
                firstValue = series[index + 1]
            
            if secondMode == 0:
                secondValue = series[series[index + 2]]
            elif secondMode == 1:
                secondValue = series[index + 2]
            
            val = firstValue + secondValue

            series[series[index + 3]] = val
            index = index + 4
        elif instruction == 2:
            #multiplication
            if firstMode == 0:
                firstValue = series[series[index + 1]]
            elif firstMode == 1:
                firstValue = series[index + 1]
            
            if secondMode == 0:
                secondValue = series[series[index + 2]]
            elif secondMode == 1:
                secondValue = series[index + 2]
            
            val = firstValue * secondValue

            series[series[index + 3]] = val
            index = index + 4
        elif instruction == 3:
            series[series[index + 1]] = inputValue
            index = index + 2
        elif instruction == 4:
            output.append(series[series[index + 1]])
            index = index + 2
        elif instruction == 99:
            break 

    return output

def Day5Part2(puzzleInput, inputValue):
    index = 0
    series = puzzleInput
    output = []

    while index < len(series):
        word = str(series[index])
        if len(word) == 4:
            instruction = int(word[2:]) #Addition/Multiplication, etc
            firstMode = int(word[1]) # Position Mode / Immediate Mode for Parameter 1
            secondMode = int(word[0]) # Position Mode / Immediate Mode for Parameter 2
        elif len(word) == 3:
            instruction = int(word[1:]) #Addition/Multiplication, etc
            firstMode = int(word[0]) # Position Mode / Immediate Mode for Parameter 1
            secondMode = 0 # Position Mode / Immediate Mode for Parameter 2
        elif len(word) <= 2:
            instruction = series[index] #Addition/Multiplication, etc
            firstMode = 0 # Position Mode / Immediate Mode for Parameter 1
            secondMode = 0 # Position Mode / Immediate Mode for Parameter 2

        if instruction == 1:
            #addition
            if firstMode == 0:
                firstValue = series[series[index + 1]]
            elif firstMode == 1:
                firstValue = series[index + 1]
            
            if secondMode == 0:
                secondValue = series[series[index + 2]]
            elif secondMode == 1:
                secondValue = series[index + 2]
            
            val = firstValue + secondValue

            series[series[index + 3]] = val
            index = index + 4
        elif instruction == 2:
            #multiplication
            if firstMode == 0:
                firstValue = series[series[index + 1]]
            elif firstMode == 1:
                firstValue = series[index + 1]
            
            if secondMode == 0:
                secondValue = series[series[index + 2]]
            elif secondMode == 1:
                secondValue = series[index + 2]
            
            val = firstValue * secondValue

            series[series[index + 3]] = val
            index = index + 4
        elif instruction == 3:
            series[series[index + 1]] = inputValue
            index = index + 2
        elif instruction == 4:
            output.append(series[series[index + 1]])
            index = index + 2
        elif instruction == 5:
            if firstMode == 0:
                if series[series[index + 1]] == 0:
                    index = index + 3
                else:
                    if secondMode == 0:
                        index = series[series[index + 2]]
                    elif secondMode == 1:
                        index = series[index + 2]
            elif firstMode == 1:
                if series[index + 1] == 0:
                    index = index + 3
                else:
                    index = index + 3
        elif instruction == 6:
            if series[index + 1] == 0:
                index = series[index + 2]
            else:
                index = index + 3
        elif instruction == 7:
            if series[index + 1] < series[index + 2]: # first parameter is smaller than second parameter
                series[series[index + 3]] = 1
            else:
                series[series[index + 3]] = 0
            index = index + 4
        elif instruction == 8:
            if series[index + 1] == series[index + 2]: # first parameter is equal to the second parameter
                series[series[index + 3]] = 1
            else:
                series[series[index + 3]] = 0
            index = index + 4
        elif instruction == 99:
            break 

    return output

test = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,88,66,225,101,8,125,224,101,-88,224,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,1101,87,23,225,1102,17,10,224,101,-170,224,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1101,9,65,225,1101,57,74,225,1101,66,73,225,1101,22,37,224,101,-59,224,224,4,224,102,8,223,223,1001,224,1,224,1,223,224,223,1102,79,64,225,1001,130,82,224,101,-113,224,224,4,224,102,8,223,223,1001,224,7,224,1,223,224,223,1102,80,17,225,1101,32,31,225,1,65,40,224,1001,224,-32,224,4,224,102,8,223,223,1001,224,4,224,1,224,223,223,2,99,69,224,1001,224,-4503,224,4,224,102,8,223,223,101,6,224,224,1,223,224,223,1002,14,92,224,1001,224,-6072,224,4,224,102,8,223,223,101,5,224,224,1,223,224,223,102,33,74,224,1001,224,-2409,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,107,677,677,224,1002,223,2,223,1006,224,329,101,1,223,223,108,677,677,224,1002,223,2,223,1005,224,344,101,1,223,223,1007,677,677,224,1002,223,2,223,1006,224,359,101,1,223,223,1107,226,677,224,1002,223,2,223,1006,224,374,1001,223,1,223,8,677,226,224,1002,223,2,223,1006,224,389,101,1,223,223,1108,677,677,224,1002,223,2,223,1005,224,404,1001,223,1,223,7,226,226,224,1002,223,2,223,1006,224,419,101,1,223,223,1107,677,677,224,1002,223,2,223,1005,224,434,101,1,223,223,107,226,226,224,102,2,223,223,1005,224,449,101,1,223,223,107,677,226,224,1002,223,2,223,1006,224,464,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,479,1001,223,1,223,108,677,226,224,102,2,223,223,1005,224,494,1001,223,1,223,1108,677,226,224,1002,223,2,223,1005,224,509,1001,223,1,223,1107,677,226,224,1002,223,2,223,1005,224,524,101,1,223,223,1008,226,226,224,1002,223,2,223,1006,224,539,101,1,223,223,1008,226,677,224,1002,223,2,223,1005,224,554,1001,223,1,223,7,226,677,224,1002,223,2,223,1005,224,569,101,1,223,223,1007,677,226,224,1002,223,2,223,1006,224,584,1001,223,1,223,7,677,226,224,102,2,223,223,1006,224,599,101,1,223,223,1007,226,226,224,102,2,223,223,1006,224,614,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,629,101,1,223,223,108,226,226,224,102,2,223,223,1006,224,644,101,1,223,223,1108,226,677,224,1002,223,2,223,1005,224,659,101,1,223,223,8,226,226,224,1002,223,2,223,1005,224,674,101,1,223,223,4,223,99,226]
test2 = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
test3 = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
test4 = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

print(Day5Part2(test4, 5))