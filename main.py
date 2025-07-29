import subprocess
import os
from constants import *

def check_http_connectivity(url):
    print("\n🔍 Verifying Internet access...")
    try:
        subprocess.check_call(["wget", "--spider", "-q", url], timeout=5)
        print(f"{'✔ Internet access (HTTP)':40} OK")
        print(f"{'✔ GitHub accessibility':40} OK")
        return True
    except subprocess.TimeoutExpired:
        print("❌ Page doesn't exits\n")
        print("💡 To fix: Make sure URL is valid")
        return False
    except subprocess.CalledProcessError:
        print("❌ Internet is NOT reachable over HTTP.\n")
        print("💡 Possible Causes:")
        print("   - VPN not connected")
        print("   - Proxy not configured correctly")
        print("   - GitHub URL is unreachable")
        print("💡 Hint:")
        print("   - Connect to Bosch VPN")
        print("   - Set HTTP_PROXY and HTTPS_PROXY in `constants.py` file")
        print("   - Verify the URL is correct")
        return False
    
if __name__ == "__main__":
    print("\n===============================================")
    print("        Developer Environment Health Check")
    print("===============================================")
    # print(f"\n🕒 Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    all_ok = True

    if not check_http_connectivity(GITHUB_URL):
        all_ok = False


    print("\n-----------------------------------------------")
    if all_ok:
        print("✅ All checks passed successfully.")
    else:
        print("❌ One or more checks failed. Please review the help text above.")
    print("-----------------------------------------------\n")