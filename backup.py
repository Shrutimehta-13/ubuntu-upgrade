import datetime
import shutil
import subprocess


def backup_previous_version():
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    BACK_UP = "/home/mehta/Downloads/Backup"
    backup_folder = f"{BACK_UP}/backup_{timestamp}"

    try:
        # Create backup folder
        subprocess.run(["mkdir", "-p", backup_folder])

        # Backup /etc to tar.gz
        subprocess.run(["sudo", "tar", "czf", f"{backup_folder}/local_backup.tar.gz", "/"])

        # Print backup location
        print(f"Backup created at: {backup_folder}")
    except Exception as e:
        print(f"Error creating backup: {e}")


def main():
	backup_previous_version()

if __name__ == "__main__":
    main()
    
    
    
#BACK_UP = "/home/mehta/Downloads/Backup"
