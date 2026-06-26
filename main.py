import sys
import subprocess
import string

def run_script(script_name):
    subprocess.run(["python", script_name + ".py"])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a script name")
        sys.exit(1)

    script_name = sys.argv[1]
    if script_name in string.ascii_lowercase:
        run_script(script_name)
    else:
        print("Invalid script name")
        sys.exit(1)
