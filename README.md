# WordClock-Python2.7

Update software
      sudo apt-get update
	

Install necessary packets
      sudo apt-get install gcc make build-essential python-dev git scons swig
      sudo reboot
	
  
installing Python 3.6 on Raspberry PI
     sudo apt-get install python3.6
     ln -s /usr/bin/python3.6 /usr/bin/python
     


ws2812 lib install
     git clone https://github.com/jgarff/rpi_ws281x
     cd rpi_ws281x/
     sudo scons
     cd python
     sudo python setup.py build
     sudo python setup.py install
     
