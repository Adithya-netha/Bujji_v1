# jarvis.py

import threading
import random
from internet_check import is_Online
from Alert import Alert
from Data.DLG_Data import online_dlg, offline_dlg
from co_brain import Jarvis
from TextToSpeech.Fast_DF_TTS import speak
from Time_Operations.throw_alert import check_schedule, check_Alam
from os import getcwd

Alam_path = r"C:\Users\Admin\Desktop\J.A.R.V.I.S\Alam_data.txt"
file_path = r"C:\Users\Admin\Desktop\J.A.R.V.I.S\schedule.txt"

ran_online_dlg = random.choice(online_dlg)
ran_offline_dlg = random.choice(offline_dlg)

def start_jarvis_logic():
    """ Function to start all jarvis processes asynchronously in separate threads """
    if is_Online():
        t1 = threading.Thread(target=speak, args=(ran_online_dlg,))
        t4 = threading.Thread(target=check_schedule, args=(file_path,))
        t5 = threading.Thread(target=Jarvis)
        t6 = threading.Thread(target=check_Alam, args=(Alam_path,))
        
        # Start the threads
        t1.start()
        t4.start()
        t5.start()
        t6.start()

        # Wait for the threads to finish
        t1.join()
        t4.join()
        t5.join()
        t6.join()
    else:
        Alert(ran_offline_dlg)

start_jarvis_logic()
