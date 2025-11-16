import os
import sys
import time 

print("☁️  Running Shu!")

if __name__ == "__main__":
    print("🧪 Running Shu Test!")

    start_time = time.time()
    print("\n> 🕑  Start (UNIX): {:.0f}".format(start_time))
    current_time = time.time()
    elapsed_time = current_time - start_time
    time_step = 1/2

    while elapsed_time < 10:
        time.sleep(time_step)
        current_time = time.time()
        elapsed_time = current_time - start_time
        print("\r> ⏳  Elapsed Time (seconds): {:.1f}s".format(elapsed_time), end='')

    print("\n> 🕓  Finish (UNIX): {:.0f}".format(current_time))
        

print("\n☁️  Exiting Shu!")
sys.exit()
    