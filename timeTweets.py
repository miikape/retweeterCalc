import json

if __name__ == "__main__":
    
    
    #1 load masterretweeterlist
    json_data = open('masterretweeterlist.txt')
    data = json.load(json_data)
    json_data.close
    
    #2load data.txt 
    json_data = open('data.txt')
    masterdata = json.load(json_data)
    json_data.close
    
    
    
    #3 go through every tweet in masterretweeterlist, take id, find it from masterdata and save the time to masterretweeterlist
    for i in range(0, len(data)):
        ID = data[i][0]
        
        for m in range(0, len(masterdata)):
            if ID == masterdata[m]["id"]:
                data[i].append(masterdata[m]["created_at"])
        
        
        
    
    #4 save to masterretweeterlist2
    with open('masterretweeterlist2.txt', 'w') as outfile:
            json.dump(data, outfile)    
    
    
    
    
   
    
        