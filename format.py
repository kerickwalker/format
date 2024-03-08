import sys

"""
Format takes in an integer L and a text file.
It will read the text file, and format it such that there are no 
more than L characters on the line, while minimizing the whitespace
at the end of lines.  It then prints out the formatted string as well
as the total penalty associated with that string
"""
def format(L, filename):
    pen_table = {}  
    split_table = {}    

    words = []

    #get the words out of the txt file
    with open(filename, 'r') as file_in:
        for line in file_in:
            words.extend(line.split())
    
    # Initialize penalty_table and split_table
    for i in range(len(words)):
        pen_table[i] = float('inf')
        split_table[i] = 0

    pen_table[len(words)] = 0
    
    
    # Fill in dynamic programming tables
    for i in range(len(words) - 1, -1, -1):
        for j in range(i, len(words)):
            vals = words[i:j+1]
            pen = penalty(L, vals)
            if pen == float('inf'):
                break
            elif (pen + pen_table[j+1]) < pen_table[i]:
                pen_table[i] = penalty(L, vals) + pen_table[j+1]
                split_table[i] = j + 1
    
    # Print the total penalty
    print(pen_table[0])
    
    # Initalize the return string
    ret_string = ""

    # Fill out the return string based off the split table
    i = 0
    while True:
        nextline = split_table[i]
        if (nextline == len(words)):
            for j in range(i, nextline):
                ret_string += words[j]+ " "
            break
        else:
            for j in range(i, nextline):
                ret_string += words[j]+ " "
            ret_string += "\n"

        i = split_table[i]

    # Print the return string
    print(ret_string)

        
"""
This helper function calculates the penalty for a given subarray. 
It takes in the subarray as well as L, the maximum length of characters for a 
line. It returns the slack cubed, or if L is less than the length of the subarray
it returns infinity. 
"""
def penalty(L, subarray):
    sum_length = sum(len(word) + 1 for word in subarray) - 1 
    slack = L - sum_length
    if slack >= 0:
        return slack ** 3
    else:
        return float('inf')
    
"""
Main takes in the L and txt filename from the command line and runs format.
"""
def main():
    L = int(sys.argv[1])
    filename = str(sys.argv[2])
    format(L, filename)

if __name__ == "__main__":
    main()