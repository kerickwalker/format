
def function1(L, filename):
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
    


    for i in range(len(words) - 1, -1, -1):
        for j in range(i, len(words)):
            vals = words[i:j+1]
            if (penalty(L, vals) + pen_table[j+1]) < pen_table[i]:
                pen_table[i] = penalty(L, vals) + pen_table[j+1]
                split_table[i] = j + 1


    print(pen_table)
    print(split_table)
    

    lines = []
    split_val = 0


    #go through split table 
        #fill up the line with words until we see the split value change 
        #when it changes, start new line

   
    # Print the lines
    for line in lines:
        print(line)
        

def penalty(L, subarray):
    sum_length = sum(len(word) + 1 for word in subarray) - 1  # Account for spaces between words
    slack = L - sum_length
    if slack >= 0:
        return slack ** 3
    else:
        return float('inf')
    

def main():
    function1(10, "sample.txt")

if __name__ == "__main__":
    main()




