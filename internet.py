import requests
import subprocess

def check_internet_connectivity():
    try:
        # Check using GET request to Google
        response = requests.get("http://www.google.com")
        response.raise_for_status()
        
        # Check using ping to 8.8.8.8
        subprocess.run(["ping", "-c", "1", "8.8.8.8"], check=True)
        
        return True
    except requests.exceptions.RequestException:
        return False
    except subprocess.CalledProcessError:
        return False


if __name__ == "__main__":
    if check_internet_connectivity():
        print("Internet connectivity established.")
    else:
        print("No internet connectivity......!!!")

