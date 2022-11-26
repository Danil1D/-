import numpy as np
import matplotlib.pyplot as plt 
from scipy.interpolate import interp1d
from colorama import Fore


speed = [25, 35, 45, 30, 60, 120, 100, 100, 70, 75, 80, 65] #1
time = np.linspace(0,11,12,endpoint=True,dtype=int)


print( Fore.CYAN + "\n#2  " + Fore.GREEN + "Time: ", time)         #2


fig, ax = plt.subplots() #3
plt.xlabel("Time")
plt.ylabel("Speed")
plt.title( "#3")
plt.plot(time, speed, color = "red")
ax.grid()
plt.xticks(time)
plt.yticks(np.arange(0, 140, 10))
plt.show()


inter = interp1d(time, speed, kind="cubic")  #4
time2 = np.linspace(0, 11, 10000)
speed2 = inter(time2)
plt.plot(time2, speed2)
plt.plot(time, speed, "s")
plt.title( "#4")
ax.grid()
plt.xlabel("Time")
plt.ylabel("Speed")
plt.xticks(time)
plt.yticks(np.arange(0, 140, 10))
plt.show ()


dst = np.trapz(speed2, time2)  #5
print(Fore.CYAN + "#5  " + Fore.GREEN + f"Distance: {int(dst)} км")


inter = interp1d(time, speed, kind="quadratic")  #6
time2 = np.linspace(0, 11, 10000)
speed2 = inter(time2)
plt.plot(time2, speed2)
plt.plot(time, speed, "s")
plt.title( "#6")
ax.grid()
plt.xlabel("Time")
plt.ylabel("Speed")
plt.xticks(time)
plt.yticks(np.arange(0, 140, 10))
plt.show ()

dst = np.trapz(speed2, time2)  
print(Fore.CYAN + "#6  " + Fore.GREEN + f"Distance: {int(dst)} км")


