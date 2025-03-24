import streamlit as st
from cryptography.fernet import Fernet
import csv
import os

# Streamlit page configuration
st.set_page_config(page_title="Hasher.com", page_icon="🔐", layout="centered")

# Custom Theme Styling
st.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            background-color: #1E1E1E;
            padding: 20px;
            color: white;
        }
        .stRadio [role=radiogroup] {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .stRadio div[role=radio] {
            background: #2A2A2A;
            padding: 10px;
            border-radius: 8px;
            text-align: center;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        .stRadio div[role=radio]:hover {
            background: #444;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.title("🔐 Hasher.com")
st.write("A simple and secure text encryption & decryption tool.")

# Sidebar navigation with custom styling
st.sidebar.markdown("## Select an Option")
option = st.sidebar.radio("", ["Encrypt", "Decrypt", "View Logs"])

log_file = "log.csv"
header = ["Input Text", "Key", "Output", "Message"]
if not os.path.exists(log_file):
    with open(log_file, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)

# Encryption
if option == "Encrypt":
    st.subheader("🔑 Encrypt Your Text")
    text = st.text_area("Enter text to encrypt:")
    if st.button("Generate Key & Encrypt"):
        if text:
            key = Fernet.generate_key()
            f = Fernet(key)
            encrypted_text = f.encrypt(text.encode())
            
            st.success("Text encrypted successfully!")
            st.code(encrypted_text.decode(), language="text")
            st.write("🔑 **Save this key to decrypt later:**")
            st.code(key.decode(), language="text")
            
            with open(log_file, "a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([text, key.decode(), encrypted_text.decode(), "Encryption Successful"])
        else:
            st.warning("Please enter text to encrypt.")

# Decryption
elif option == "Decrypt":
    st.subheader("🔓 Decrypt Your Text")
    key = st.text_input("Enter your secret key:")
    encrypted_token = st.text_area("Enter encrypted text:")
    
    if st.button("Decrypt"):
        if key and encrypted_token:
            try:
                f = Fernet(key.encode())
                decrypted_text = f.decrypt(encrypted_token.encode()).decode()
                st.success("Decryption successful!")
                st.code(decrypted_text, language="text")
                
                with open(log_file, "a", newline="") as file:
                    writer = csv.writer(file)
                    writer.writerow([encrypted_token, key, decrypted_text, "Decryption Successful"])
            except Exception as e:
                st.error("Invalid key or encrypted text. Please check your inputs.")
        else:
            st.warning("Please enter both key and encrypted text.")

# View Logs
elif option == "View Logs":
    st.subheader("📜 Encryption & Decryption Logs")
    try:
        with open(log_file, "r") as file:
            reader = csv.reader(file)
            logs = list(reader)
            if len(logs) > 1:
                st.dataframe(logs, use_container_width=True)  # Enable warp mode
            else:
                st.info("No logs available yet.")
    except Exception as e:
        st.error(f"Error reading log file: {e}")

# Footer
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit and Cryptography module.")
