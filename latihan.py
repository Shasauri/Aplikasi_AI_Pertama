import streamlit as st

# konfigurasi halaman
st.set_page_config(page_title="projectAI", page_icon=":robot_face:")

# 1. st.title() - judul aplikasi
st.title("Selamat Datang di Aplikasi ProjectAI")
st.markdown("**Ini adalah aplikasi AI pertamaku**")
st.divider()

# 2. st.text_input() - input topik dari user
user_topic = st.text_input("Masukkan topik yang ingin Anda pelajari :")

# code untuk menampilkan topik yang dimasukkan user
if user_topic:
    st.write(f"Topik yang Anda masukkan: {user_topic}")

# 3. st.button() - tombol untuk memulai generate
if st.button("Generate konten"):
    # validasi input user
    if not user_topic.strip():
        st.error("⚠️Mohon masukkan topik terlebih dahulu!")
    else:
        # simulasi hasil ai untuk latihan
        hasil_dari_ai = f"""
        # {user_topic}

        ## Pendahuluan
        Topik "{user_topic}" adalah topik yang akan kita bahas

        ## Poin Utama
        1. **ide pertama** - ini adalah penjelasan ide pertama
        2. **ide kedua** - ini adalah penjelasan ide kedua
        3. **ide ketiga** - Informasi tambahan yang berguna

        ## Kesimpulan

        Demikianlah pembahasan singkat mengenai "{user_topic}". Semoga bermanfaat!

        --------------------------
        ini dibuat oleh ProjectAI
        """
        # 4. st.info() - ini berguna untuk menampilkan hasil dari button
        st.success("✅ Konten berhasil digenerate!")
        st.info(hasil_dari_ai)

# tambahan komponen streamlit
st.divider()
st.markdown("**Komponen stramlit tambahan**")

# contoh komponen/widget yang sering digunakan
col1, col2 = st.columns(2)

with col1:
    st.selectbox("pilih waifu kalian:", ["Rem", "Emilia", "Yukino", "Megumin"])

with col2:
    st.slider("Pilih panjang konten (dalam kata)", 100, 500, 250)

# footer
st.divider()
st.markdown("© 2024 ProjectAI. All rights reserved.")