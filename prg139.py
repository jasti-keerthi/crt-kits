title = input("Enter title: ")
slug = title.lower().strip().replace(" ", "-")
slug = "".join(c for c in slug if c.isalnum() or c == "-")
print(slug.strip("-"))