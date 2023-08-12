from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def volume_program(num):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    # 현재 볼륨 값 가져오기
    current_volume = int(volume.GetMasterVolumeLevelScalar() * 100)

    sound_level = level(current_volume, num)

    # 볼륨 설정
    volume.SetMasterVolumeLevelScalar(sound_level / 100, None)
    
    text = f'지금 소리를 {sound_level}으로 조절했습니다'
    return text

# 소리 값을 숫자로 반환
def level(curr_n, n):
    n = str(n)
    if 'max' in n:
        output_level = 100

    elif 'med' in n:
        output_level = 50

    elif 'little' in n:
        output_level = curr_n + 5

    elif 'slight' in n:
        output_level = curr_n - 5

    else:
        output_level = int(n)

    if output_level >= 100:
        output_level = 100
    elif output_level <= 0:
        output_level = 0

    return output_level