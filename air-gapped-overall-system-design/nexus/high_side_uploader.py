import os
import time
import subprocess
import sys

# --- CONFIGURATION ---
WATCH_DIR = "./airgap_sim/high_side_out"

# Nexus Credentials
NEXUS_UPLOAD_URL = "http://192.168.1.157:8081/repository/air-gapped-pypi/"
NEXUS_USER = "example"       
NEXUS_PASS = "123"    

def upload_package(filename):
    filepath = os.path.join(WATCH_DIR, filename)
    
    if not (filename.endswith('.whl') or filename.endswith('.tar.gz')):
        return

    print(f" [!] New Package Detected: {filename}")
    print(f" [...] Uploading to Nexus...")

    try:
        # METHOD: Calling twine via python module
        # FIX: Removed '--skip-existing' causing the error
        cmd = [
            sys.executable, "-m", "twine", "upload",
            "--repository-url", NEXUS_UPLOAD_URL,
            "-u", NEXUS_USER,
            "-p", NEXUS_PASS,
            filepath,
            "--non-interactive"
        ]
        
        # We capture output to suppress huge stack traces if it fails
        subprocess.check_output(cmd, stderr=subprocess.STDOUT)
        
        print(f" [V] SUCCESS: {filename} uploaded to Nexus.")
        os.remove(filepath)

    except subprocess.CalledProcessError as e:
        output = e.output.decode()
        if "400" in output or "409" in output:
             # 400/409 usually means file already exists. We can safely delete it.
             print(f" [i] Package already exists in Nexus. Deleting local copy.")
             os.remove(filepath)
        else:
             print(f" [!] Upload Failed. Error output:\n{output}")

    except Exception as e:
        print(f" [!] System Error: {e}")

def main():
    print("--- HIGH SIDE UPLOADER (Internal Nexus) ---")
    print(f"Watching: {WATCH_DIR}")
    
    if not os.path.exists(WATCH_DIR): os.makedirs(WATCH_DIR)

    while True:
        files = os.listdir(WATCH_DIR)
        for f in files:
            upload_package(f)
        time.sleep(2)

if __name__ == "__main__":
    main()