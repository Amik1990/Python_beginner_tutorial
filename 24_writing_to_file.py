#  "a" - append umožní přidat další řádek.   .write - přidá řádek do dokumentu. Když spustím podruhé, tak se zase přidá do dokumentu
scratch_file = open("scratch.txt", "a")
scratch_file.write("Nissan - Japan")
scratch_file.close()

# \n pčidá text na druhý řádek
scratch_file = open("scratch.txt", "a")
scratch_file.write("\nSeat - Spain")
scratch_file.close()

# "w" overwrite. Přepíše celý dokument a zůstane nový text
scratch_file = open("scratch.txt", "w")
scratch_file.write("\nSeat - Spain")
scratch_file.close()

# Vtvoří nový dokument scratch2
scratch_file = open("scratch2.txt", "w")
scratch_file.write("\nSeat - Spain")
scratch_file.close()
