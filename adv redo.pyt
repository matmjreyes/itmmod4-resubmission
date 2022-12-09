'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

"""
Sample data for Relationship Status below:
"""

# define the social graph
social_graph = {
    "@voninini": {
        "first_name": "Voni",
        "last_name": "Reyes",
        "following": ["@jeromey", "@tennylo", "@namnamnam"],
    },
    "@jeromey": {
        "first_name": "Jerome",
        "last_name": "Pineda",
        "following": ["voninini", "tennylo"],
    },
    "@namnamnam": {
        "first_name": "Namdo",
        "last_name": "San",
        "following": ["@jeromey", "@voninini", "@aljongs", "@tennylo"],
    },
    "@tennylo": {
        "first_name": "Kirsten",
        "last_name": "Leong",
        "following": [
            "@voninini","@namnamnam","@aljongs",],
    },
    "@aljongs": {
        "first_name": "Alheit",
        "last_name": "Jongski",
        "following": ["@tennylo",],
    },
}

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if to_member in social_graph[from_member]["following"]:
        return "follower"

    # check if to_member follows from_member
    if from_member in social_graph[to_member]["following"]:
        return "followed by"

    # check if from_member and to_member are friends
    if from_member in social_graph[to_member]["following"] and to_member in social_graph[from_member]["following"]:
        return "friends"

    # if none of the above, return "no relationship"
    return "no relationship"


# call the relationship_status() function and store the result
stat = relationship_status("@voninini", "@jeromey", social_graph)

# print the result
print(stat)  # should print "follower"

board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]

def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    for row in board:
        if all(x == row[0] for x in row):
            return row[0]

    for col in range(len(board)):
        if all(board[i][col] == board[0][col] for i in range(len(board))):
            return board[0][col]

    if all(board[i][i] == board[0][0] for i in range(len(board))):
        return board[0][0]
    if all(board[i][len(board) - i - 1] == board[0][len(board) - 1] for i in range(len(board))):
        return board[0][len(board) - 1]

    return "NO WINNER"


my_answer = tic_tac_toe(board7)
print(my_answer)

legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

legs = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    total_time = 0

    # keep track of the current stop
    current_stop = first_stop

    # keep track of the visited stops
    visited_stops = set()
    next_stop = None
    # loop until we reach the second stop
    while current_stop != second_stop:
        # add the current stop to the set of visited stops
        visited_stops.add(current_stop)

        # find the next stop and the travel time to that stop
        for leg in route_map:
            if current_stop in leg and (current_stop, next_stop) not in visited_stops:
                next_stop = leg[0] if leg[1] == current_stop else leg[1]
                travel_time = route_map[leg]["travel time mins"]
                break

        # add the travel time to the total time
        total_time += travel_time

        # update the current stop
        current_stop = next_stop

        # if we have visited all the stops, then we are stuck in a loop
        if len(visited_stops) == len(route_map):
            return -1

    # return the total travel time
    return total_time


# define the route map
route_map = {
    ("upd", "admu"): {"travel time mins": 10},
    ("admu", "dlsu"): {"travel time mins": 35},
    ("dlsu", "upd"): {"travel time mins": 55},
}

# call the eta() function and store the result
travel_time = eta("upd", "admu", route_map)

# print the result
print(travel_time)  # should print 10