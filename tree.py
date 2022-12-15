# This file can help you build the orginal tree I use for the project
# Please note this file should be processed after you get the cache file in the final_project.py program
import json
from datetime import datetime
import sys

# I use this for more recursion
sys.setrecursionlimit(100000)

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

# Get the tree 
new_list_node = Node(list1[0])
for i in range(1, len(list1)):
    new_list_node.insert(list1[i])

new_list_node1 = Node1(list1[0])
for i in range(1, len(list1)):
    new_list_node1.insert(list1[i])

new_list_node2 = Node2(list1[0])
for i in range(1, len(list1)):
    new_list_node2.insert(list1[i])



# Define a function for constructing a list
def printTree(node,listn):
    if node != None:
        printTree(node.left,listn)
        listn.append(node.data)
        printTree(node.right,listn)



# Get the json file for average voting score tree
list_voting = []

printTree(new_list_node,list_voting)

tree_Voting = "tree_Voting.json"
dumped_json_tree_voting = json.dumps(list_voting,indent=4, sort_keys=True, default=str)
fw = open(tree_Voting,"w")
fw.write(dumped_json_tree_voting)



# Get the json file for popularity tree
list_popularity = []

printTree(new_list_node1,list_popularity)

tree_Popularity= "tree_Popularity.json"
dumped_json_tree_popularity = json.dumps(list_popularity,indent=4, sort_keys=True, default=str)
fw = open(tree_Popularity,"w")
fw.write(dumped_json_tree_popularity)



# Get the json file for release_date tree
list_release_date = []

printTree(new_list_node2,list_release_date)

tree_Release_date= "tree_Release_date.json"
dumped_json_tree_release_date = json.dumps(list_release_date,indent=4, sort_keys=True, default=str)
fw = open(tree_Release_date,"w")
fw.write(dumped_json_tree_release_date)



