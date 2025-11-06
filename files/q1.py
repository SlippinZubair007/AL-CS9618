#Write a code that reads data from a file

file="file1.txt"
try:
  with open(file,"r") as f:
    for line in f:
      print(f"{line.strip()}")
    print("File found!\n")
except Exception as e:
  print(f"Error thrown:{e}")