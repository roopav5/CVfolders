import winsound
import time

# Function to play the alarm sound
def play_alarm():
    for _ in range(5):
        winsound.Beep(440, 500)

# Function to play the snooze sound
def play_snooze():
    winsound.Beep(440, 550)

# Function to handle snooze
def handle_snooze():
    snooze_count = 0
    while snooze_count < 3:
        print("Press 'S' for Snooze or 'C' to stop:")
        choice = input().upper()
        if choice == 'C':
            break
        elif choice == 'S':
            print("Snoozing...")
            time.sleep(180)  # Snooze for 3 minutes
            play_alarm()  # Ring the alarm again after snooze
            snooze_count += 1
    if snooze_count == 3:
        print("Three snooze attempts exhausted.")

# Set alarm time
alarm_hour = 5
alarm_minute = 30

# Main loop
while True:
    current_time = time.localtime()
    print("Table top - alarm clock")
    print("Set alarm: {} : {}".format(alarm_hour, alarm_minute))
    print("Current time: {} : {}".format(current_time.tm_hour, current_time.tm_min))
    
    # Check if it's time for the alarm
    if current_time.tm_hour == alarm_hour and current_time.tm_min == alarm_minute:
        print("Alarm ringing...")
        play_alarm()
        handle_snooze()
        break
    
    # Wait for a minute before checking again
    time.sleep(60)
