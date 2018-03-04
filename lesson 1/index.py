import webbrowser
import time

total_breaks = 3
break_count = 0
print("this program started on " + time.ctime())
while(break_count < total_breaks):
    time.sleep(2)
    webbrowser.open(
        "https://www.youtube.com/watch?v=b43kxhnPy28&list=PLwyZdDTyvucw5JhBMJxFwsYc1EbQYxr0G&index=17")
    break_count += 1
