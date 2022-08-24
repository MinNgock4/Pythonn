import os 
import signal  # thư viện kill process
import psutil  # thư viện lấy PID qua Name

def find_kill_process(name_process):
	PID = [] # xử lí app có nhiều PID
# Tìm kiếm name_process trong danh sách Details của system 
	for sys_proc in psutil.process_iter():
		if name_process in sys_proc.name():
			PID.append(sys_proc.pid)  # thêm pid vào DS_PID 
# xuất PID
	print("PID", name_process, ":" ,PID)
# kill process with PID
	if len(PID) == 0:
		print("Name Process isn't exist...")
	else:
		for i in PID:
			os.kill(i, signal.SIGTERM)
		print("Kill "+ name_process + " Successful...")


name_process = input("Name Proccess Killed: ")
find_kill_process(name_process)
