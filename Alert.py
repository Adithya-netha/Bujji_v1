import os
from winotify import Notification, audio

def Alert(Text):
    icon_path = r"C:\Users\chatu\OneDrive\Desktop\Jarvis\logo.png"

    # Create a notification
    toast = Notification(
        app_id="🟢 J.A.R.V.I.S.",
        title=Text,
        msg="",  
        duration="short",
        icon=icon_path
    )

    toast.set_audio(audio.Default, loop=False)

    toast.add_actions(label="Click me", launch="https://www.google.com")
    toast.add_actions(label="Dismiss", launch="")

    toast.show()
Alert("hello iam jarvis")