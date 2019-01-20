# Outcognito
Hack N' Roll 2019 Project.

_Ported over to public repo._

Idea: Door enhancement with additional functionalities (**opening detection**)

Logical Flow:

1. Raspberry Pi camera detects movement (while loop w short delay and comparison w past images?) *(use milk volume code for reference)*
2. Sends alert via SSH to device (laptop).
3. Launch screenguard.
4. Different screenguards depending on priority assigned.
    * Minimize Window 
    * Reduce Display Brightness
    * Open Random Resource Site


Possible enhancements:
* Arduino interfacing (LED lights up when motion is detected)
* Proper GUI to change the combined script
* Additional screenguards (lowered brightness, random educational website)

