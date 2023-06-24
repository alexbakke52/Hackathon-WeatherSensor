# Hackathon-WeatherSensor
Portable weather hyperlocal weather sensor that will ping (send a notification to) your phone given certain weather changes.
For instance if it's about to rain, air quality has lowered, change in humidity etc.

# Several possible applications:

-IoT/Smart Home 
    - You're drying your clothes on a drying rack outside, but it's started to rain and now your clothes are wet. Avoid this issue by having a device that detects the rain
    - It's about to rain and you have windows open
    
-Portable weather warner - You're on a trip and dressed for sunny weather, suddenly it starts to rain, and you had no idea. Now you'll get a notification beforehand, and be prepared


# Problems (Cajus)
- Trying to program in qt, serialport inclusion too hard (might not work on ArchLinux)
  ## What I learned from that
  - seek all the help you can get first, before spending hours on (possibly) impossible solutions
  - compare different languages and programs before jumping into one

# ToDo
- seperate temperature and pressure DONE
- plot temp & pressure DONE
- algorithm for rain/weather prediction DONE
- include plot into tkinter DONE
- android app WIP
- make tkinter nice looking IN PROGRESS
- IoT instead of USB WIP
      - make app for android/ios prob not happening
      - cloud database? how does iot actually work? wtf


# for later
- no feasible way to measure wind direction, it would have to be web scraped (like altitude is done)
