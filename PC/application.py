from pycaw.pycaw import AudioUtilities, AudioDeviceState

devices = AudioUtilities.GetAllDevices()
for device in devices:
    if device.state == AudioDeviceState.Active:
        print(f"Name: {device.FriendlyName}")
