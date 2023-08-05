import subprocess

brightness_level = 0  # 밝기 레벨 (0 ~ 100)
subprocess.run(["powershell", "(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1, {})".format(brightness_level)])