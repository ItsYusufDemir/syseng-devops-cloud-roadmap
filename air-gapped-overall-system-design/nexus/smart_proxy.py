from flask import Flask, redirect
import requests
import json
import time
import os

app = Flask(__name__)

# --- CONFIG ---
# Real Nexus URL (Internal)
NEXUS_URL = "http://192.168.1.157:8081/repository/air-gapped-pypi/simple"

# TRANSFER INPUT: Where we drop files *to be transferred*
REQUESTS_OUTBOX = "./airgap_sim/high_side_in/"

@app.route('/simple/<package_name>/')
def handle_request(package_name):
    # 1. Check if package exists in local Nexus first
    try:
        resp = requests.get(f"{NEXUS_URL}/{package_name}/", timeout=2)
        if resp.status_code == 200:
            # If found, redirect user to the real internal repo
            return redirect(f"{NEXUS_URL}/{package_name}/", code=302)
    except:
        pass # If Nexus is down or package missing, proceed to request it

    # 2. Package missing? Create Ticket for Low Side
    create_request(package_name)

    # 3. Notify User
    return f"""
    <html><body>
    <h1>Request Sent: {package_name}</h1>
    <p>Package not found on High Side. Request sent to Low Side agent.</p>
    <p>Please check back in 2 minutes.</p>
    </body></html>
    """, 404

def create_request(pkg):
    # Filename is just the timestamp
    timestamp = str(int(time.time()))
    filename = f"{timestamp}.json"
    filepath = os.path.join(REQUESTS_OUTBOX, filename)
    
    # JSON Content: type and package_name
    data = {
        "type": "pypi",
        "package_name": pkg
    }
    
    # Ensure directory exists
    if not os.path.exists(REQUESTS_OUTBOX):
        os.makedirs(REQUESTS_OUTBOX)

    with open(filepath, 'w') as f:
        json.dump(data, f)
    
    print(f" [>] Request Created (Input to Transfer): {filename} -> {data}")

if __name__ == '__main__':
    print(f"--- SMART PROXY (High Side) ---")
    print(f"Writing to: {REQUESTS_OUTBOX}")
    app.run(port=5000)