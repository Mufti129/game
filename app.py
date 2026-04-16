import streamlit as st
import random
import time
import requests
import urllib.parse
from streamlit_lottie import st_lottie

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Oracle Pro: Ramalan & Khodam", page_icon="🔮", layout="centered")

# --- CUSTOM CSS (Bikin tampilan kayak aplikasi premium) ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        background: linear-gradient(45deg, #6200ea, #03dac6);
        color: white; font-weight: bold; border: none; height: 3em; transition: 0.3s;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 10px 20px rgba(0,0,0,0.4); }
    .result-card {
        background: #161b22; padding: 25px; border-radius: 20px;
        border: 1px solid #30363d; text-align: center; margin-top: 20px;
    }
    .share-btn {
        background-color: #25D366; color: white; padding: 10px 20px;
        border-radius: 10px; text-decoration: none; display: inline-block; font-size: 14px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- FUNGSI HELPER ---
def load_lottie(url):
    r = requests.get(url)
    return r.json() if r.status_code == 200 else None

def wa_share(pesan):
    url = f"https://wa.me{urllib.parse.quote(pesan)}"
    st.markdown(f'<a href="{url}" target="_blank" class="share-btn">📲 Share Hasil ke WhatsApp</a>', unsafe_allow_html=True)

# --- LOAD ASSETS ---
lottie_main = load_lottie("https://lottiefiles.com")

# --- SIDEBAR ---
with st.sidebar:
    st.title("🌌 Menu Oracle")
    menu = st.radio("Pilih Ramalan:", ["Beranda", "Cek Khodam Pro", "Love Compatibility", "Job Future"])
    st.markdown("---")
    st.write("Developed by [Nama Kamu]")

# --- LOGIKA GAME ---

if menu == "Beranda":
    st.title("🔮 Oracle Advanced")
    st.subheader("Temukan rahasia masa depanmu dengan teknologi AI Gaib.")
    st_lottie(lottie_main, height=300)
    st.info("Pilih salah satu menu di samping untuk memulai petualanganmu!")

elif menu == "Cek Khodam Pro":
    st.header("🐯 Ritual Cek Khodam")
    nama = st.text_input("Siapa nama lengkapmu?", placeholder="Contoh: Budi Santoso")
    
    if st.button("Panggil Entitas"):
        if nama:
            with st.status("Membuka Gerbang Gaib...", expanded=True) as s:
                time.sleep(1); st.write("Membaca garis tangan..."); 
                time.sleep(1); st.write("Mendeteksi energi sekitar...");
                s.update(label="Ritual Selesai!", state="complete")
            
            khodams = ["Macan Mewing", "Naga Hitam TikTok", "Kucing Oren Racing", "Garuda Pancasila", "Tutup Panci Sakti", "Sandal Jepit Putus"]
            hasil = random.choice(khodams)
            img_id = random.randint(1, 1000)
            
            st.markdown(f"""<div class='result-card'>
                <h3>Khodam {nama} adalah:</h3>
                <h1 style='color: #03dac6;'>{hasil}</h1>
                </div>""", unsafe_allow_html=True)
            
            # Gambar khodam dinamis
            st.image(f"https://robohash.org{nama}?set=set2", width=250, caption="Visualisasi Aura Khodam")
            
            wa_share(f"Gila! Aku baru cek khodam di Oracle App. Khodamku ternyata: {hasil}! Cek punyamu di sini: [Link-Web-Kamu]")
        else:
            st.warning("Namanya diisi dulu bosku!")

elif menu == "Love Compatibility":
    st.header("❤️ Love Meter v2.0")
    col1, col2 = st.columns(2)
    n1 = col1.text_input("Nama Kamu")
    n2 = col2.text_input("Nama Dia")
    
    if st.button("Hitung Kecocokan"):
        if n1 and n2:
            bar = st.progress(0)
            for i in range(100):
                time.sleep(0.02); bar.progress(i + 1)
            
            skor = random.randint(1, 100)
            st.balloons()
            
            color = "#ff4b4b" if skor > 70 else "#f1c40f"
            st.markdown(f"<div class='result-card'><h2 style='color:{color}'>{skor}% MATCH!</h2></div>", unsafe_allow_html=True)
            
            if skor > 80: st.success("Kalian adalah definisi jodoh sebenarnya! 🔥")
            else: st.info("Tetaplah berjuang, cinta butuh usaha! ☕")
            
            wa_share(f"Cek kecocokan aku sama {n2} hasilnya {skor}%! Berani coba?")
        else:
            st.warning("Isi kedua nama!")

elif menu == "Job Future":
    st.header("💼 Karir Masa Depan")
    nama_j = st.text_input("Siapa namamu?")
    
    if st.button("Lihat Karir 2030"):
        if nama_j:
            jobs = ["CEO Startup Kopi Gula Aren", "Pawang Hujan Digital", "Astronot TikTok", "Sultan Jalur Langit", "Duta Rebahan Indonesia"]
            hasil_j = random.choice(jobs)
            st.snow()
            st.markdown(f"<div class='result-card'><h3>{nama_j}, di masa depan kamu akan menjadi:</h3><h2 style='color:#bb86fc;'>{hasil_j}</h2></div>", unsafe_allow_html=True)
            wa_share(f"Masa depanku sudah diramal! Katanya aku bakal jadi {hasil_j}. Cek punyamu!")
