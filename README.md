# RaspberyPi
My Team's Repository for the IEA Rapsbery Pi Competitions

After the Arab Spring, especially the ongoing conflict in Syria, over 4.6 million Syrians have become refugees, with nearly half of them being children. A main issue with such mass displacements is the continuation of children’s education after leaving their homes due to conflict. In fact, international organizations such as UNICEF and UNHCR have made it their goal to provide refugee children with this education. However, given the uncertainty of these children’s circumstances and the unpredictability of camp life, it may be difficult for such organizations to properly monitor the regularity of these refugees receiving an education. 

MANARA, an attachable Bluetooth emitting plastic token, is a product providing easier methods of monitoring the comings and goings, as well as the overall attendance of refugee children seeking educational benefits. Its functionality is based on the use of Bluetooth 4.0 (Low Energy), online servers (google Firebase), MANARA beacons (Bluetooth Emitters) and the Raspberry Pi (Receiver).

By integrating Bluetooth with the Raspberry Pi, MANARA was able to detect incoming Bluetooth Devices (Beacons) and was able to compare the detected devices with registered ones on a private server (Google Firebase), filtering out the devices not present on the server. It was then able to log the comings and goings of registered devices within the vicinity and with further development could send the logs to a database for further data analysis by international organizations. This may provide easier methods of managing the refugee students and may help these organizations in the management of student transportation, division of students among facilities, and fund allocation.

We chose MANARA as the product name because a MANARA, or lighthouse, is a guide for ships in hard times which provides an easier path for them to take to reach safety. We wish our product to help organizations similarly, and to be a source of benefit when monitoring the refugee children’s education.

The file is named Project.py, and it works as follows:.

-The pi detects bluetooth addresses of devices in the vicinity

-It then checks if the devices are registered in a Google Firebase server

-If they are, it proceeds to save them in a csv (excel) file on the pi for future reference.


