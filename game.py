import time

# Set the length of the track
track_length = 20  
# Initialize the player's position
player_position = 0  
# Initialize the NPC's position
npc_position = 0  
# Set a fixed speed for the NPC
npc_speed = 3  

print("Welcome to the Simple Racing Game!")

# Start the game loop
while player_position < track_length and npc_position < track_length:
    # Ask the player to choose their acceleration speed
    action = input("Do you want to accelerate? (y/n): ")
    
    if action.lower() == 'y':
        # Ask the player to enter their speed (1 to 5)
        player_speed = int(input("Enter your speed (1-5): "))
        
        # Validate the input speed
        if player_speed < 1 or player_speed > 5:
            print("Invalid speed! Please enter a number between 1 and 5.")
            continue  # Skip the rest of the loop and ask again
        
        # Update the player's position
        player_position += player_speed  
        print("You accelerate to position", player_position)
    else:
        print("You chose not to accelerate.")

    # Move the NPC
    npc_position += npc_speed  # NPC moves at a fixed speed
    print("The NPC moves to position", npc_position)

    # Pause for a moment to simulate time passing
    time.sleep(1)  

    # Check if the player or NPC has reached the finish line
    if player_position >= track_length and npc_position >= track_length:
        print("It's a tie!")
        break
    elif player_position >= track_length:
        print("Congratulations! You reached the finish line first!")
        break
    elif npc_position >= track_length:
        print("The NPC reached the finish line first! Better luck next time.")
        break

    # Show the current positions
    print("Current Positions: Player:", player_position, "NPC:", npc_position)

# End of the game
print("Thanks for playing!")
