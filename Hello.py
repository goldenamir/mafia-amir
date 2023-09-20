import streamlit as st
import random

import streamlit as st
import random

def main():
    st.title("Mafia Game")

    mafia_count = st.number_input("Number of Mafia", min_value=0, value=0)
    citizen_count = st.number_input("Number of Citizens", min_value=0, value=0)
    independent_count = st.number_input("Number of Independent Players", min_value=0, value=0)

    total_players = mafia_count + citizen_count + independent_count

    character_names = []
    for i in range(total_players):
        character = st.text_input(f"Enter the character name for Player {i + 1}", f"Character {i + 1}")
        character_names.append(character)

    player_names = []
    for i in range(total_players):
        name = st.text_input(f"Enter the name of Player {i + 1}", f"Player {i + 1}")
        player_names.append(name)

    if len(character_names) == total_players:  # Check if the number of character names matches total players
        if st.button("Assign Characters"):
            st.write(f"Total Players: {total_players}")

            # Shuffle the character names
            shuffled_characters = character_names.copy()
            random.shuffle(shuffled_characters)

            # Create a dictionary to assign characters to players
            player_characters = {}
            for i in range(total_players):
                player_characters[player_names[i]] = shuffled_characters[i]

            # Display assigned characters as a table
            character_data = {"Player": list(player_characters.keys()), "Character": list(player_characters.values())}
            character_table = st.table(character_data)
    else:
        st.write("Please enter the same number of character names as the total number of players.")

if __name__ == "__main__":
    main()
