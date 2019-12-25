import pyautogui
import bleak
import asyncio
import signal
import platform


BUTTON_A_CHAR_UUID = "e95dda90-251d-470a-a062-fa1922dfa9a8"
BUTTON_B_CHAR_UUID = "e95dda91-251d-470a-a062-fa1922dfa9a8"

FStop = 0


def button_a_handler(sender, data):
    # print("A - {0}: {1}".format(sender, data))
    if data == b'\x01':
        pyautogui.press('left')
    elif data == b'\x02':
        pyautogui.press('esc')


def button_b_handler(sender, data):
    # print("B - {0}: {1}".format(sender, data))
    if data == b'\x01':
        pyautogui.press('right')


def exit_sig(sig, frame):
    global FStop
    FStop = 1
    print("Exit!")


async def run(address, lp):
    async with bleak.BleakClient(address, loop=lp) as client:
        x = await client.is_connected()
        print("Connected!")
        print("Press Ctrl + c to exit ... ")
        await client.start_notify(BUTTON_A_CHAR_UUID, button_a_handler)
        await client.start_notify(BUTTON_B_CHAR_UUID, button_b_handler)
        global FStop
        while not FStop:
            await asyncio.sleep(0.5)

        await client.stop_notify(BUTTON_A_CHAR_UUID)
        await client.stop_notify(BUTTON_B_CHAR_UUID)


if __name__ == '__main__':
    signal.signal(2, exit_sig)
    if platform.system() == 'Darwin':
        BIT_ADDR = "B19A5BC3-28BA-4B51-A39D-C1C3ED28BB46"
    else:
        BIT_ADDR = 'F9:8D:B1:97:51:2E'
    opLoop = asyncio.get_event_loop()
    opLoop.run_until_complete(run(BIT_ADDR, opLoop))


