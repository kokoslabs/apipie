#from apipie import main
'''from apipie import main

main("config.json", is_string=False)'''
import multiprocessing
import psutil
import time
import os

# --- Configuration ---
CPU_LIMIT_PERCENT = 30.0  # Percentage
MEMORY_LIMIT_MB = 100.0   # Megabytes
TIME_LIMIT_SECONDS = 10   # Total runtime limit

def execute_user_code(code_str):
    """
    A simple wrapper to execute the user's code string.
    This function will be the target for the new process.
    """
    try:
        # A slightly safer environment for exec
        safe_globals = {
            "__builtins__": __builtins__, # Provides standard built-ins like print, len, etc.
            "time": time
        }
        exec(code_str, safe_globals)
    except Exception as e:
        print(f"User code raised an exception: {e}")

def run_sandboxed(code_str):
    """
    Runs user code in an isolated process and monitors its resource usage.
    Terminates the process if it exceeds the defined limits.
    """
    # Create a new process to run the user code
    child_process = multiprocessing.Process(target=execute_user_code, args=(code_str,))
    child_process.start()
    print(f"Started user code in process with PID: {child_process.pid}")

    # Get a handle on the child process for monitoring
    try:
        p = psutil.Process(child_process.pid)
    except psutil.NoSuchProcess:
        print("Could not find the child process immediately after start.")
        child_process.join()
        return

    start_time = time.time()
    
    # Monitoring loop
    while child_process.is_alive():
        # 1. Time Limit Check
        if time.time() - start_time > TIME_LIMIT_SECONDS:
            print(f"TIME LIMIT EXCEEDED ({TIME_LIMIT_SECONDS}s). Terminating process.")
            p.terminate()
            break

        try:
            # 2. Memory Limit Check (RSS is a good general metric)
            mem_usage = p.memory_info().rss / (1024 * 1024) # in MB
            if mem_usage > MEMORY_LIMIT_MB:
                print(f"MEMORY LIMIT EXCEEDED ({mem_usage:.2f}MB > {MEMORY_LIMIT_MB}MB). Terminating process.")
                p.terminate()
                break

            # 3. CPU Limit Check
            # interval=0.1 means it's a non-blocking check comparing against the last call.
            cpu_usage = p.cpu_percent(interval=0.1)
            if cpu_usage > CPU_LIMIT_PERCENT:
                print(f"CPU LIMIT EXCEEDED ({cpu_usage:.2f}% > {CPU_LIMIT_PERCENT}%). Terminating process.")
                p.terminate()
                break
        
        except psutil.NoSuchProcess:
            # The process finished on its own before a limit was hit
            break
        except Exception as e:
            print(f"An error occurred during monitoring: {e}")
            p.terminate()
            break
            
        time.sleep(0.5) # Check resources twice a second

    # Wait for the process to terminate and clean up
    child_process.join(timeout=2)
    if child_process.is_alive():
        print("Process did not terminate gracefully, killing it.")
        child_process.kill() # Force kill if terminate didn't work
    
    print("Monitoring finished.")


# --- Example Usage ---
# This code will be stopped once it allocates ~100MB of memory.
user_code = """
print('hello world')
'''import time
print("User code started...")
data = []
try:
    while True:
        # Each string is ~10MB
        data.append(" " * 10_000_000)
        allocated_mb = len(data) * 10
        print(f"Allocated: {allocated_mb} MB")
        time.sleep(0.2)
except Exception as e:
    print(f"User code stopped with: {e}")'''
"""

if __name__ == '__main__':
    run_sandboxed(user_code)