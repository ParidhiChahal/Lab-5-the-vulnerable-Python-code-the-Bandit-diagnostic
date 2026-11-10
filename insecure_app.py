import subprocess
import random

# Issue 1 (B105): Hard-coded password string
ADMIN_PASSWORD = "SuperSecretAdminPassword123"

def authenticate(password):
    if password == ADMIN_PASSWORD:
        return True
    return False

# Issue 2 (B602): Subprocess call with shell=True (Command Injection Risk)
def run_system_command(user_input):
    cmd = f"echo Running command for: {user_input}"
    subprocess.run(cmd, shell=True)

# Issue 3 (B311): Using pseudo-random generator (random) for security tokens
def generate_token():
    token = ''.join(random.choice('0123456789ABCDEF') for _ in range(32))
    return token

if __name__ == "__main__":
    print("Insecure App Initialized")
