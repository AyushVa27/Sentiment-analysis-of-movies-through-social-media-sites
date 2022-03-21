import json
import requests
import os 
import time
import tqdm

class tweepy:

    response = ""
    config = ""

    def __init__(self):
        # reading config data
        data = open("config.json")
        self.config = json.load(data)

    def search_tweets(self,search_topic, max_results):
        api_url = 'https://api.twitter.com/2/tweets/search/recent'
        headers = {
            'Authorization': 'Bearer ' + self.config['Bearer_token']
        }
        params = (
            ('query', search_topic),
            ('max_results', max_results)
        )

        api_response = requests.get(api_url, headers=headers, params=params)
        print("......Getting Tweeet Response")
        for i in tqdm.tqdm (range(int(max_results)), desc="Loading..."):
            time.sleep(0.05)

        print(api_response)
        self.response = api_response.json()

        return self.response

    def generate_data_file(self,file_name,print_each_line = False):
        if self.response == "": return False

        dirPath = os.getcwd()
        newPath = dirPath + f"/Data/{file_name}.txt"

        with open(newPath,'a') as file_object:
            for index,data in enumerate(self.response['data'],1):
                build_string = ""
                build_string += str(index) + " "
                build_string += data['text'] + "\n"
                
                if print_each_line: print(build_string)
                file_object.writelines(build_string)

        return True
            
topic_name = input("Enter topic to search : ")
number_of_tweets = input("Number of tweets [10-100] : ")
print_tweets = input("Print tweets fetcheed [True/False] : ")
print_response = input("Print Response Content [True/False] : ")

test = tweepy()
test.search_tweets(topic_name,number_of_tweets)
if print_response.lower() == "true" : print(test.response)
test.generate_data_file(topic_name,print_tweets.lower() == "true")





