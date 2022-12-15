import json
import requests
from urllib.request import urlopen
from datetime import datetime
import re
import sys

# I use this for more recursion
sys.setrecursionlimit(100000)



# Cache part
CACHE_FILENAME = "cache.json"

def open_cache():
    try:
        cache_file = open(CACHE_FILENAME, 'r')
        cache_contents = cache_file.read()
        cache_dict = json.loads(cache_contents)
        cache_file.close()
    except:
        cache_dict = {}
    return cache_dict

def save_cache(cache_dict):
    dumped_json_cache = json.dumps(cache_dict)
    fw = open(CACHE_FILENAME,"w")
    fw.write(dumped_json_cache)

FIB_CACHE = open_cache()

def fib_with_cache(n):
    if n in FIB_CACHE:
        return FIB_CACHE[n]
    else:
        FIB_CACHE[n] = get_text(n)
        save_cache(FIB_CACHE)
        return FIB_CACHE[n]

def get_text(url):
    response = requests.get(url).text
    RedliningData = json.loads(response)
    return RedliningData

href = "https://api.themoviedb.org/3/movie/top_rated?api_key=fcac3cfea82453c3bc910d1c10050adf"

for i in range(1,501):
    parameters = {"page":i}
    api_result = requests.get(href,params = parameters)
    fib_with_cache(api_result.url)

f = open('cache.json')

data = json.load(f)



# Because every page construct a dic, I use this way to make them into one list
list1 = []
for k, v in data.items():
    a = v["results"]
    list1 = list1+a



#Change the type of release_date to datetime format
for i in range(len(list1)):
    list1[i]['release_date'] = datetime.strptime(list1[i]['release_date'], '%Y-%m-%d')



# Make a class for building a tree to store data by the variable vote_average
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.avg = data['vote_average']

    # This function can be used to insert new node to a tree
    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data['vote_average'] <= self.avg:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data['vote_average'] > self.avg:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

    # This function can be used to screen movies in the range minimum and maximum by vote_average
    def search_range(root, minimum, maximum):
        nodes = []

        def recursive_search(node):
            if node is None:
                return None

            if node.avg > minimum:
                recursive_search(node.left)
            if minimum <= node.avg <= maximum:
                nodes.append(node.data)
            if node.avg < maximum:
                recursive_search(node.right)

        recursive_search(root)
        return nodes



# Make a class for building a tree to store data by the variable popularity 
class Node1:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.avg = data['popularity']

    # This function can be used to insert new node to a tree
    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data['popularity'] <= self.avg:
                if self.left is None:
                    self.left = Node1(data)
                else:
                    self.left.insert(data)
            elif data['popularity'] > self.avg:
                if self.right is None:
                    self.right = Node1(data)
                else:
                    self.right.insert(data)

    # This function can be used to screen movies in the range minimum and maximum by popularity
    def search_range(root, minimum, maximum):
        nodes = []

        def recursive_search(node):
            if node is None:
                return None

            if node.avg > minimum:
                recursive_search(node.left)
            if minimum <= node.avg <= maximum:
                nodes.append(node.data)
            if node.avg < maximum:
                recursive_search(node.right)

        recursive_search(root)
        return nodes



# Make a class for building a new tree to store data by the variable release_date 
class Node2:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.avg = data['release_date']

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data['release_date'] <= self.avg:
                if self.left is None:
                    self.left = Node2(data)
                else:
                    self.left.insert(data)
            elif data['release_date'] > self.avg:
                if self.right is None:
                    self.right = Node2(data)
                else:
                    self.right.insert(data)

    # This function can be used to screen movies in the range minimum and maximum by release date
    def search_range(root, minimum, maximum):
        nodes = []

        def recursive_search(node):
            if node is None:
                return None

            if node.avg > minimum:
                recursive_search(node.left)
            if minimum <= node.avg <= maximum:
                nodes.append(node.data)
            if node.avg < maximum:
                recursive_search(node.right)

        recursive_search(root)
        return nodes




if __name__ == '__main__':
    term = input("Do you want to search movies? If you don't just type quit ")
    if term == "quit":
        print("Bye!")
        quit()
    else:
        while True:
            print("This program has four methods to screen\n1: by average voting scores\n2: by popularity\n3: by release date\n4: by title")
            num = input("please input a number from 1-4, to show which one you want to use for screening; if you want to get the result, please enter result; if you want to quit, please enter quit ")
            #Screen movies based on average voting scores, and use first_output as the new list to screen 
            if num == "1":
                # Build a tree to store data by the variable average voting scores 
                new_list_node = Node(list1[0])
                for i in range(1, len(list1)):
                    new_list_node.insert(list1[i])
                # Get the right interval for average voting scores
                while True:
                    try:
                        vote_avg_rank_min = float(input("What is the low average vote score you want? Please input a number from 5.3-8.7 "))
                        vote_avg_rank_max = float(input("What is the high average vote score you want? Please input a number from 5.3-8.7, this number should be bigger than the low average vote score "))
                        list1 = new_list_node.search_range(vote_avg_rank_min,vote_avg_rank_max)
                        break
                    except:
                        print("Please input a number from 5.3-8.7 ")

            elif num == "2":
                # Build a tree to store data by the variable popularity 
                new_list_node = Node1(list1[0])
                for i in range(1, len(list1)):
                    new_list_node.insert(list1[i])
                # Get the right interval for popularity
                while True:
                    try:
                        popularity_min = float(input("What is the low popularity you want? Please input a number from 0-5400 "))
                        popularity_max = float(input("What is the high popularity you want? Please input a number from 0-5400, this number should be bigger than the low popularity "))
                        list1 = new_list_node.search_range(popularity_min,popularity_max)
                        break
                    except:
                        print("Please input a number from 0-5400 ")
                        
            elif num == "3":
                # Build a tree to store data by the variable release_date 
                new_list_node = Node2(list1[0])
                for i in range(1, len(list1)):
                    new_list_node.insert(list1[i])
                # Get the right interval for release date
                while True:
                    try:
                        release_date_min = input("What is the further release date you want? Please input a date from 1895-06-10 to 2022-12-02 in the format %Y-%m-%d(such as: 2000-01-01) ")
                        release_date_max = input("What is the recent release date you want? Please input a date from 1895-06-10 to 2022-12-02 in the format %Y-%m-%d(such as: 2000-01-01) , this date should be more recent than the further release date ")
                        release_date_min = datetime.strptime(release_date_min, '%Y-%m-%d')
                        release_date_max = datetime.strptime(release_date_max, '%Y-%m-%d')
                        list1 = new_list_node.search_range(release_date_min,release_date_max)
                        break
                    except:
                        print("Please input a date from 1895-06-10 to 2022-12-02 in the format %Y-%m-%d(such as: 2000-01-01) ")
            elif num == "4":
                new_list = []
                # Get the parameter for regex
                regex_part = input("Please enter the text you want in the movie title ")
                regex = "(?i)" + regex_part
                for i in range(len(list1)):
                    if re.findall(regex,list1[i]["original_title"]):
                        new_list.append(list1[i])
                # Use copy list1 from new_list
                list1 = new_list
            # Show the result of the movies
            elif num == "result":
                for i in range(len(list1)):
                    print(list1[i]["original_title"])
            # Quit the program
            elif num == "quit":
                for i in range(len(list1)):
                    print(list1[i]["original_title"])
                quit()



