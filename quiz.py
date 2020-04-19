class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

def create_players():
    players = []
    num_players = int(input("Please enter the number of players/teams: "))

    i = 0
    while i < num_players:
        name = input("Please enter a name/teamname: ")
        player = Player(name, 0)
        players.append(player)
        i += 1
    
    return players

def update_score(players):
    for player in players:
        score = float(input("Enter score for {}: ".format(player.name)))
        player.score += score
    
    print("\n")
    print_scores(players)

def print_scores(players):
    # Calculating leaderboard after inputting round scores
    leaderboard = []
    for player in players:
        leaderboard.append(player)
    
    for i in range(1, len(leaderboard)):
        current = leaderboard[i]
        j = i-1
        while j>=0 and current.score > leaderboard[j].score:
            leaderboard[j+1] = leaderboard[j]
            j -= 1
        leaderboard[j+1] = current

    # Printing updated leaderboard
    print("Leaderboard:")
    for i in range(0,len(leaderboard)):
        str = "{}. {} - {}".format(i+1,leaderboard[i].name,leaderboard[i].score)
        print(str)
    print("\n")

def new_round(i, rounds, players):
    print("-----------------------------------------")
    print("ROUND {}".format(i))
    update_score(players)


def start_game():
    players = create_players()
    rounds = int(input("Enter number of rounds: "))
    i = 1

    while i < rounds+1:
        new_round(i, rounds, players)
        i+= 1

    print("Quiz finished")
    exit()
        

start_game()

