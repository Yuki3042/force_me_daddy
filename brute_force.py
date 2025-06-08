import pyzipper

zip_file_path = "force me.zip"
wordlist_path = "wordlist.txt"

# Membaca wordlist
with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as f:
    wordlist = [line.strip() for line in f]

# Coba brute-force
with pyzipper.AESZipFile(zip_file_path) as zf:
    for password in wordlist:
        try:
            zf.pwd = password.encode("utf-8")
            zf.extractall()
            print(f"✅ Password ditemukan: {password}")
            break
        except RuntimeError:
            print(f"❌ Gagal: {password}")
        except Exception as e:
            print(f"⚠️ Error lain saat mencoba {password}: {e}")
