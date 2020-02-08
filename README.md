# controlOscilloscope
Control tektronix osciloscope with pyvisa in linux.
# usage guidelines
Replace line #7 with your device details as below :

rm.open_resource('USB0::{Vendor ID}::{Model ID}::{Serial Number}::INSTR')
To get device details run findID.py 

If you get a timeout error, follow the given steps.
After connecting the tektronix oscilloscope : 
$sudo chmod a+w /dev/usbtmc0
$sudo echo "*IDN?" > /dev/usbtmc0

# tekmeasure
  measures the values and outputs the plot of Freq vs Vrms
  
# teklive
  this will output the live plot
