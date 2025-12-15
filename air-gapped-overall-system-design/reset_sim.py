import os
import shutil

# --- CONFIGURATION ---
FOLDERS = [
    "./airgap_sim/low_side_out",
    "./airgap_sim/high_side_in",
    "./airgap_sim/high_side_out",
    "./airgap_sim/low_side_in",
    "./airgap_sim/quarantine"
]

def reset_folders():
    print("--- Resetting Simulation Environment ---")
    
    for folder in FOLDERS:
        # 1. Remove existing folder and contents
        if os.path.exists(folder):
            try:
                shutil.rmtree(folder)
                print(f" [x] Cleared: {folder}")
            except Exception as e:
                print(f" [!] Error clearing {folder}: {e}")
        
        # 2. Recreate empty folder
        try:
            os.makedirs(folder)
            print(f" [+] Created: {folder}")
        except Exception as e:
            print(f" [!] Error creating {folder}: {e}")

    print("\n--- Environment Ready ---")

if __name__ == "__main__":
    reset_folders()