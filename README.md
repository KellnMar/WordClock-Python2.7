For "raspberry zero w" with python2.7

Update software

      sudo apt-get update
      
Install necessary packets

      sudo apt-get install gcc make build-essential python-dev git scons swig
      sudo reboot

ws2812 lib install

      sudo apt-get update
      git clone https://github.com/jgarff/rpi_ws281x
      cd rpi_ws281x/
      sudo scons
      cd python
      sudo python setup.py build
      sudo python setup.py install
