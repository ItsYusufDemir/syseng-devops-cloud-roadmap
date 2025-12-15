import os
import time
import json
import subprocess
import shutil

# --- CONFIGURATION ---
# OUTPUT from High Side transfer (Where the request arrives)
WATCH_DIR = "./airgap_sim/low_side_out"

# INPUT to Low Side transfer (Where we drop the downloaded file to go up)
EXPORT_DIR = "./airgap_sim/low_side_in"

def process_request(filename):
    filepath = os.path.join(WATCH_DIR, filename)
    
    try:
        # 1. Read JSON Request
        with open(filepath, 'r') as f:
            data = json.load(f)
        
        # Check if it is the correct type
        if data.get('type') != 'pypi':
            print(f" [i] Ignoring non-pypi request: {filename}")
            # Optional: Move to quarantine instead of delete if you want to inspect
            os.remove(filepath)
            return

        pkg_name = data.get('package_name')
        print(f" [!] Request Received: {pkg_name}")

        # 2. Download Package
        print(f" [...] Downloading '{pkg_name}'...")
        subprocess.check_call([
            "pip", "download", 
            pkg_name, 
            "--dest", EXPORT_DIR,
            "--no-deps" # Only download the specific package requested
        ])
        print(f" [V] Downloaded to: {EXPORT_DIR}")

        # 3. Cleanup Request File
        os.remove(filepath)
        print(f" [x] Request closed: {filename}")

    except Exception as e:
        print(f" [!] Error: {e}")
        # Delete failed request to prevent infinite loops
        if os.path.exists(filepath):
            os.remove(filepath)

def main():
    print("--- LOW SIDE LISTENER (Internet Connected) ---")
    print(f"Watching (Requests): {WATCH_DIR}")
    print(f"Exporting (Downloads): {EXPORT_DIR}")
    
    # Ensure dirs exist
    if not os.path.exists(WATCH_DIR): os.makedirs(WATCH_DIR)
    if not os.path.exists(EXPORT_DIR): os.makedirs(EXPORT_DIR)

    while True:
        # Get list of .json files
        files = [f for f in os.listdir(WATCH_DIR) if f.endswith('.json')]
        
        for f in files:
            process_request(f)
            
        time.sleep(2)

if __name__ == '__main__':
    main()