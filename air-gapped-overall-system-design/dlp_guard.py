import os
import shutil
import time

# --- CONFIGURATION ---
INPUT_DIR = "./airgap_sim/high_side_in"
OUTPUT_DIR = "./airgap_sim/low_side_out"

def move_file(filename):
    src_path = os.path.join(INPUT_DIR, filename)
    dest_path = os.path.join(OUTPUT_DIR, filename)
    
    print(f" [i] Simulating DLP & Officer check for: {filename}...")
    time.sleep(0.5) # Fake processing time
    
    shutil.move(src_path, dest_path)
    print(f" [V] Transferred: {filename} -> Low Side")

def main():
    print("--- Simple DLP Guard Running ---")
    while True:
        if os.path.exists(INPUT_DIR):
            files = os.listdir(INPUT_DIR)
            for f in files:
                move_file(f)
        time.sleep(2)

if __name__ == "__main__":
    main()