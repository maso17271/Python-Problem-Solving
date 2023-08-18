import graphs
import digraphs
## Q1 
def gamesOK(games):
    V = set()
    E = set()
    #Making the graph
    for (a, b) in games:
        V.add(a)
        V.add(b)
        E.add((a, b))
        E.add((b, a)) ##GPT appoach to symmetrical edges
    
    # see if distance is less than 2
    for a in V:
        for b in V:
            if a != b and graphs.distance(V, E, a, b) > 2: ## utilising distance calc from CAB203 graphs.py
                return False

    return True

## Q2

import csv
def potentialReferees(refereecsvfilename, player1, player2):
    referees = set()
    
    with open(refereecsvfilename, 'r') as ref_file: ## modified approach from CAB203 9.2 case study
        reader = csv.reader(ref_file)
        header = next(reader)
        
        for row in reader:
            referee = row[0]
            conflicts = set(row[1:])
            
            # Check if the referee has conflicts of interest with the players
            if player1 in conflicts or player2 in conflicts or referee in [player1, player2]:
                continue
            
            referees.add(referee)
            
    return referees

##Q3 

def gameReferees(gamePotentialReferees):
    players = set()
    refs = set()
    edges = set()
    for player, referees in gamePotentialReferees.items():
        players.add(player)
        for referee in referees:
            refs.add(referee)
            edges.add((player, referee))
    if len(refs) < len(players):
        return None
    else:
        matching = digraphs.maxMatching(players,refs,edges)
        results = {k: v for k, v in matching if k in players} #Used GPT to only parse results where keyvalues appeared first.
        return results

## Q4

def gameSchedule(assignedReferees):
    # Extract vertices into a tuple format
    V = [(items[0][0], items[0][1], items[1]) for items in assignedReferees.items()]
    ## utilise the approach from CAB 203 lecture 9
    E = {(u,v) for u in V for v in V if u != v and set(u).intersection(set(v)) != set()} 

    # Find the chromatic number and coloring of the graph
    k, colouring = graphs.minColouring(V, E)

    # # # Create a schedule based on the coloring
    schedule = [set() for games in range(k)] ## Geeks for geeks on sets
    for match, timeslot in colouring.items():
        schedule[timeslot].add(match)
    return schedule

## Q5
def ranking ( games ):
    V = set()
    E = (games)
    for winner,loser in games: ## similar apporach to q1
        V.add(winner)
        V.add(loser)
    ordering = digraphs.topOrdering(V,E)
    return ordering








