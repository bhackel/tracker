import psutil
import time
import datetime


def get_all_procs(attrs):
    """ Returns a list of dictionaries of processes
    on the computer 
    """

    # fetch all processes and their specified attributes
    attrs = ['name', 'username', 'create_time', 'status', 'pid']
    procs = {p.pid: p.info for p in psutil.process_iter(attrs=attrs)}

    def add_uptime(proc):
        # creates another attribute with the current uptime
        proc['uptime'] = time.time() - proc['create_time']
        return proc

    # add uptime for all process dictionaries
    procs = {p: add_uptime(i) for p, i in procs.items()}

    return procs

def get_whitelisted_procs(proc_dict, proc_names, flag=False):
    """input a list of process names and 
    Return a list of dictionaries of processes, filtered
    from the whole list of running processes
    """
    if flag:
        return proc_dict

    filtered = {p: i for p, i in proc_dict.items() if i['name'] not in proc_names}
    return filtered

def main_loop():
    #1. get all running processes every X seconds
    #2. get every PID for user-selected processes
    #3. check if these PIDS exist every x seconds
    #     dictionary with process names as keys and lists as values
    #4. if PID no longer exists, check for other PIDS with the same name
    #5. if no other PID with same name exists, store the last known value before removing it
    
    new_check_int = 10
    alive_check_int = 2

    #####add here a function that opens a file with tracked processes
    #proc_names = ['chrome.exe', 'explorer.exe', 'cmd.exe' , 'chrome', 'nautilus', 'ONENOTE.EXE', 'MinecraftLauncher.exe']
    proc_names = ['SearchProtocolHost.exe', 'SearchFilterHost.exe']

    while True:
        all_proc_dict = get_all_procs([])
        proc_dict = get_whitelisted_procs(all_proc_dict, proc_names, True)
        print(*proc_dict, sep=', ')
        # proc_dict is a dictionary of dictionaries, with PIDs
        # as keys and dictionaries of attributes as values

        # check processes for specified interval
        sub_iters = int(new_check_int/alive_check_int)
        for i in range(sub_iters):
            time.sleep(alive_check_int)
            print(".")
            # check if any pid has been terminated
            for pid in list(proc_dict.keys()):
                if not psutil.pid_exists(pid):
                    # remove the pid and get its attributes
                    data = proc_dict.pop(pid)
                    print("  ",pid, 'is dead!')
                    proc_name = data['name']

                    # check for other pids with same name. Assume dead
                    for pid_attrs in proc_dict.values():
                        is_kill = True
                        if pid_attrs['name'] == proc_name:
                            print('However,',proc_name,'is still alive!', pid_attrs['pid'])
                            is_kill = False
                            break
                    
                    if is_kill:
                        print(data)
                        with open("output.txt", "a") as f:
                            f.write(str(data)+'\n')

                    
            

if __name__ == '__main__':
    main_loop()