import hashlib

# Function to calculate SHA-256 hash of a string
def sha256_hash(input_string):
    sha_signature = hashlib.sha256(input_string.encode()).hexdigest()
    return sha_signature

# Function to calculate MD5 hash of a string
def md5_string(input_string):
    md5_hash = hashlib.md5()
    md5_hash.update(input_string.encode('utf-8'))
    return md5_hash.hexdigest()

# Main program
def main():
    print("\n=== MENU ===")
    print("1. SHA-256 (Secure Hash Algorithm)")
    print("2. MD5 (Message-Digest Algorithm 5)")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
        
    if choice == '1':
        input_string = input("Enter the text for SHA-256 hashing: ")
        hash_result = sha256_hash(input_string)
        print("SHA-256 Hash:", hash_result)
        
    elif choice == "2":
        user_string = input("Enter the string to hash: ")
        print("MD5 Hash of the string:", md5_string(user_string))
    
    elif choice == '3':
        print("Exiting...")
        return
    
    else:
        print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()
