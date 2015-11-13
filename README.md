___Computer:___
Thingspeak: #CHANNEL1
	1. mysql -u thing -p #[pass: speak]
	2. cd thingspeak && rails server
	3. python3 fetch_csv_thingspeak.py #for Fetch .csv file to computer
Phant: #Random Value from Notebook
	1. phant
	2. python3 phant_pc.py #run Python server Phant
	3. python3 fetch_csv_phant.py #for Fetch .csv file to computer

___Arduino:___
Thingspeak: #CHANNEL2
	1. mysql -u thing -p #[pass: speak]
	2. cd thingspeak && rails server

Phant: #Random Value from Arduino
	1. phant
	2. python3 phant_arduino.py #run Python server Phant 
				    #[NEED TO REFRACTIORING]

