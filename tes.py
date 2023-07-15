import streamlit as st

def main():
    st.set_page_config(page_title="Aplikasi Menu", page_icon="📚", layout="wide")

    # Sidebar
    st.sidebar.title("Menu Utama")
    selected_menu = st.sidebar.selectbox("Pilih Menu", ("Beranda", "Tentang", "Kontak"))

    # Main content
    if selected_menu == "Beranda":
        st.title("Selamat Datang di Beranda")
        st.write("Ini adalah halaman beranda aplikasi.")

    elif selected_menu == "Tentang":
        st.title("Tentang Kami")
        st.write("Ini adalah halaman tentang kami.")

    elif selected_menu == "Kontak":
        st.title("Hubungi Kami")
        st.write("Ini adalah halaman kontak kami.")

    # Footer
    st.markdown("---")
    st.write("© 2023 Aplikasi Menu")

if __name__ == "__main__":
    main()