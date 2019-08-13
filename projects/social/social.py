import random
import math
from util import Queue
from graph import Graph


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def __repr__(self):
        return f"Friendships: {self.friendships}"

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # TODO:

        # Add users
        for i in range(0, numUsers):
            self.addUser(f"Brian{i}")

        # Create Friendships
        possibleFriendships = []
        for userID in self.users:
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append(
                    (userID, friendID))  # appending a tuple of current user and all possible friends being users after them in list (userID + 1)

        # changes the position of items in a list
        random.shuffle(possibleFriendships)
        # random.sample(possibleFriendships, (numUsers * avgFriendships) // 2)

        for i in range(0, math.floor(numUsers * avgFriendships / 2)):
            # remember possibleFriendships is a list of tuples of friends [(val1, val2), (val1, val2), (val1, val2)]
            friendship = possibleFriendships[i]
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        # TODO: !!!! IMPLEMENT ME

        if not self.friendships[userID]:
            return "User has no friends"

        # use bft from Graph
        # g = Graph()
        # g.vertices = self.friendships

        visited = {}  # Note that this is a dictionary, not a set

        q = Queue()
        path = [userID]
        q.enqueue(path)
        while q.size() > 0:
            # print("Current Queue: ", q.queue)
            path = q.dequeue()  # remove/return next path block in line

            # Get last item in path block
            # This is the end friend
            # The path block holds the connections bw the starting user (userID) to this end friend
            # Path format ex:
            # [start, end] or
            # [start, next,... next, end]
            # So we want to add the end item/friend as a key in dictionary, with the full path block/array as the value
            # in dict: for user to get to this item/friend/key: the path of user's friends
            v = path[-1]

            if v not in visited:

                if v is not userID:  # starting user doesn't need to be in dictionary
                    visited[v] = path

                for friend in self.friendships[v]:
                    new_path = list(path)  # or = path[:]
                    new_path.append(friend)  # adding friend to path
                    # adds path as a block [friend, friend, friend], so queue is a list of lists
                    q.enqueue(new_path)

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(10, 2)
    print("Friendships: ", sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print("Connections: ", connections)

""" In Command Line: 
$ cd into social folder
$ python3
>>> from social import *
>>> sg = SocialGraph()
>>> sg.populateGraph(10, 2)
>>> print(sg.friendships)
>>> print(sg.getAllSocialPaths(1))
"""

