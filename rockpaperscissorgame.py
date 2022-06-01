from random import choice

playing = True
invalid_value = None


while(playing):
    rand_num =  choice([1,2,3])

    print("""
        .-------------------------.
        |   this is a Rock Paper  |
        |    and Scissors game    |                       |
        '-------------------------'
            
        """)

    player_input = input("please enter R, P or S to play: ")

    def comp():
        cpu_res = None
        if(rand_num == 1):
            cpu_res = "R"
            return cpu_res
        elif(rand_num == 2):
            cpu_res = "P"
            return cpu_res
        elif(rand_num == 3):
            cpu_res = "S"
            return cpu_res

    comp_result = comp()
 
    if(player_input == comp_result):
        print("Player:", player_input, "CPU:", comp_result, "TIE" ) 
    elif(player_input == "R" and comp_result == "S"):
        print("player:", player_input, "CPU:", comp_result, "Winner: Player"  )
    elif(player_input == "S" and comp_result == "R"):
        print("CPU:", comp_result, "Player:", player_input, "Winner: CPU")
    elif(player_input == "P" and comp_result == "S"):
        print("CPU:", comp_result, "Player:", player_input, "Winner: CPU")
    elif(player_input == "S" and comp_result == "P"):
        print("Player:", player_input, "CPU:", comp_result, "Winner: Player")
    elif(player_input == "R" and comp_result == "P"):
        print("CPU:", comp_result, "Player:",  player_input, "Winner: CPU")
    elif(player_input == "P" and comp_result == "R"):
        print("Player:", player_input, "CPU:", comp_result, "Winner: Player")
    elif(player_input != "R"  or player_input != "p" or player_input != "S"):
        invalid_value = True
        print("error invalid value was entered")
        while(invalid_value):
            player_input = input("please enter R, P or S to play: ")
            if(player_input == "R"  or player_input == "p" or player_input == "S"):
                    break

    continue_to_play = input("wuould you like to continue playing enter Y or N:")

    if(continue_to_play == "Y"):
        playing = True
    else:
        playing = False
    

print("thank you for playing")
