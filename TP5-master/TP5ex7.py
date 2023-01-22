def LastEdit():
    import os
    from datetime import datetime

    file1 = input("Entrez le nom du premier fichier : ")
    file2 = input("Entrez le nom du second fichier : ")

    if os.path.isfile(file1):
        file1_size = os.path.getsize(file1)
        file1_time = os.path.getmtime(file1)
        print(
            f"Le fichier {file1} existe, sa taille est de {file1_size} octets, et sa dernière modification était le {datetime.fromtimestamp(file1_time)}")
    else:
        print(f"Le fichier {file1} n'existe pas.")

    if os.path.isfile(file2):
        file2_size = os.path.getsize(file2)
        file2_time = os.path.getmtime(file2)
        print(
            f"Le fichier {file2} existe, sa taille est de {file2_size} octets, et sa dernière modification était le {datetime.fromtimestamp(file2_time)}")
    else:
        print(f"Le fichier {file2} n'existe pas.")
LastEdit()
