with open("test.txt", "r") as file:
    line_count = 0
    for stroka in file:
        line_count +=1
        print(f"символов в {line_count} stroke: {len(stroka)-1}")
        splitted = stroka.split()
        print(f"slov v {line_count} stroke: {len(splitted)}")
print("Vsego strok v file:",line_count)
        