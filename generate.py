import random
import string

def generate_password(length):
    if length < 4:
        return "❌ Password too short. Must be at least 4 characters."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# --- Run the app ---
print("🔐 Random Password Generator")

try:
    length = int(input("Enter desired password length: "))
    result = generate_password(length)
    print(f"\nGenerated Password: {result}")
except ValueError:
    print("❌ Please enter a valid number.")
