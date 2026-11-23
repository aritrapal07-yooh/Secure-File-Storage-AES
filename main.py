
import os
import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox

from cryptography.fernet import Fernet, InvalidToken

OUTPUT_FOLDER = "encrypted_files"
KEY_FILE = "secret.key"

os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def load_key():
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()


def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        original_data = file.read()

    encrypted_data = fernet.encrypt(original_data)

    file_name = os.path.basename(file_path)
    output_path = os.path.join(
        OUTPUT_FOLDER, file_name + ".enc"
    )

    with open(output_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    return output_path


def decrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    file_name = os.path.basename(file_path)

    if file_name.endswith(".enc"):
        file_name = file_name[:-4]

    output_path = os.path.join(
        OUTPUT_FOLDER, "decrypted_" + file_name
    )

    with open(output_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    return output_path


def select_encrypt_file():
    file_path = filedialog.askopenfilename(
        title="Select File to Encrypt"
    )

    if not file_path:
        return

    try:
        output_path = encrypt_file(file_path)

        messagebox.showinfo(
            "Encryption Successful",
            f"Encrypted file saved:\n{output_path}"
        )

    except FileNotFoundError:
        messagebox.showerror(
            "Error", "Encryption key not found."
        )

    except Exception as error:
        messagebox.showerror(
            "Error", str(error)
        )


def select_decrypt_file():
    file_path = filedialog.askopenfilename(
        title="Select Encrypted File",
        filetypes=[("Encrypted files", "*.enc")]
    )

    if not file_path:
        return

    try:
        output_path = decrypt_file(file_path)

        messagebox.showinfo(
            "Decryption Successful",
            f"Decrypted file saved:\n{output_path}"
        )

    except InvalidToken:
        messagebox.showerror(
            "Decryption Failed",
            "Wrong key or corrupted encrypted file."
        )

    except FileNotFoundError:
        messagebox.showerror(
            "Error", "Encryption key not found."
        )

    except Exception as error:
        messagebox.showerror(
            "Error", str(error)
        )

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()

    with open(file_path, "rb") as file:
        for block in iter(
            lambda: file.read(4096), b""
        ):
            sha256_hash.update(block)

    return sha256_hash.hexdigest()

def verify_file_integrity():
    file_path = filedialog.askopenfilename(
        title="Select File to Verify"
    )

    if not file_path:
        return

    file_hash = calculate_sha256(file_path)

    messagebox.showinfo(
        "File Integrity",
        f"SHA-256 Hash:\n\n{file_hash}\n\n"
        "Keep this hash for comparison."
    )


# GUI window
root = tk.Tk()
root.title("Secure File Storage System")
root.geometry("500x350")
root.resizable(False, False)

title_label = tk.Label(
    root,
    text="SECURE FILE STORAGE",
    font=("Arial", 18, "bold")
)
title_label.pack(pady=25)

subtitle_label = tk.Label(
    root,
    text="AES-based File Encryption and Decryption",
    font=("Arial", 10)
)
subtitle_label.pack(pady=5)

encrypt_button = tk.Button(
    root,
    text="Encrypt File",
    command=select_encrypt_file,
    width=25,
    height=2,
    bg="#2E8B57",
    fg="white"
)
encrypt_button.pack(pady=15)

decrypt_button = tk.Button(
    root,
    text="Decrypt File",
    command=select_decrypt_file,
    width=25,
    height=2,
    bg="#1E90FF",
    fg="white"
)
decrypt_button.pack(pady=10)

verify_button = tk.Button(
    root,
    text="Verify File Integrity",
    command=verify_file_integrity,
    width=25,
    height=2,
    bg="#6A5ACD",
    fg="white"
)
verify_button.pack(pady=10)


exit_button = tk.Button(
    root,
    text="Exit",
    command=root.destroy,
    width=15
)
exit_button.pack(pady=10)

root.mainloop()
