# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import random

def main():
    st.title("Mafia Game by Amir Vahed")

    mafia_count = st.number_input("Number of Mafia", min_value=0, value=0)
    citizen_count = st.number_input("Number of Citizens", min_value=0, value=0)
    independent_count = st.number_input("Number of Independent Players", min_value=0, value=0)

    total_players = mafia_count + citizen_count + independent_count

    player_names = []
    for i in range(total_players):
        name = st.text_input(f"Enter the name of Player {i + 1}", f"Player {i + 1}")
        player_names.append(name)

    if st.button("Shuffle and Show Names"):
        st.write(f"Total Players: {total_players}")
        st.write("Shuffled Player Names:")

        # Shuffle the player names
        random.shuffle(player_names)

        # Display names one by one
        for i, name in enumerate(player_names):
            st.write(f"Player {i + 1}: {name}")

if __name__ == "__main__":
    main()
