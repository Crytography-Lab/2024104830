from cryptography.hazmat.primitives.asymmetric import dsa
from cryptography.hazmat.primitives import hashes

# Step 1: Generate private and public keys
private_key = dsa.generate_private_key(key_size=2048)
public_key = private_key.public_key()

# Get message from user
message = input("Enter the message: ").encode()

# Step 2: Create Digital Signature
signature = private_key.sign(
    message,
    hashes.SHA256()
)

print("\nDigital Signature:", signature.hex())

# Step 3: Verify Digital Signature
try:
    public_key.verify(
        signature,
        message,
        hashes.SHA256()
    )
    print("\nSignature is VALID")
    print("Message is authentic and unchanged.")

except Exception:
    print("\nSignature is INVALID")
