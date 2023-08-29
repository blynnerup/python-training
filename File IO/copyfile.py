def copy(src, dst):
    with open(src, encoding="utf8") as src:
        with open(dst, "a", encoding="utf8") as dst:
            for line in src:
                dst.write(line)

copy("story.txt", "story_copy.txt")

def copy_and_reverse(source, dest):
    with open(source, encoding="utf8") as story:
        with open(dest, "w", encoding="utf8") as story_reversed:
            story_reversed.write(story.read()[::-1])