import csv


def generatePlayerStats():
    playerData = {}
    playerStats ={}
    playerWins = {}
    playerCBet ={}
    playerSD = {}
    playerAF = {}
    players = []
    with open('importantpokernow.csv', 'r') as csvfile:
        lines = csvfile.readlines()
        lines.reverse()
        
        for line in lines:
            first = line.split(",")[0]
            if first.startswith('"""'):
                first_quote = first.index('"""')
                second_quote = first.index('""', first_quote + 3)
                player_name = first[first_quote + 3:second_quote]
                if player_name not in players:
                    players.append(player_name)


    for i in players:
        playerData[i] = {"handsPlayed": 0, "PFR": 0, "VPIP": 0, "3BET": 0, "4BET": 0, "5BET": 0, "6BET" :0, "RaiseFaceTotal" :0, "3BetFaceTotal": 0,  "4BetFaceTotal": 0, "5BetFaceTotal": 0, "3BetFold": 0, "4BetFold": 0, "5BetFold" : 0, "CBET%": 0}
        playerStats[i] = { "TOTAL HANDS": 0,"PFR": 0, "VPIP": 0, "3BET%": 0, "FOLD TO 3BET AFTER RAISING%": 0, "FLOP CBET%": 0, "FOLD TO FLOP CBET%": 0, "AF":0, "WTSD": 0, "W$SD":0, "WWSF": 0, "PREFLOP WIN%": 0, "FLOP WIN%" : 0, "TURN WIN%": 0, "RIVER WIN%": 0, "SHOWDOWN WIN%":0, "4BET%": 0, "4BET FOLD%" :0, "5BET%" : 0}
        playerWins[i] = {"PREFLOPWIN": 0, "FLOPWIN" :0 , "TURNWIN" :0, "RIVERWIN":0, "SHOWDOWNWIN" :0, "TOTALWINS":0}
        playerCBet[i] = {"CBETACTUAL": 0, "CBETCHANCES": 0, "CALLCBET": 0, "FOLDCBET" :0}
        playerSD[i] = {"SAWFLOP": 0, "SAWSD": 0, "WONSD" : 0, "WONHAND": 0}
        playerAF[i] = {"BETRAISE" :0, "CALLS":0}



    with open('importantpokernow.csv', 'r') as csvfile:
        totalCount = 0
        lines = csvfile.readlines()
        lines.reverse()
        for line in lines:
            first = line.split(",")[0]
            if first.__contains__("-- ending hand"):
                totalCount = totalCount + 1




    with open('importantpokernow.csv', 'r') as csvfile:
        count = 0
        done = False
        totalCount = 0
        lines = csvfile.readlines()
        lines.reverse()
        
        PFR = False
        for line in lines:
            first = line.split(",")[0] 
            if first.__contains__("-- starting hand"):
                PFR = False
                actualPreFlopRaiser = "NA"
                preflopRaiser = "NA"
                done = False
            elif done == True:
                next
            elif first.__contains__("raise"):
                first_quote = first.index('"""')
                second_quote = first.index('""', first_quote + 3)
                player = first[first_quote + 3:second_quote]
                preflopRaiser = player
            elif first.__contains__("Flop") and preflopRaiser != "NA":
                actualPreFlopRaiser = preflopRaiser
                playerCBet[actualPreFlopRaiser]["CBETCHANCES"] += 1
            elif first.__contains__("bets"):
                first_quote = first.index('"""')
                second_quote = first.index('""', first_quote + 3)
                player = first[first_quote + 3:second_quote]
                count +=1
                if player == actualPreFlopRaiser:
                    playerCBet[actualPreFlopRaiser]["CBETACTUAL"] +=1
                    PFR = True
                done = True
            if PFR == True and (first.__contains__("calls") or first.__contains__("raises")):
                first_quote = first.index('"""')
                second_quote = first.index('""', first_quote + 3)
                player = first[first_quote + 3:second_quote]
                playerCBet[player]["CALLCBET"] +=1
            elif PFR == True and first.__contains__("folds"):
                first_quote = first.index('"""')
                second_quote = first.index('""', first_quote + 3)
                player = first[first_quote + 3:second_quote]
                playerCBet[player]["FOLDCBET"] +=1  
            elif first.__contains__("Turn"):
                PFR = False
                
            
    with open('importantpokernow.csv', 'r') as csvfile:
        lines = csvfile.readlines()
        lines.reverse()
        postFlop = False
        for line in lines:
            first = line.split(",")[0] 
            if first.__contains__("-- starting hand"):
                postFlop = False
            elif first.__contains__("Flop"):
                postFlop = True
            elif postFlop == True and (first.__contains__("raises") or first.__contains__("bets")):
                first_quote = first.index('"""')
                second_quote = first.index('""', first_quote + 3)
                player = first[first_quote + 3:second_quote]
                playerAF[player]["BETRAISE"] +=1
            elif postFlop == True and (first.__contains__("calls")):
                first_quote = first.index('"""')
                second_quote = first.index('""', first_quote + 3)
                player = first[first_quote + 3:second_quote]
        
                playerAF[player]["CALLS"] +=1


    with open('importantpokernow.csv', 'r') as csvfile:
        totalCount = 0
        lines = csvfile.readlines()
        lines.reverse()
        flop = False
        river = False
        sawFlop = set()
        sawRiver = set()
        for (i,line) in enumerate(lines):
            first = line.split(",")[0]
            if first.__contains__("-- starting hand"):
                river = False
                flop = False
                sawRiver = set()
                sawFlop = set()
                showdown = False
            elif first.__contains__("Flop"):
                flop = True
            elif first.__contains__("Turn"):
                flop = False
            elif first.__contains__("Uncalled"):   
                flop = False
            elif flop == True and (first.__contains__("check") or first.__contains__("bets")):
                first_quote = first.index('"""')
                second_quote = first.index('""', first_quote + 3)
                player = first[first_quote + 3:second_quote]
                sawFlop.add(player)
            if first.__contains__("River"):
                river = True
            elif river == True and (first.__contains__("check") or first.__contains__("bets")):
                first_quote = first.index('"""')
                second_quote = first.index('""', first_quote + 3)
                player = first[first_quote + 3:second_quote]
                sawRiver.add(player)
            elif river == True and (first.__contains__("fold")):
                first_quote = first.index('"""')
                second_quote = first.index('""', first_quote + 3)
                player = first[first_quote + 3:second_quote]
                sawRiver.discard(player)
            if river == True and first.__contains__("shows") and lines[i+1].split(",")[0].__contains__("collect"):
                first_quote = lines[i+1].split(",")[0].index('""')
                second_quote = lines[i+1].split(",")[0].index('""', first_quote + 2)
                player = lines[i+1].split(",")[0][first_quote + 3:second_quote]
                showdown = True
                playerSD[player]["WONSD"]+=1
            if first.__contains__("collect"): #Won hand in general, does not have to be showdown
                first_quote = first.index('"""')
                second_quote = first.index('""', first_quote + 3)
                player = first[first_quote + 3:second_quote]
                if player in sawFlop:
                    playerSD[player]["WONHAND"] +=1
            if first.__contains__("-- ending hand"):
                for i in sawFlop: 
                    playerSD[i]["SAWFLOP"] +=1
                for i in sawRiver:
                    playerSD[i]["SAWSD"] +=1
                









    #THis one is just hands played for each player

    with open('importantpokernow.csv', 'r') as csvfile:
        preflop = False
        totalCount = 0
        lines = csvfile.readlines()
        lines.reverse()
        for line in lines:
            first = line.split(",")[0]
            if first.__contains__("-- starting hand"):
                preflop = True
                playersHandChecked = []
            if first.__contains__("Flop"):
                preflop = False
            if preflop == True and first.startswith('""') and "shows" not in first:
                first_quote = first.index('"""')
                second_quote = first.index('""', first_quote + 3)
                player = first[first_quote + 3:second_quote]
                if player not in playersHandChecked:
                    playersHandChecked.append(player)
                    playerData[player]["handsPlayed"] +=1

    #VPIP
    with open('importantpokernow.csv', 'r') as csvfile:
        preflop = False
        totalCount = 0
        lines = csvfile.readlines()
        lines.reverse()
        for line in lines:
            first = line.split(",")[0]
            if first.__contains__("-- starting hand"):
                preflop = True
                playersHandChecked = []
            if first.__contains__("Flop"):
                preflop = False
            if preflop == True and first.startswith('""') and "shows" not in first:
                first_quote = first.index('"""')
                second_quote = first.index('""', first_quote + 3)
                player = first[first_quote + 3:second_quote]
                if player not in playersHandChecked and (first.__contains__("call") or first.__contains__("raise")):
                    playersHandChecked.append(player)
                    playerData[player]["VPIP"] +=1

    #PFR 3 bet 4 bet yadadaa
    with open('importantpokernow.csv', 'r') as csvfile:
        preflop = False
        totalCount = 0
        lines = csvfile.readlines()
        lines.reverse()
        for line in lines:
            first = line.split(",")[0]
            if first.__contains__("-- starting hand"):
                preflop = True
                pfr = "NA"
                playerRaise = 0
            if first.__contains__("Flop"):
                preflop = False
            if preflop == True and first.startswith('""') and "shows" not in first:
                first_quote = first.index('"""')
                second_quote = first.index('""', first_quote + 3)
                player = first[first_quote + 3:second_quote]
                if first.__contains__("raises"):
                    if playerRaise == 0:
                        playerData[player]["PFR"] +=1
                        pfr = player
                        playerRaise = playerRaise + 1
                    elif playerRaise == 1:
                        playerData[player]["RaiseFaceTotal"] +=1
                        playerData[player]["PFR"] +=1
                        playerData[player]["3BET"] +=1
                        playerRaise = playerRaise + 1
                    elif playerRaise == 2:
                        playerData[player]["PFR"] +=1
                        playerData[player]["3BetFaceTotal"] +=1
                        playerData[player]["4BET"] +=1
                        playerRaise = playerRaise + 1
                    elif playerRaise == 3:
                        playerData[player]["PFR"] +=1
                        playerData[player]["4BetFaceTotal"] +=1
                        playerData[player]["5BET"] +=1
                        playerRaise = playerRaise + 1
                    elif playerRaise == 4:
                        playerData[player]["PFR"] +=1
                        playerData[player]["5BetFaceTotal"] +=1
                        playerData[player]["6BET"] +=1
                        playerRaise = playerRaise + 1
                    
                if first.__contains__("fold") and playerRaise == 1:
                    playerData[player]["RaiseFaceTotal"] +=1
                elif first.__contains__("fold") and playerRaise == 2 and player == pfr:
                    playerData[player]["3BetFold"] +=1
                    playerData[player]["3BetFaceTotal"] +=1
                elif first.__contains__("fold") and playerRaise == 3:
                    playerData[player]["4BetFold"] +=1
                    playerData[player]["4BetFaceTotal"] +=1
                elif first.__contains__("fold") and playerRaise == 4:
                    playerData[player]["5BetFold"] +=1
                    playerData[player]["5BetFaceTotal"] +=1

    with open('importantpokernow.csv', 'r') as csvfile:
        hand = "preflop"
        totalCount = 0
        lines = csvfile.readlines()
        lines.reverse()
        for (i,line) in enumerate(lines):
            first = line.split(",")[0]
            if first.__contains__("-- starting hand"):
                hand = "PREFLOPWIN"
            elif first.__contains__("Flop"):
                hand = "FLOPWIN"
            elif first.__contains__("Turn"):
                hand = "TURNWIN"
            elif first.__contains__("River"):
                hand = "RIVERWIN"
            elif first.__contains__("Uncalled"):
                first_quote = first.index('""')
                second_quote = first.index('""', first_quote + 2)
                player = first[first_quote + 2:second_quote]
    
                playerWins[player][hand] +=1
            elif first.__contains__("shows") and hand == "RIVERWIN" and lines[i+1].split(",")[0].__contains__("collect"):
                first_quote = lines[i+1].split(",")[0].index('""')
                second_quote = lines[i+1].split(",")[0].index('""', first_quote + 2)
                player = lines[i+1].split(",")[0][first_quote + 3:second_quote]
            
                playerWins[player]["SHOWDOWNWIN"] +=1
            

        


    for i in playerStats:
        playerStats[i]["TOTAL HANDS"] = playerData[i]["handsPlayed"]
        playerStats[i]["PFR"] = playerData[i]["PFR"] / playerData[i]["handsPlayed"] if playerData[i]["handsPlayed"] != 0 else 0
        playerStats[i]["VPIP"] = playerData[i]["VPIP"] / playerData[i]["handsPlayed"] if playerData[i]["handsPlayed"] != 0 else 0
        playerStats[i]["3BET%"] = playerData[i]["3BET"] / playerData[i]["handsPlayed"] if playerData[i]["RaiseFaceTotal"] != 0 else "NA"
        playerStats[i]["FOLD TO 3BET AFTER RAISING%"] = playerData[i]["3BetFold"] / playerData[i]["3BetFaceTotal"] if playerData[i]["3BetFaceTotal"] != 0 else "NA"
        playerStats[i]["4BET%"] = playerData[i]["4BET"] / playerData[i]["3BetFaceTotal"] if playerData[i]["3BetFaceTotal"] != 0 else "NA"
        playerStats[i]["4BET FOLD%"] = playerData[i]["4BetFold"] / playerData[i]["4BetFaceTotal"] if playerData[i]["4BetFaceTotal"] != 0 else "NA"
        playerStats[i]["5BET%"] = playerData[i]["5BET"] / playerData[i]["4BetFaceTotal"] if playerData[i]["4BetFaceTotal"] != 0 else "NA"
        playerWins[i]["TOTALWINS"] = playerWins[i]["PREFLOPWIN"] + playerWins[i]["FLOPWIN"] + playerWins[i]["TURNWIN"] + playerWins[i]["RIVERWIN"] + playerWins[i]["SHOWDOWNWIN"]
        playerStats[i]["PREFLOP WIN%"] = playerWins[i]["PREFLOPWIN"]/playerWins[i]["TOTALWINS"] if playerWins[i]["TOTALWINS"] != 0 else "NA"
        playerStats[i]["FLOP WIN%"] = playerWins[i]["FLOPWIN"]/playerWins[i]["TOTALWINS"] if playerWins[i]["TOTALWINS"] != 0 else "NA"
        playerStats[i]["TURN WIN%"] = playerWins[i]["TURNWIN"]/playerWins[i]["TOTALWINS"] if playerWins[i]["TOTALWINS"] != 0 else "NA"
        playerStats[i]["RIVER WIN%"] = playerWins[i]["RIVERWIN"]/playerWins[i]["TOTALWINS"] if playerWins[i]["TOTALWINS"] != 0 else "NA"
        playerStats[i]["SHOWDOWN WIN%"] = playerWins[i]["SHOWDOWNWIN"]/playerWins[i]["TOTALWINS"] if playerWins[i]["TOTALWINS"] != 0 else "NA"
        playerStats[i]["FLOP CBET%"] = playerCBet[i]["CBETACTUAL"]/playerCBet[i]["CBETCHANCES"] if playerCBet[i]["CBETCHANCES"] != 0 else "NA"
        totalCBETFACE = playerCBet[i]["CALLCBET"] + playerCBet[i]["FOLDCBET"] 
        playerStats[i]["FOLD TO FLOP CBET%"] = playerCBet[i]["FOLDCBET"]/totalCBETFACE if totalCBETFACE != 0 else "NA"
        playerStats[i]["WTSD"] = playerSD[i]["SAWSD"]/playerSD[i]["SAWFLOP"] if playerSD[i]["SAWFLOP"] != 0 else "NA"
        playerStats[i]["W$SD"] = playerSD[i]["WONSD"] /playerSD[i]["SAWSD"] if playerSD[i]["SAWSD"] != 0 else "NA"
        playerStats[i]["WWSF"] = playerSD[i]["WONHAND"]/playerSD[i]["SAWFLOP"] if playerSD[i]["SAWFLOP"] != 0 else "NA"
        playerStats[i]["AF"] = playerAF[i]["BETRAISE"]/playerAF[i]["CALLS"] if playerAF[i]["CALLS"] != 0 else "NA"
    return playerStats

playerStats = generatePlayerStats()

