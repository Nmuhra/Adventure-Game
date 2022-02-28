print("Welcome to Numanji!")

character = input("choose your character (Nabegh, John Danaher, Ted):\n").lower()

if character == "nabegh":
  print("you are the leader of the group")
  weapon = input("pick your weapon (Sword, Bow, Heel Hook):\n").lower()
  if weapon == "heel hook":
    print("Great choice!")
  else:
    print(f"your weapon is a {weapon}")
if character == "john danaher":
  print("you are the master mind of the group")
  weapon = input("pick your weapon (Sword, triangle, Heel Hook):\n").lower()
  if weapon == "heel hook":
    print("Great choice!")
  else:
    print(f"your weapon is a {weapon}")
if character == "ted":
  print("you are useless, just try to stay alive")
  weapon = input("pick your weapon (stick, Bow, hammer):\n").lower()
  if weapon == "hammer":
    print("Great choice!")
  else:
    print(f"your weapon is a {weapon}")

choice = input("you are being chased by chimpanzees, you can either fight or drive off:\n").lower()

if choice == "fight":
  print("John Danaher strangled two chimpanzees, however, he got outnumbered and killed")
  print("Game Over")
if choice == "drive off":
  print("you managed to escape, however, Ted is injured")

