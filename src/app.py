import sys
import os
import time as t
from ppadb.client import Client as AdbClient
from ppadb.device import Device
from com.dtmilano.android.viewclient import ViewClient


try:
    sys.path.insert(0, os.path.join(os.environ["ANDROID_VIEW_CLIENT_HOME"], "src"))
except:
    pass


if __name__ == "__main__":
    client = AdbClient(host="127.0.0.1", port=5037)  # Default is "127.0.0.1" and 5037

    device = Device(client=client, serial="R3CR10YWKQM")

    if device is None:
        print("NO DEVICE")
        quit()
    else:
        print(f"Connected to {device}")

    # device.shell("input keyevent 66")

    last_chat = []

    conn = ViewClient.connectToDeviceOrExit()

    while True:
        text = []
        current_text = []

        vc = ViewClient(*conn)
        # vc.traverse()

        FrameLayout = vc.findViewById(
            "com.kakao.talk:id/chat_log_recycler_list"
        ).children

        for frame in FrameLayout:
            children = frame.children
            for child in children:
                c = child.children
                if len(c) != 0:
                    text.append(c[0].getText())

        first_text = text[0]

        try:
            l = last_chat.index(first_text)
            i = text.index(last_chat[-1])
            current_text = text[i + 1 :]

        except ValueError:
            pass

        print(current_text)

        for sentence in current_text:
            if sentence == "!인사":
                device.input_text("HELLO WORLD!")
                device.shell("input keyevent 66")
                break

        last_chat = text
