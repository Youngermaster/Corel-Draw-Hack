import shutil
import subprocess
import configparser

# Parameters can be ENABLED or DISABLED
def internet_state_controller(state):
    subprocess.run(["netsh", "interface", "set", "interface", "Wi-Fi", state])


def delete_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
    except OSError as e:
        print("Error: %s : %s" % (folder_path, e.strerror))


def run_corel(corel_process_path):
    subprocess.run(corel_process_path)


if __name__ == "__main__":
    config = configparser.RawConfigParser()   
    configFilePath = r'.config'
    config.read(configFilePath)
    internet_state_controller("DISABLED")
    delete_folder(config.get('your-config', 'folder_path'))
    run_corel(config.get('your-config', 'corel_process_path'))
    internet_state_controller("ENABLED")
