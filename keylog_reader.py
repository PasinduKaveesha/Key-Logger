import re
import time
import os
from datetime import datetime

def parse_key_event(line):
    match = re.match(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}):\s*(.+)', line.strip())
    if not match:
        return None, None
    timestamp_str, key_str = match.groups()
    try:
        timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S,%f')
    except:
        timestamp = None
    return timestamp, key_str.strip()

def key_to_readable(key):
    key = key.strip()
    
    special_keys = {
        "Key.enter": "[ENTER]",
        "Key.backspace": "[BACKSPACE]",
        "Key.space": "[SPACE]",
        "Key.ctrl_l": "[CTRL]",
        "Key.ctrl_r": "[CTRL]",
        "Key.shift": "[SHIFT]",
        "Key.shift_r": "[SHIFT]",
        "Key.tab": "[TAB]",
        "Key.esc": "[ESC]",
        "Key.delete": "[DELETE]",
    }
    
    if key in special_keys:
        return special_keys[key]
    
    if key.startswith("'\\x") or key.startswith("\\x"):
        ctrl_char = key.strip("'")
        ctrl_map = {
            '\\x03': "[CTRL+C]", '\\x16': "[CTRL+V]", '\\x18': "[CTRL+X]",
            '\\x01': "[CTRL+A]", '\\x17': "[CTRL+W]", '\\x19': "[CTRL+Y]",
            '\\x1a': "[CTRL+Z]",
        }
        return ctrl_map.get(ctrl_char, f"[CTRL]")
    
    if key.startswith("'") and key.endswith("'"):
        char = key[1:-1]
        if char == " ":
            return " "
        if char == "\\n":
            return "[NEWLINE]"
        return char
    
    return f"[{key}]"

def realtime_keylog_reader(log_file="KeyLogs.txt"):
    print(f"Monitoring {log_file} in real-time... (Press Ctrl+C to stop)\n")
    
    buffer = []
    last_position = 0
    last_text = ""
    
    try:
        while True:
            if not os.path.exists(log_file):
                print(f"Waiting for {log_file} to appear...")
                time.sleep(1)
                continue
                
            with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
                f.seek(last_position)
                new_lines = f.readlines()
                last_position = f.tell()
            
            for line in new_lines:
                if not line.strip():
                    continue
                    
                timestamp, key_str = parse_key_event(line)
                if not key_str:
                    continue
                
                readable = key_to_readable(key_str)
                
                # Reconstruct typing buffer
                if key_str == "Key.backspace":
                    if buffer:
                        buffer.pop()
                elif key_str == "Key.enter":
                    current_sentence = "".join(buffer).strip()
                    if current_sentence:
                        print(f"\n[ENTER] → {current_sentence}")
                    buffer = []
                elif key_str.startswith("'") and key_str.endswith("'"):
                    char = key_str[1:-1]
                    if char not in ["\\n", "\\t"]:
                        buffer.append(char)
                
                # Live preview
                current = "".join(buffer)
                if current != last_text:
                    print(f"\rTyping: {current}", end="", flush=True)
                    last_text = current
            
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\n\nStopped.")
        final = "".join(buffer).strip()
        if final:
            print(f"Final text: {final}")
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    realtime_keylog_reader("KeyLogs.txt")