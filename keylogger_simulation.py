#Keystroke Logging Simulation
#Purpose: Security awareness & learning
#Environment: Local Machine, user consent

log_file="keystrokes_log.txt"
print(" === Keystroke Logging Simulation ===")
print("Type something and press ENTER.")
user_input=input("< ")
with open(log_file,"a") as file:
     file.write(user_input + "\n")

print("\n Input Captured and saved locally.")   
print(f"Log File: {log_file}")
