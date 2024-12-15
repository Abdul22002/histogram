def histogram(fin):
    hist = dict()
    # Read every line in fin
    with open(fin, 'r') as file:
        for line in fin : 
        # Split() the line into a list of words
            words = line.split()
        # Process every word in the list
            for word in words:
            # Convert each word to lower case
                word = word.lower().strip(",.!?;:\"()[]{}")
            # Check if each word is in the dictionary    
                if word in hist:
                    hist[word] +=1  ###
    # If not, add it
                else:
                    hist[word] = 1
    return hist
def printHistogram(hist):
        print("Word Count")
        print("----------------")
        for word in hist:
            print(f"{word:<12}{hist[word]:2d}")
        fin = open('Myra.txt')
        print('Reading file Myra.txt...')
        hist = histogram(fin)
        printHistogram(hist)
# Check if each word is in the dictionary
        if word in hist:
            print()