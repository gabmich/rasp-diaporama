import os, time, subprocess
from datetime import datetime

def now():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

DAYS_FR = {
    1:'lundi',
    2:'mardi',
    3:'mercredi',
    4:'jeudi',
    5:'vendredi',
    6:'samedi',
    7:'dimanche',
}

# application base directory
BASE_DIR = os.path.dirname(os.path.realpath(__file__))

NOW = datetime.now()
# get current weekday name in french
CURRENT_WEEKDAY = DAYS_FR[NOW.isoweekday()]
# get dir with same name of 'CURRENT_WEEKDAY'
TARGET_DIR = f"{BASE_DIR}/{CURRENT_WEEKDAY}"

print('CURRENT WEEKDAY :', CURRENT_WEEKDAY)
print('TARGET DIR :', TARGET_DIR)

# change this value if you want the script to run a shorter / longer amount of time. Here, 10 minutes
TOTAL_DISPLAY_DURATION = 600 # in seconds
# get a list of all images in TARGET_DIR (assuming there are only images in it...)
IMAGES_LIST = os.listdir(TARGET_DIR)

# each image will be displayed the same duration
IMAGE_DISPLAY_DURATION = round(TOTAL_DISPLAY_DURATION/len(IMAGES_LIST))

print('IMAGES LIST LENGTH:', len(IMAGES_LIST))
print('EACH IMAGE DISPLAY DURATION:', IMAGE_DISPLAY_DURATION)

# we force the display to wake up
subprocess.Popen("export DISPLAY=:0.0; xset dpms force on", shell=True)
# we set the screen standby/suspend/off timers to 600 seconds
subprocess.Popen("export DISPLAY=:0.0; xset dpms 600 600 600", shell=True)

for IMAGE in IMAGES_LIST:
    # for each image in IMAGES_LIST, we open it with 'eog' software and display it fullscreen
    image_path = f"{TARGET_DIR}/{IMAGE}"
    print(now(), 'IMAGE PATH :', image_path)

    command    = f"""export DISPLAY=:0.0; eog -w --fullscreen -f "{image_path}" &"""
    subprocess.Popen(command, shell=True)
    # sleep n seconds, until continuing to the next image
    time.sleep(IMAGE_DISPLAY_DURATION)

# kill all pkill instances
subprocess.Popen("pkill eog", shell=True)
time.sleep(2)

# force Raspberry to standby at the end
subprocess.Popen("export DISPLAY=:0.0; xset dpms force standby", shell=True)
