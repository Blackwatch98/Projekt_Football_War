import socket
from _thread import *
from Game import Game
import pickle

currentPlayer = 0
number = 0
server = "10.128.158.4"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connected = set()

try:
    s.bind((server,port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for connection - the Server has started...")

MAX_POINTS = 3
ROUNDS = 0
games={}
idCount = 0

def threaded_client(conn,player,gameId):
    conn.sendall(str.encode(str(player)))
    global idCount
    reply = ""
    while True:
        try:
            data = conn.recv(4096).decode()
            #reply = data.decode("utf-8")
            if gameId in games:
                game = games[gameId]

                if not data:
                    print("Disconnected")
                    break
                else:
                    if data == "next_round":
                        game.nextRoundWent()
                    elif data == "raise":
                        print("WYNIKI: ", game.points)
                        if player == 1:
                            game.points[0] += 1
                        else:
                            game.points[1] += 1
                    elif data != "get":
                        print("dostalem ",data)
                        print(game.play(player, data))

                    if game.points[0] == MAX_POINTS or game.points[1] == MAX_POINTS or ROUNDS == 7:
                        game.end = True


                    conn.sendall(pickle.dumps(game))
            else:
                break
        except:
            break

    print("Lost connection")
    try:
        del games[gameId]
        print("Closing Game", gameId)
    except:
        pass
    idCount -= 1
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    idCount += 1
    p = 1
    gameId = (idCount - 1) // 2
    if idCount % 2 == 1:
        games[gameId] = Game(gameId)
        print("Creating a new game...")
    else:
        games[gameId].ready = True
        p = 2

    start_new_thread(threaded_client, (conn, p,gameId))