import hashlib
import hmac
import os

# Encrypt Function
def EncryptText (text: str, algorithm: str, salt: str = None):
    hash = None

    if not text:
        return ValueError("Text is empty")
    
    if algorithm == "MD5":
        hash = hashlib.md5(text.encode()).hexdigest()
    elif algorithm == "SHA1":
        hash = hashlib.sha1(text.encode()).hexdigest()
    elif algorithm == "SHA2_224":
        hash = hashlib.sha224(text.encode()).hexdigest()
    elif algorithm == "SHA2_256":
        hash = hashlib.sha256(text.encode()).hexdigest()
    elif algorithm == "SHA2_512":
        hash = hashlib.sha512(text.encode()).hexdigest()
    elif algorithm == "HMAC-SHA1":
        hash = hmac.new(salt.encode(), text.encode(), hashlib.sha1).hexdigest()
    else:
        return ValueError("Algorithm not found")
    
    return hash

# Decrypt Function
def DecryptText(hashText: str, algorithm: str, salt: str = None) -> str:
    if not os.path.exists("wordlist/hashs.txt"):
        raise FileNotFoundError("File not found: hashs.txt")
    
    possibleAlgorithm = None
    
    with open("wordlist/hashs.txt", "r") as file:
        for line in file:
            try:
                storedHash, originalText = line.strip().split(":", 1) 
                computedHash = EncryptText(originalText, algorithm, salt)

                if computedHash == hashText:
                    return f"{originalText}"
                
                for algo in ["MD5", "SHA1", "SHA256", "SHA512", "SHA2_256"]:
                    if EncryptText(originalText, algo, salt) == hashText:
                        possibleAlgorithm = algo
                        break

            except ValueError:
                continue

    if possibleAlgorithm:
        return f"The hash you entered might be {possibleAlgorithm}. Please change the decryption algorithm."

    return "No matching hash found for decryption."
