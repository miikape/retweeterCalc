import json



if __name__ == "__main__":
    
    
    #1 load both files data2 and reTweeterIndex
    json_data = open('masterretweeterlist.txt')
    data = json.load(json_data)
    json_data.close
    
    json_data2 = open('retweeterset.txt')
    retweeterset = json.load(json_data2)
    json_data2.close
    
    
    #2 calculate how many times p n occur for each retweeter..
    #iterate
    
    #iteration for every retweeter
    for i in range(0, len(retweeterset)):
        countp = 0
        countn = 0
        #iteration for all the tweets
        for k in range(0, len(data)):
            
            #iteration for all the retweeters in one tweet
            for m in range(0, len(data[k][2])):
                if retweeterset[i] == data[k][2][m]:
                    if data[k][1] == "p":
                        countp = countp + 1
                    if data[k][1] == "n":
                        countn = countn + 1
        
        #save to retweeterset
        tList = []
        tList.append(retweeterset[i])
        tList.append(countp)
        tList.append(countn)
        retweeterset[i] = tList
    
    
    #optional print
    for i in range(0, len(retweeterset)):
        print retweeterset[i][0].encode("utf-8") + "\t" + str(retweeterset[i][1]) + "\t" + str(retweeterset[i][2]) 
    
    countpos = 0
    countneg = 0
    for k in range(0, len(data)):
        if data[k][1] == "p":
            countpos = countpos + 1
        if data[k][1] == "n":
            countneg = countneg + 1
    
    print str(countpos)  + "\t" + str(countneg)
    
        
    
    
    
    #3 save data to reTweeterindex
    with open('results.txt', 'w') as outfile:
            json.dump(retweeterset, outfile) 