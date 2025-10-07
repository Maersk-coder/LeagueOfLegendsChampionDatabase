import streamlit as st
import pandas as pd
import numpy as np
import os

# Load data from CSV
csvData = pd.read_csv("LeagueOfLegends/champions.csv")
Champion = csvData['Champion Name'].to_numpy()
Role = csvData['Role'].to_numpy()
Health = csvData['Base Health'].to_numpy()
Mana = csvData['Base Mana'].to_numpy()
Armor = csvData['Base Armor'].to_numpy()
Damage = csvData['Base Attack Damage'].to_numpy()
Gold = csvData['Gold Efficiency'].to_numpy()

# Function to search for champions based on role and stat
def search_champions(role, stat, max_or_min):
    role_indices = np.where(Role == role)[0]
    if len(role_indices) == 0:
        return []

    if stat == "Health":
        stat_array = Health
    elif stat == "Mana":
        stat_array = Mana
    elif stat == "Armor":
        stat_array = Armor
    elif stat == "Damage":
        stat_array = Damage
    elif stat == "Gold":
        stat_array = Gold
    else:
        return []

    if max_or_min == "Max":
        sorted_indices = role_indices[np.argsort(stat_array[role_indices])[::-1]]
    elif max_or_min == "Min":
        sorted_indices = role_indices[np.argsort(stat_array[role_indices])]
    else:
        return []

    return sorted_indices

# Streamlit UI
st.title("Champion Stats Search")

role = st.selectbox("Select Role", ["Top", "Jungle", "Mid", "ADC", "Support"])
stat = st.selectbox("Select Stat", ["Health", "Mana", "Armor", "Damage", "Gold"])
max_or_min = st.selectbox("Max or Min", ["Max", "Min"])

if st.button("Search"):
    indices = search_champions(role, stat, max_or_min)
    if len(indices) == 0:
        st.write("No champions found for the selected criteria.")
    else:
        for i in indices:
            st.write(f"Champion: {Champion[i]}")
            image_path = os.path.join("LeagueOfLegends", "lol_images", f"{Champion[i]}.jpg")
            st.write(f"Image path: {image_path}")  # Debugging line to show the image path
            if os.path.exists(image_path):
                st.image(image_path, caption=Champion[i], use_column_width=True)
            else:
                st.write("Image not found")
            st.write(f"Health: {Health[i]}")
            st.write(f"Mana: {Mana[i]}")
            st.write(f"Armor: {Armor[i]}")
            st.write(f"Damage: {Damage[i]}")
            st.write(f"Gold: {Gold[i]}")
            st.write("\n")
            