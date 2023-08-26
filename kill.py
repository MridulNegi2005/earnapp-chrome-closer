import psutil,time
def get_processes_by_name(name):
   """Return a list of processes matching 'name'."""
   matching_processes = [proc for proc in psutil.process_iter(['name']) if proc.info['name'] == name]
   return matching_processes

def kill_processes(processes):
   """Attempt to kill all 'processes'."""
   for proc in processes:
      try:
         proc.kill()
      except psutil.NoSuchProcess:
         print(f"No such process: {proc.pid}")
      except psutil.AccessDenied:
         print(f"Access denied to {proc.pid}")

process_name = "chrome.exe"
while True:
    processes_to_kill = get_processes_by_name(process_name)
    kill_processes(processes_to_kill)
    print("HEY")
    time.sleep(60)