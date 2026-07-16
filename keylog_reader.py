import re
import time
import os
from datetime import datetime


OUTPUT_FILE = "keylogs_reconstructed.txt"


def parse_key_event(line):

    match = re.match(
        r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}): (.+)',
        line
    )

    if not match:
        return None, None

    timestamp_str, key = match.groups()

    timestamp = datetime.strptime(
        timestamp_str,
        "%Y-%m-%d %H:%M:%S,%f"
    )

    return timestamp, key



def convert_key(key):

    special = {

        "Key.enter": "\n",
        "Key.space": " ",
        "Key.backspace": "[BACKSPACE]",
        "Key.tab": "[TAB]",
        "Key.shift": "[SHIFT]",
        "Key.shift_r": "[SHIFT]",
        "Key.ctrl_l": "[CTRL]",
        "Key.ctrl_r": "[CTRL]",
        "Key.alt_l": "[ALT]",
        "Key.alt_r": "[ALT]",
        "Key.esc": "[ESC]",
        "Key.delete": "[DELETE]",

    }


    if key in special:
        return special[key]


    if key.startswith("'") and key.endswith("'"):

        return key[1:-1]


    return f"[{key}]"



def realtime_keylog_reader(log_file="keylogs.txt"):


    last_position = 0


    # create file
    open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ).write(
        "=== Reconstructed Key Logs ===\n\n"
    )


    while True:


        if not os.path.exists(log_file):
            time.sleep(1)
            continue


        with open(
            log_file,
            "r",
            encoding="utf-8",
            errors="ignore"
        ) as file:


            file.seek(last_position)

            lines = file.readlines()

            last_position = file.tell()



        for line in lines:


            timestamp, key = parse_key_event(line)


            if not key:
                continue


            readable = convert_key(key)


            with open(
                OUTPUT_FILE,
                "a",
                encoding="utf-8"
            ) as output:

                output.write(readable)



        time.sleep(0.2)



if __name__ == "__main__":

    realtime_keylog_reader()