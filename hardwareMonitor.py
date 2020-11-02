#in order for this to work you need to have Open Hardware Monitor running
import wmi
import time
w = wmi.WMI(namespace="root\OpenHardwareMonitor")
sensors = w.Sensor()
while True:
    for sensor in sensors:
    
        if sensor.Parent=='/amdcpu/0' and sensor.Name=='CPU Package' and sensor.SensorType == 'Temperature':
            print(sensor.Name, sensor.SensorType, sensor.Value)
    
        elif sensor.Parent=='/atigpu/0' and sensor.Name=='GPU Core' and sensor.SensorType == 'Temperature':
            print(sensor.Name, sensor.SensorType, sensor.Value)
    print('______________________________________________________\n')
    time.sleep(5)    
        
    