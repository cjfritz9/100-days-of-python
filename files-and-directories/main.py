# with open("snake_db.txt") as snake_db:
#   entries = snake_db.read()
#   print(entries)

with open("new_file.txt", "w") as snake_db:
  snake_db.write("New File Contents")