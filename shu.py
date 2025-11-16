print("☁️  Loading Shu!")

import os
import sys
import time 

print("☁️  Shu Loaded!")

if __name__ == "__main__":
    # Clearing terminal for clarity
    if sys.platform in ('linux', 'darwin'):
        os.system('clear')
    elif sys.platform == 'win32':
        os.system('cls')
    else:
        print('⚠️  Unable to clear terminal!')

    print("☁️  Running Shu!")

    # Initialize variables
    start_time = time.time()
    elapsed_time = 0
    print("\n> 🕑  Start (UNIX): {:.0f}".format(start_time)) 
    max_time = 5
    time_step = 1/10 

    # Main loop
    while elapsed_time < max_time:
        time.sleep(time_step)
        current_time = time.time()
        elapsed_time = current_time - start_time
        print("\r> ⏳  Elapsed time: {:.1f}s".format(elapsed_time), end='')

    # Exiting
    print("\n> 🕓  Finish (UNIX): {:.0f}".format(current_time))
    print("\n☁️  Exiting Shu!")
    sys.exit()
