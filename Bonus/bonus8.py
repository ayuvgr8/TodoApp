date = input("Enter date : ")
mood = input("How do  you date your today's mood  from 1 to 10 ?")
thoughts = input("Let your thoughts flow:\n ")

with open(f"../journal/{date}.txt", "w") as file:
    file.write(mood)
    file.write(thoughts)
