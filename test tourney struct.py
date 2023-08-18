games = {("Alice", "Bob"), ("Charlie", "Bob"), ("Charlie", "Alice")}

##games = {("Alice", "Bob"), ("Charlie", "Bob"), ("Charlie", "Diana")}
 
from test_project import *
from graphs import *

def gamesOK(games):
    # create the set of all players
    players = set()
    for (a, b) in games:
        players.add(a)
        players.add(b)
    
    # create the graph as a set of directed edges
    edges = {(a, b) for (a, b) in games}
    
    # check if the graph is connected
    return connected(players, edges)

print(gamesOK(games))