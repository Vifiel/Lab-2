import pandas as pd
import random as rd

data = pd.read_csv("books-en.csv", header=0, encoding="latin-1", on_bad_lines="skip", sep =";")
xml_data = pd.read_xml("currency.xml", encoding="cp1251")
names = []
values = []
count = 0
s_author = input("Enter author: ")
border = 9388
start = rd.randint(0, 9388)
end = start + 20
file = open("Library_List.txt", "x")


if __name__ == "__main__":

    #Task1
    
    for name in data["Book-Title"]:
        count += 1 if len(name) >= 30 else 0

    print(f"\nTask 1 answer: {count}\n")
    

    #Task2
    
    print("Answer for Task 2, all the books of " + s_author + " before 2016:" + "\n")
    for author, name, date in zip(data["Book-Author"], data["Book-Title"], data["Year-Of-Publication"]):
        if author == s_author and int(date) < 2016:
            print(f"{name} - {author}, {date}")

    #Task 3
    print(f"\nAnswer for Task 3 books with numbers from {start} to {end-1}:")
    for num, (author, name, date) in enumerate(list(zip(data["Book-Author"], data["Book-Title"], data["Year-Of-Publication"]))):
        if start <= num < end:
            link = f"{author}. {name} - {date}"
            print(str(num) + " " + link)
            file.write(f"{num} link\n")
    
    #Task 4

    for name, value in zip(xml_data["Name"], xml_data["Value"]):
        names.append(name)
        values.append(value)
    print(f"Answer for Task 4: \n Names: {names} \n \nValues: {values}\n")

    #Additional Task

    print(f"All the publishers without duplicates: {list(set(data['Publisher']))}\n")
    
    book_rating = list(zip(data["Downloads"], data["Book-Title"]))
    book_rating.sort(key=lambda x: x[0])
    print("Top20 Books:")
    [print(i[1]) for i in book_rating[-20:]]



