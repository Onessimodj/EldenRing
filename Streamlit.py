import streamlit as st
import requests
from bs4 import BeautifulSoup

# ---------------- DATA ----------------
NightFarers = {
    '1': 'wylder',
    '2': 'guardian',
    '3': 'ironeye',
    '4': 'duchess',
    '5': 'raider',
    '6': 'revenant',
    '7': 'recluse',
    '8': 'executor',
    '9': 'scholar',
    '10': 'undertaker'
}

NightLords = {
    '1': 'gladius',
    '2': 'adel',
    '3': 'goster',
    '4': 'maris',
    '5': 'libra',
    '6': 'fulghor',
    '7': 'caligo',
    '8': 'heolstor'
}

st.title("⚔️ Elden Ring Nightreign Info Tool")

choice = st.radio("Choose category:", ["Night Farers", "Night Lords"])

# ---------------- NIGHT FARERS ----------------
if choice == "Night Farers":
    selection = st.selectbox(
        "Select a Night Farer",
        [f"{k}. {v}" for k, v in NightFarers.items()]
    )

    if st.button("Get Night Farer Info"):
        key = selection.split(".")[0]
        nightfarer = NightFarers[key]

        st.success(f"Selected: {nightfarer}")

        # ---------------- STATS ----------------
        url = "https://eldenringnightreign.wiki.fextralife.com/Level"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        tables = soup.find_all("table")
        found = False

        for table in tables:
            rows = table.find_all("tr")

            if len(rows) > 1:
                first_row_cols = rows[0].find_all(["td", "th"])

                if len(first_row_cols) > 0:
                    table_name = first_row_cols[0].text.strip().lower()

                    if nightfarer in table_name:
                        found = True

                        for i in range(len(rows)):
                            cols = rows[i].find_all("td")

                            if len(cols) >= 9:
                                level = cols[0].text.strip().lower()

                                if level in ["level 1", "level 15"]:
                                    st.subheader(f"Stats ({cols[0].text.strip()})")
                                    st.write("VIG:", cols[1].text.strip())
                                    st.write("MND:", cols[2].text.strip())
                                    st.write("END:", cols[3].text.strip())
                                    st.write("STR:", cols[4].text.strip())
                                    st.write("DEX:", cols[5].text.strip())
                                    st.write("INT:", cols[6].text.strip())
                                    st.write("FAI:", cols[7].text.strip())
                                    st.write("ARC:", cols[8].text.strip())

                        break

        if not found:
            st.warning("Stats not found.")

        # ---------------- SCALINGS ----------------
        url = "https://eldenringnightreign.wiki.fextralife.com/Nightfarers+(Classes)"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        rows = soup.find_all("tr")
        found = False

        for row in rows:
            cols = row.find_all("td")

            if len(cols) >= 9:
                name = cols[0].text.strip().lower()

                if nightfarer in name:
                    found = True

                    st.subheader("Scalings")
                    st.write("VIG:", cols[1].text.strip())
                    st.write("MND:", cols[2].text.strip())
                    st.write("END:", cols[3].text.strip())
                    st.write("STR:", cols[4].text.strip())
                    st.write("DEX:", cols[5].text.strip())
                    st.write("INT:", cols[6].text.strip())
                    st.write("FAI:", cols[7].text.strip())
                    st.write("ARC:", cols[8].text.strip())

                    break

        if not found:
            st.warning("Scalings not found.")

# ---------------- NIGHT LORDS ----------------
if choice == "Night Lords":
    selection = st.selectbox(
        "Select a Night Lord",
        [f"{k}. {v}" for k, v in NightLords.items()]
    )

    if st.button("Get Night Lord Info"):
        key = selection.split(".")[0]
        nightlord = NightLords[key]

        st.success(f"Selected: {nightlord}")

        url = "https://eldenringnightreign.wiki.fextralife.com/Bosses"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        rows = soup.find_all("tr")
        found = False

        for row in rows:
            cols = row.find_all("td")

            if len(cols) >= 16:
                name = cols[0].text.strip().lower()

                if nightlord in name:
                    found = True

                    st.subheader("Boss Stats")
                    st.write("Name:", cols[0].text.strip())
                    st.write("Standard:", cols[2].text.strip())
                    st.write("Slash:", cols[3].text.strip())
                    st.write("Strike:", cols[4].text.strip())
                    st.write("Pierce:", cols[5].text.strip())
                    st.write("Magic:", cols[6].text.strip())
                    st.write("Fire:", cols[7].text.strip())
                    st.write("Lightning:", cols[8].text.strip())
                    st.write("Holy:", cols[9].text.strip())
                    st.write("Poison:", cols[10].text.strip())
                    st.write("Rot:", cols[11].text.strip())
                    st.write("Bleed:", cols[12].text.strip())
                    st.write("Frostbite:", cols[13].text.strip())
                    st.write("Sleep:", cols[14].text.strip())
                    st.write("Madness:", cols[15].text.strip())

        if not found:
            st.warning("Boss not found.")