import subprocess
import sys

result = subprocess.run(
    [
        sys.executable,"-c",
        "print ('Child process is running.')"
    ],
    capture_output = True,
    text = True,
    check = True
)
print ("PROCESS MANAGEMENT REPORT")
print ("-----------------------------------------------")

print ("Program Output:", result.stdout.strip())
print ("Exit Code:", result.returncode)
print ("-----------------------------------------------")

automation = subprocess.run (
    [
        sys.executable, "-c",
        "print ('PYTHON AUTOMATION TASK COMPLETED.')"
    ],
    capture_output = True,
    text = True,
    check = True
)
print ("Program Output:", automation.stdout.strip())
print ("Exit Code:", result.returncode)

print ("-----------------------------------------------")
print ("PROCESS EXECUTION COMPLETED")