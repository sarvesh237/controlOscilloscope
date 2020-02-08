import visa
import numpy as np
import time
import matplotlib.pyplot as plt

rm = visa.ResourceManager('@py')
#print(rm.list_resources())
scope = rm.open_resource('USB0::1689::872::C038299::0::INSTR')
scope.write('*rst')
scope.write('autoset execute')
time.sleep(10)

scope.write("MEASUrement:MEAS1:SOURCE CH1")
scope.write("MEASUrement:MEAS1:TYPE FREQuency")
scope.write("MEASUrement:MEAS1:STATE ON")

scope.write("MEASUrement:MEAS2:SOURCE CH1")
scope.write("MEASUrement:MEAS2:TYPE CRMS")
scope.write("MEASUrement:MEAS2:STATE ON")
time.sleep(10)
plt.ion()
fig = plt.figure()
ax = fig.add_subplot(111)

def ploti():    
    plt.scatter(rms, frequency) 
    plt.show()
    plt.pause(0.01)
    plt.clf()
    fig.canvas.draw()

frequency,rms = [],[]
for i in range(2000):
    a = scope.query('measurement:meas1:value?')
    b = scope.query('measurement:meas2:value?')
    time.sleep(0.000001)
    frequency.append(float(a[:len(a)-1]))
    rms.append(float(b[:len(b)-1]))
    ploti()
    print(frequency[i],rms[i])
