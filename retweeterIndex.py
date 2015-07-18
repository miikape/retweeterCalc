import json

#makes a list of all retweeters

if __name__ == "__main__":
    
    
    #1 load data2
    #open the file
    json_data = open('masterretweeterlist.txt')
    data = json.load(json_data)
    json_data.close
    
    
    #2 create index of Tweeters..
    retweeterIndex = []
    
    for i in range(0, len(data)):
        for k in range(0, len(data[i][2])):
            retweeterIndex.append(data[i][2][k])
    
    
    #3remove duplicates
    retweeterIndex = list(set(retweeterIndex))
    
    #4 save set to new file
    
    with open('retweeterset.txt', 'w') as outfile:
            json.dump(retweeterIndex, outfile) 
    
    