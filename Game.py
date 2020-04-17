
class Game:
    def __init__(self,id):
        self.ready = False
        self.p1Went = False
        self.p2Went = False
        self.id = id
        self.played_cards = [None,None]
        self.points = [0,0]
        self.end = False

    def get_played_cards(self):
        return self.played_cards

    def get_points(self):
        return self.points

    def connected(self):
        return self.ready

    def bothWent(self):
        return self.p1Went and self.p2Went
        '''
    def round_winner(self, cards, playerNumber):
        id1 = int(self.played_cards[0])
        id2 = int(self.played_cards[1])

        card1 = None
        card2 = None

        print("id1 " + str(id1) + " id2 " + str(id2))
        for card in cards:
            print("SZUKAM "+str(id1)+","+str(id2)+" MAM ", card.id)
            if card.id == id1:
                card1 = card
            if card.id == id2:
                card2 = card

        print("cdid1 " + str(card1.id) + " cdid2 " + str(card2.id))

        winner = -1

        if card1.power > card2.power:
            winner = 1

        elif card1.power < card2.power:
            winner = 2
            
        return winner
    '''
    def round_winner(self, cards, playerNumber):
        # zasady do wygrania rundy
        id1 = int(self.played_cards[0])
        id2 = int(self.played_cards[1])

        card1 = None
        card2 = None

        print("id1 " + str(id1) + " id2 " + str(id2))
        for card in cards:
            print("SZUKAM " + str(id1) + "," + str(id2) + " MAM ", card.id)
            if card.id == id1:
                card1 = card
            if card.id == id2:
                card2 = card

        print("cdid1 " + str(card1.id) + " cdid2 " + str(card2.id))

        winner = -1

        if (card1.Atk > card1.Def):
            card1.Atk *= (1 + ((card1.For / 100) * 0.5))

        if (card1.Atk < card1.Def):
            card1.Def *= (1 + ((card1.For / 100) * 0.5))

        if (card2.Atk > card2.Def):
            card2.Atk *= (1 + ((card2.For / 100) * 0.5))

        if (card2.Atk < card2.Def):
            card2.Def *= (1 + ((card2.For / 100) * 0.5))

        player1_pkt = (int(card1.Atk) + card1.Sil + card1.Dos + card1.Dry + int(card1.Def)) * card1.For / 100;
        player2_pkt = (int(card2.Atk) + card2.Sil + card2.Dos + card2.Dry + int(card2.Def)) * card2.For / 100;
        print("Punkty graczy " + str(player1_pkt) + " " + str(player2_pkt))
        if player1_pkt > player2_pkt:
            winner = 1
            self.points[0] += 1;
        elif player1_pkt < player2_pkt:
            self.points[1] += 1;
            winner = 2

        # for card in cards:
        #    print("Karta: ",card.id)

        return winner

    def play(self, player, card_id):
        self.played_cards[player-1] = card_id
        if player == 1:
            self.p1Went = True
        else:
            self.p2Went = True

        return player

    def nextRoundWent(self):
        self.p1Went = False
        self.p2Went = False