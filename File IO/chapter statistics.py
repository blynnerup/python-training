def statistics(file_name):
    with open("story.txt", encoding="utf8") as file:
        data = file.readlines()
        return {
            "lines": len(data),
            "words": sum(len(line.split(" ")) for line in data),
            "characters": sum(len(line) for line in data)
        }
    
print(statistics("story.txt"))