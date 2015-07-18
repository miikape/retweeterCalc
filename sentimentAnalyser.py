import json
import unirest


if __name__ == "__main__":
    
    #1st open the tweet data and load to json
    json_data = open('LetsTalkBitcoin_data_sentiment.txt')
    data = json.load(json_data)
    json_data.close
    
    #2nd loop for sentiment, store the result as item in the tweets json list
    
    
    for i in range(len(data)):
    
        response = unirest.post("https://japerk-text-processing.p.mashape.com/sentiment/",
            headers={
                "X-Mashape-Key": "insert your mashape key here",
                "Content-Type": "application/x-www-form-urlencoded",
                "Accept": "application/json"
            },
            params={
                "language": "english",
                "text": data[i]["text"].encode("utf-8")
            }
        )
        print i
        data[i]["sentiment"] = response.body
        
    with open('cryptocoinsnews_data_sentiment.txt', 'w') as outfile:
            json.dump(data, outfile)
        
    
    
    
    # 
    # for i in range(0,5):
    # 
    #     url = "http://text-processing.com/api/sentiment/"
    #     text = {'text':'this is a very bad situation'}
    #     text['text'] = data[i]["text"].encode("utf-8") 
    #     r = requests.post(url, text)
    # 
    #     print r.text    
    
    
    
