# Outcognito
Hack N' Roll 2019 Project. Published at: https://devpost.com/software/outcognito

_Ported over to public repo._

Idea: Door enhancement with additional functionalities (**opening detection**)

Logical Flow:

1. Raspberry Pi camera detects movement
2. Sends alert via SSH to device (laptop).
3. Launch screenguard.
4. Different screenguards depending on priority assigned.
    * Minimize Window 
    * Reduce Display Brightness
    * Open Random Resource Site


Possible enhancements:
* Arduino interfacing (LED lights up when motion is detected)
* Proper GUI to change the combined script
