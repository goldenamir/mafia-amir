import streamlit as st
import random

def main():
    st.title("Mafia Game")

    mafia_count = st.number_input("Number of Mafia", min_value=0, value=0)
    citizen_count = st.number_input("Number of Citizens", min_value=0, value=0)
    independent_count = st.number_input("Number of Independent Players", min_value=0, value=0)

    total_players = mafia_count + citizen_count + independent_count

    player_names = []
    for i in range(total_players):
        name = st.text_input(f"Enter the name of Player {i + 1}", f"Player {i + 1}")
        player_names.append(name)

    if st.button("Assign Characters"):
        st.write(f"Total Players: {total_players}")
        st.write("Assigned Characters:")

        # Shuffle the player names
        random.shuffle(player_names)

        # Create a dictionary to assign characters to players
        player_characters = {}
        for i, player_name in enumerate(player_names):
            character = st.text_input(f"Enter the character name for {player_name}", f"Character {i + 1}")
            player_characters[player_name] = character

        # Display assigned characters as a table
        character_data = {"Player": list(player_characters.keys()), "Character": list(player_characters.values())}
        character_table = st.table(character_data)

if __name__ == "__main__":
    main()
