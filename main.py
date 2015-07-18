import json


#program to iteratively give sentiment for the tweets by hand..


if __name__ == "__main__":
    
    
    #open the file
    json_data = open('data.txt')
    data = json.load(json_data)
    json_data.close

    
    
    #ask user at which index to start..
    print len(data)
    input_index = raw_input("at which index to start? \n")
    startIndex = int(input_index)
    input_indexEnd = raw_input("at which index to stop \n")
    endIndex = int(input_indexEnd)
    
    print "start at " + str(startIndex) + " end at " + str(endIndex)
    
    #iterative loop, loop prints the tweet and then asks input for negative or positive..
    for i in range(startIndex, endIndex):
        print str(i) + " " + data[i]["text"].encode("utf-8")
        input_sentiment = raw_input("input: ")
        
        #if no input given then proceed to next one, if input given store it as a new value..
        if input_sentiment != "":
            data[i]["sentiment"] = input_sentiment
    
            
    #save data back to file
    with open('data.txt', 'w') as outfile:
            json.dump(data, outfile)        
    
    
    
    