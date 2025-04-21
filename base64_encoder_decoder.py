import base64

def encode_text(text):
    try:
        encoded_bytes = base64.b64encode(text.encode('utf-8'))
        return encoded_bytes.decode('utf-8')
    except Exception as e:
        return f"Error encoding: {e}"

def decode_text(encoded_text):
    try:
        decoded_bytes = base64.b64decode(encoded_text.encode('utf-8'))
        return decoded_bytes.decode('utf-8')
    except Exception as e:
        return f"Error decoding: {e}"

def main():
    print("🔐 Base64 Encoder/Decoder - CodMetric Task 5 🔐")
    while True:
        print("\nChoose an option:")
        print("1. Encode text")
        print("2. Decode text")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            text = input("Enter text to encode: ").strip()
            if not text:
                print("⚠️ Input cannot be empty!")
                continue
            print("🔒 Encoded:", encode_text(text))

        elif choice == '2':
            encoded_text = input("Enter Base64 text to decode: ").strip()
            if not encoded_text:
                print("⚠️ Input cannot be empty!")
                continue
            print("🔓 Decoded:", decode_text(encoded_text))

        elif choice == '3':
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
