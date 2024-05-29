# Breadth-first search_Social_Network_And_Graph
Consider a social network with many users, and a user can follow many other users. We can use a graph to represent the relationship among users. Each node in the graph represents a user. A directed edge  A→B  means user A follows user B. The graph can be represented by user and follow that are global variables implemented using Python dictionary (You can also use another way to implement the graph.)

user={}
follow={}

user is a global variable with key as user ID (an int), value as name of the user (a string). 
follow is a global variable with key as user ID (an int), value as a list of other user ID(s) that the user follows. 
We would like to implement a program ig.py that supports six commands, namely  AddUser, AddFollow, CommonFollow, ListFollower, Recommend and ShortestPath.
