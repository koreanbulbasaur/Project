import win32gui
import win32con

# 알람을 설정할 시간
alarm_time = 7, 30

# 알람을 생성합니다.
alarm_handle = win32gui.CreateAlarmW(alarm_time, None, None, None, None)

# 알람을 활성화합니다.
win32gui.EnableAlarm(alarm_handle, True)