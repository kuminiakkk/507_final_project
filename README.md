# 507_final_project

Run the final_project.py program can help you screen movies.
After the users run the program, the program will ask them “Do you want to search movies?”, if the users want to quit the program, they can type “exit”, and then the program will quit; else, this program will give users four choices to choose, and the four choices will be shown on the screen “This program has four methods to screen 1: by average voting scores 2: by popularity 3: by release date 4: by title”. Then, the program will show to users “please input a number from 1-4, to show which one you want to use for screening; if you want to get the result, please enter result; if you want to quit, please enter quit”. Therefore, users will have 6 selections, “1-4” can give them the methods to screen movies, “result” will show them the result of movies they get, “quit” will quit the program as well as show the results of movies they get. If users choose “1”, the program will ask them for the low and high average vote score they want, and then get the movies in the range. If users choose “2”, the program will ask them for the low and high popularity they want, and then get the movies in the range. If users choose “3”, the program will ask them for the further and recent release date they want, and then get the movies in the range. If users choose “4”, the program will ask them for the text they want in the movie title, and then get the movies containing the text.


The cache.json file is about the result of caching.

The tree.py file can help build the three initial trees and convert them into json files, they are separately tree_Voting.json, tree_Popularity.json and tree_Release_date.json. Users can use read_json.py to read those three tree json files. However, those files won’t work in my program, they just fulfill the requirement:
1.	A python file that constructs your graphs or trees from your stored data using classes
2.	JSON file with your graphs or trees
3.	A stand alone python file that reads the json of your graphs or trees.

Why I don’t need to use those three original trees? The reason is that the program is a bit of complex, every time after the users choose a method to search movies, the program needs to build a new tree to help users search based on their previous search results. In detail, I have three different variables for users to select, “vote scores”, “popularity”, “release date” and “title”. For the title part, I just use regex to help search; for the others, I need to build a tree and use the function I construct when I build this tree to help search. Therefore, each time users choose a method to search, the program will need to build a new tree based on the result they get from previous search. 

Enjoy my program!
Thank you!
