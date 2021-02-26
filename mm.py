import sys
import time
import win32api

while(True):
	current = win32api.GetCursorPos()
	cx = current[0]
	cy = current[1]
	if( (int(time.time())%2) == 0):
		mx = cx+1
	else:
		mx = cx-1
	my = cy
	win32api.SetCursorPos((int(mx),int(my)))
	time.sleep(11)