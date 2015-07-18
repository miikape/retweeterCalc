import json

if __name__ == "__main__":
    
    
    #1 load both files data2 and reTweeterIndex
    json_data = open('masterretweeterlist2.txt')
    data = json.load(json_data)
    json_data.close
    
    
    #2 print the tweet sentiment and amount of retweeters
    for i in range(0, len(data)):
        
        print data[i][1].encode("utf-8") + " " + str(len(data[i][2])) + " " + data[i][3]
    
        
    
        