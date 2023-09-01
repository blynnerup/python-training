def find_and_replace(file_name, word_to_replace, replacement_word):
    with open(file_name, encoding="utf8", mode="r+") as file:
        file_contents = file.read()
        new_file_content = file_contents.replace(word_to_replace, replacement_word)
        file.seek(0)
        file.write(new_file_content)

print(find_and_replace("story_alteration_copy.txt", "Alice", "Louise"))