import shutil
import subprocess

folder_path = 'tmp/'
process_path = 'C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'

# Parameters can be ENABLED or DISABLED
def internet_state(state):
    subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", state])


def delete_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
    except OSError as e:
        print("Error: %s : %s" % (folder_path, e.strerror))


def run_subproccess():
    subprocess.run(process_path)


if __name__ == "__main__":
    internet_state("DISABLED")
    delete_folder(folder_path)
    run_subproccess()
    internet_state("ENABLED")