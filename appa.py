import streamlit as st
import random
import time
import requests
import urllib.parse
from datetime import datetime
from streamlit_lottie import st_lottie

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="NASYA GAME v2 🔮",
    page_icon="🔮",
    layout="centered"
)

# =========================
# SESSION STATE
# =========================
if "xp" not in st.session_state:
    st.session_state.xp = 0

if "level" not in st.session_state:
    st.session_state.level = 1

if "inventory" not in st.session_state:
    st.session_state.inventory = []

if "history" not in st.session_state:
    st.session_state.history = []

# =========================
# STYLE
# =========================
st.markdown("""
<style>
.result-card {
    background:#161b22;
    padding:20px;
    border-radius:15px;
    text-align:center;
    margin-top:15px;
    border:1px solid #30363d;
}
.stButton>button {
    width:100%;
    border-radius:20px;
    background:linear-gradient(45deg,#6a00ff,#00ffd5);
    color:white;
    font-weight:bold;
}
.share-btn {
    display:inline-block;
    margin-top:10px;
    background:#25D366;
    color:white;
    padding:10px;
    border-radius:10px;
    text-decoration:none;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HELPERS
# =========================
def load_lottie(url):
    try:
        r = requests.get(url, timeout=5)
        return r.json() if r.status_code == 200 else None
    except:
        return None

def add_xp(amount):
    st.session_state.xp += amount
    st.session_state.level = int(st.session_state.xp ** 0.5) + 1

def get_rarity():
    roll = random.randint(1, 100)
    if roll <= 60:
        return "Common"
    elif roll <= 85:
        return "Rare"
    elif roll <= 97:
        return "Epic"
    else:
        return "Legendary"

def save_history(mode, result, rarity):
    st.session_state.history.append({
        "time": datetime.now().strftime("%H:%M:%S"),
        "mode": mode,
        "result": result,
        "rarity": rarity
    })

def wa_share(text):
    url = "https://wa.me/?text=" + urllib.parse.quote(text)
    st.markdown(
        f'<a class="share-btn" href="{url}" target="_blank">📲 Share Result</a>',
        unsafe_allow_html=True
    )

# =========================
# KHODAM GACHA ENGINE
# =========================
def pull_khodam():
    common = ["Kucing Oren", "Sandal Jepit", "Tutup Panci"]
    rare = ["Macan Mewing", "Garuda Santai"]
    epic = ["Naga Hitam TikTok"]
    legendary = ["Ratu Dimensi Gaib"]

    rarity = get_rarity()

    if rarity == "Common":
        result = random.choice(common)
        xp = 10
    elif rarity == "Rare":
        result = random.choice(rare)
        xp = 20
    elif rarity == "Epic":
        result = random.choice(epic)
        xp = 35
    else:
        result = random.choice(legendary)
        xp = 60

    return result, rarity, xp

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.title("🔮 NASYA GAME")

    st.metric("Level", st.session_state.level)
    st.metric("XP", st.session_state.xp)
    st.metric("Inventory", len(st.session_state.inventory))

    menu = st.radio("Menu", [
        "🏠 Home",
        "🎰 Khodam Gacha",
        "📦 Inventory",
        "📜 History"
    ])

# =========================
# HOME
# =========================
if menu == "🏠 Home":
    st.title("NASYA GAME v2 🔮")
    st.subheader("RPG Gacha Oracle System")

    st.info("Mainkan gacha, kumpulkan khodam, dan naik level!")

# =========================
# GACHA
# =========================
elif menu == "🎰 Khodam Gacha":
    st.header("🎰 Summon Khodam")

    if st.button("Panggil Entitas Gaib"):

        result, rarity, xp = pull_khodam()

        add_xp(xp)
        save_history("khodam", result, rarity)
        st.session_state.inventory.append(result)

        st.balloons()

        st.markdown(f"""
        <div class="result-card">
            <h3>Hasil Summon</h3>
            <h1>{result}</h1>
            <h3>🔥 {rarity}</h3>
            <p>+{xp} XP</p>
            <p>Level: {st.session_state.level}</p>
        </div>
        """, unsafe_allow_html=True)

        wa_share(f"🔥 Gue dapet {result} ({rarity}) di NASYA GAME v2! Level {st.session_state.level}")

# =========================
# INVENTORY
# =========================
elif menu == "📦 Inventory":
    st.header("📦 Koleksi Khodam")

    if not st.session_state.inventory:
        st.warning("Belum punya khodam. Main dulu gacha!")
    else:
        for i, item in enumerate(st.session_state.inventory, 1):
            st.write(f"{i}. {item}")

# =========================
# HISTORY
# =========================
elif menu == "📜 History":
    st.header("📜 Riwayat Game")

    if not st.session_state.history:
        st.info("Belum ada history")
    else:
        for h in reversed(st.session_state.history[-10:]):
            st.write(f"{h['time']} | {h['mode']} → {h['result']} ({h['rarity']})")
