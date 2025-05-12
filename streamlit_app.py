import streamlit as st
import re

# Massa atom lengkap
massa_atom = {
    "H": 1.008, "He": 4.0026, "Li": 6.94, "Be": 9.0122, "B": 10.81, "C": 12.01,
    "N": 14.007, "O": 16.00, "F": 18.998, "Ne": 20.180, "Na": 22.990, "Mg": 24.305,
    "Al": 26.982, "Si": 28.085, "P": 30.974, "S": 32.06, "Cl": 35.45, "Ar": 39.948,
    "K": 39.098, "Ca": 40.078, "Sc": 44.956, "Ti": 47.867, "V": 50.942, "Cr": 51.996,
    "Mn": 54.938, "Fe": 55.845, "Co": 58.933, "Ni": 58.693, "Cu": 63.546, "Zn": 65.38,
    "Ga": 69.723, "Ge": 72.63, "As": 74.922, "Se": 78.971, "Br": 79.904, "Kr": 83.798,
    "Rb": 85.468, "Sr": 87.62, "Y": 88.906, "Zr": 91.224, "Nb": 92.906, "Mo": 95.95,
    "Tc": 98, "Ru": 101.07, "Rh": 102.91, "Pd": 106.42, "Ag": 107.87, "Cd": 112.41,
    "In": 114.82, "Sn": 118.71, "Sb": 121.76, "Te": 127.60, "I": 126.90, "Xe": 131.29,
    "Cs": 132.91, "Ba": 137.33, "La": 138.91, "Ce": 140.12, "Pr": 140.91, "Nd": 144.24,
    "Pm": 145, "Sm": 150.36, "Eu": 151.96, "Gd": 157.25, "Tb": 158.93, "Dy": 162.50,
    "Ho": 164.93, "Er": 167.26, "Tm": 168.93, "Yb": 173.05, "Lu": 174.97, "Hf": 178.49,
    "Ta": 180.95, "W": 183.84, "Re": 186.21, "Os": 190.23, "Ir": 192.22, "Pt": 195.08,
    "Au": 196.97, "Hg": 200.59, "Tl": 204.38, "Pb": 207.2, "Bi": 208.98, "Po": 209,
    "At": 210, "Rn": 222, "Fr": 223, "Ra": 226, "Ac": 227, "Th": 232.04, "Pa": 231.04,
    "U": 238.03, "Np": 237, "Pu": 244, "Am": 243, "Cm": 247, "Bk": 247, "Cf": 251,
    "Es": 252, "Fm": 257, "Md": 258, "No": 259, "Lr": 266, "Rf": 267, "Db": 268,
    "Sg": 269, "Bh": 270, "Hs": 277, "Mt": 278, "Ds": 281, "Rg": 282, "Cn": 285,
    "Fl": 289, "Lv": 293, "Ts": 294, "Og": 294
}

# Fungsi hitung Mr
def hitung_mr(rumus):
    elemen = re.findall(r'([A-Z][a-z])(\d)', rumus)
    mr = 0
    for simbol, jumlah in elemen:
        jumlah = int(jumlah) if jumlah else 1
        if simbol in massa_atom:
            mr += massa_atom[simbol] * jumlah
        else:
            st.error(f"Unsur tidak dikenali: {simbol}")
            return None
    return mr

# UI Streamlit
st.title("⚗ Kalkulator Massa Molekul Relatif (Mr)")
rumus = st.text_input("Masukkan Rumus Kimia", placeholder="Contoh: H2O, Fe2O3, NaCl")

if rumus:
    hasil = hitung_mr(rumus)
    if hasil is not None:
        st.success(f"Mr dari *{rumus.upper()}* adalah *{hasil:.2f} g/mol*")

# Data sederhana untuk contoh
tabel_periodik = {
    "H": {"nama": "Hidrogen", "nomor_atom": 1, "massa_atom": 1.008},
    "He": {"nama": "Helium", "nomor_atom": 2, "massa_atom": 4.0026},
    "O": {"nama": "Oksigen", "nomor_atom": 8, "massa_atom": 15.999},
    "C": {"nama": "Karbon", "nomor_atom": 6, "massa_atom": 12.011},
    # Tambahkan data lainnya sesuai kebutuhan
}

# Sidebar
st.sidebar.title("KalkulatorMr")
menu = st.sidebar.radio("Pilih Menu", [
    "Lihat Tabel Periodik",
    "Cari Unsur Berdasarkan Simbol",
    "Hitung Massa Molekul"
])

# Halaman 1: Lihat Tabel Periodik
if menu == "Lihat Tabel Periodik":
    st.title("Tabel Periodik Sederhana")
    st.write("Berikut adalah beberapa unsur dari tabel periodik:")
    for simbol, info in tabel_periodik.items():
        st.write(f"**{simbol}** - {info['nama']} | Nomor Atom: {info['nomor_atom']} | Massa Atom: {info['massa_atom']}")

# Halaman 2: Cari Unsur
elif menu == "Cari Unsur Berdasarkan Simbol":
    st.title("Cari Unsur")
    simbol = st.text_input("Masukkan simbol unsur (contoh: H, He, O)")
    if simbol:
        unsur = tabel_periodik.get(simbol)
        if unsur:
            st.success(f"Nama: {unsur['nama']}")
            st.write(f"Nomor Atom: {unsur['nomor_atom']}")
            st.write(f"Massa Atom: {unsur['massa_atom']}")
        else:
            st.error("Simbol tidak ditemukan dalam data.")

# Halaman 3: Hitung Massa Molekul
elif menu == "Hitung Massa Molekul":
    st.title("Kalkulator Massa Molekul")
    rumus = st.text_input("Masukkan rumus kimia (misalnya: H2O, CO2)")

    import re
    def hitung_massa_molekul(rumus):
        pola = r"([A-Z][a-z]*)(\d*)"
        total = 0.0
        for simbol, jumlah in re.findall(pola, rumus):
            jumlah = int(jumlah) if jumlah else 1
            if simbol in tabel_periodik:
                massa = tabel_periodik[simbol]["massa_atom"]
                total += massa * jumlah
            else:
                return None
        return total

    if rumus:
        hasil = hitung_massa_molekul(rumus)
        if hasil is not None:
            st.success(f"Massa molekul dari {rumus} adalah {hasil:.3f} uma")
        else:
            st.error("Rumus mengandung simbol yang tidak dikenal.")

