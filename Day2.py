import copy

def Day2(input):
    index = 0
    series = input

    series[1] = 12
    series[2] = 2

    while index < len(input):
        if input[index] == 1:
            #addition
            val = input[input[index + 1]] + input[input[index + 2]]
            input[input[index + 3]] = val
        elif input[index] == 2:
            #multiplication
            val = input[input[index + 1]] * input[input[index + 2]]
            input[input[index + 3]] = val
        elif input[index] == 99:
            break
        
        index = index + 4

    return series

def Day2Part2(inp):
    firstVal = 0
    secondVal = 0
    it = 0
    series = copy.copy(inp)

    while series[0] != 19690720:   
        secondVal = secondVal + 1 
        print("inp starts with " + str(inp[0]) + " " + str(inp[1]) + " " + str(inp[2]) + " " + str(inp[3]))
        series = copy.copy(inp)
        index = 0

        if secondVal > 99:
            secondVal = 0
            firstVal = firstVal + 1
        
        if firstVal > 99:
            print("First value exceeded 100")
            break

        series[1] = firstVal
        series[2] = secondVal

        # if first:
        #     series[1] = series[1] + it
        # else:
        #     series[2] = series[2] + it
        # first = not first
        
        it = it + 1
        print("iteration nr " + str(it))
        print("Series starts with " + str(series[0]) + " " + str(series[1]) + " " + str(series[2]) + " " + str(series[3]))
        while index < len(series):
            if series[index + 3] > len(series):
                break
            elif series[index] == 1:
                #addition
                val = series[series[index + 1]] + series[series[index + 2]]
                series[series[index + 3]] = val
            elif series[index] == 2:
                #multiplication
                val = series[series[index + 1]] * series[series[index + 2]]
                series[series[index + 3]] = val
            elif series[index] == 99:
                break
        
            index = index + 4
        



    return series

test = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,2,9,19,23,2,13,23,27,1,6,27,31,2,6,31,35,2,13,35,39,1,39,10,43,2,43,13,47,1,9,47,51,1,51,13,55,1,55,13,59,2,59,13,63,1,63,6,67,2,6,67,71,1,5,71,75,2,6,75,79,1,5,79,83,2,83,6,87,1,5,87,91,1,6,91,95,2,95,6,99,1,5,99,103,1,6,103,107,1,107,2,111,1,111,5,0,99,2,14,0,0]
print(Day2Part2(test))
