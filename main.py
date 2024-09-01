import sys
import subprocess

def run_script(script_name):
    subprocess.run(["python", script_name + ".py"])

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a script name")
        sys.exit(1)

    script_name = sys.argv[1]
    # AtCoder: A, B, C, D, E, F, G
    if script_name in "abcdefg":
        run_script(script_name)
    else:
        print("Invalid script name")
        sys.exit(1)
