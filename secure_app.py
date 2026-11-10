import subprocess
import os
import secrets

# Fix 1: Load password securely from environment variables
ADMIN_PASSWORD = os.environ.get("ADMIN_PASSWORD", "default_fallback")

def authenticate(password):
    return secrets.compare_digest(password, ADMIN_PASSWORD)

# Fix 2: Avoid shell=True by passing arguments as a list
def run_system_command(user_input):
    # Safe execution without shell interpretation
    subprocess.run(["echo", "Running command for:", user_input], check=True)

# Fix 3: Use cryptographically secure 'secrets' module for tokens
def generate_token():
    return secrets.token_hex(16)

if __name__ == "__main__":
    print("Secure App Initialized")
