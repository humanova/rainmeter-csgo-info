import os
import valve.source.a2s

def getServerInfo(ip):
    SERVER_ADDRESS = (ip, 27015)

    with valve.source.a2s.ServerQuerier(SERVER_ADDRESS, 2.0) as server:
        info = server.info()

        players = []
        players_name = []
        
        for player in server.players()["players"]:
            if player["name"]:
                players.append(player)

        player_count = len(players)

        if not player_count == 0:
            for player in players:
                players_name.append(str(player["name"]))
        else:
            players_name.append("Server Boş ¯\_(ツ)_/¯")

        server_map = info['map']
        max_players = info['max_players']
        server_name = info['server_name']

        player_count_info = str(player_count) + " / " + str(max_players)


    return server_name, server_map, player_count_info, players_name

if __name__ == "__main__":

    shark_ip = "185.193.165.251"
    s_name, s_map, s_player_count, s_players = getServerInfo(shark_ip)

    log_file = open("log.txt", "w+", encoding='utf-8')
    log_file.write(f"{s_name}\n")
    log_file.write(f"Map : {s_map}\n")
    log_file.write(f"Players ({s_player_count}) :\n")
    for p in s_players:
        log_file.write(f"{p}\n")