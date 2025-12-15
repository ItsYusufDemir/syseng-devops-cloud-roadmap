import subprocess
import time
import sys
import os

# The list of scripts to run in parallel
SCRIPTS = [
    "nexus/smart_proxy.py",       # 1. High Side: Creates Request
    "dlp_guard.py",        # 2. Guard: Transfers High -> Low
    "nexus/low_side_agent.py",    # 3. Low Side: Downloads File
    "cdr_guard.py",        # 4. Guard: Transfers Low -> High
    "nexus/high_side_uploader.py" # 5. High Side: Uploads to Nexus
]

def main():
    print("==================================================")
    print("   AIR GAP SIMULATION CONTROLLER")
    print("==================================================")
    
    # Optional: Reset folders if reset_sim.py exists
    if os.path.exists("reset_sim.py"):
        print(" [i] Resetting environment...")
        subprocess.run([sys.executable, "reset_sim.py"])
    
    processes = []
    print("\n [i] Launching services...")

    try:
        # Launch each script as a subprocess
        for script in SCRIPTS:
            if not os.path.exists(script):
                print(f" [!] ERROR: Could not find '{script}'")
                continue
                
            print(f" [+] Starting {script}...")
            # Use sys.executable to ensure we use the same python env
            p = subprocess.Popen([sys.executable, script])
            processes.append((script, p))
            time.sleep(1) # Small delay to prevent output jumbling

        print("\n [V] All systems operational.")
        print(" [i] Press Ctrl+C to stop the simulation.\n")
        
        # Keep the main thread alive to listen for Ctrl+C
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print("\n\n [!] Stopping simulation...")
        for name, p in processes:
            print(f" [-] Terminating {name}...")
            p.terminate()
        print(" [V] Shutdown complete.")

if __name__ == "__main__":
    main()