import pyautogui
import bleak
import asyncio
import signal
import platform


ACC_DATA_CHAR_UUID = "E95DCA4B-251D-470A-A062-FA1922DFA9A8"

FStop = 0
FTiltR = 0
FTiltL = 0


def acc_handler(sender, data):

    # print("x - {0:x} {1:x}".format(data[1], data[0]))
    if (data[1] & 0x10) == 0x10:
        accX = -((~data[1] + 256) * 0x100 + (~data[0] + 256))
        # print("accX:{0}".format(accX))
    else:
        accX = data[1] * 0x100 + data[0]
        # print("accX:{0}".format(accX))

    # print("y - {0:x} {1:x}".format(data[3], data[2]))
    if (data[3] & 0x10) == 0x10:
        accY = -((~data[3] + 256) * 0x100 + (~data[2] + 256))
        # print("accY:         {0}".format(accY))
    else:
        accY = data[3] * 0x100 + data[2]
        # print("accY:         {0}".format(accY))

    # print("z - {0:x} {1:x}".format(data[5], data[4]))
    if (data[5] & 0x10) == 0x10:
        accZ = -((~data[5] + 256) * 0x100 + (~data[4] + 256))
        # print("accZ:                {0}".format(accZ))
    else:
        accZ = data[5] * 0x100 + data[4]
        # print("accZ:                {0}".format(accZ))

    # print("A - {0}: {1}".format(sender, data))
    global FTiltR, FTiltL
    # right
    if (FTiltR == 0) and (accX > 1500) and (accY > -800):
        pyautogui.press('right')
        FTiltR = 1
    elif (FTiltR == 1) and (accX < 400):
        FTiltR = 0
    # left
    if (FTiltL == 0) and (accY > 1400):
        pyautogui.press('left')
        FTiltL = 1
    elif (FTiltL == 1) and (accY < 400):
        FTiltL = 0


def exit_sig(sig, frame):
    global FStop
    FStop = 1
    print("Exit!")


async def run(address, lp):
    async with bleak.BleakClient(address, loop=lp) as client:
        x = await client.is_connected()
        print("Connected!")
        print("Press Ctrl + c to exit ... ")
        await client.start_notify(ACC_DATA_CHAR_UUID, acc_handler)
        global FStop
        while not FStop:
            await asyncio.sleep(0.5)

        await client.stop_notify(ACC_DATA_CHAR_UUID)


if __name__ == '__main__':
    signal.signal(2, exit_sig)
    if platform.system() == 'Darwin':
        BIT_ADDR = "B19A5BC3-28BA-4B51-A39D-C1C3ED28BB46"
    else:
        BIT_ADDR = 'F9:8D:B1:97:51:2E'
    opLoop = asyncio.get_event_loop()
    opLoop.run_until_complete(run(BIT_ADDR, opLoop))


