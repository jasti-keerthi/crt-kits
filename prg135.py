resume = input("Enter resume text: ")

start = resume.find("SKILLS:")

if start == -1:
    print("Skills Section Not Found")
else:
    skills_text = resume[start + len("SKILLS:"):]

    end = skills_text.find("EDUCATION:")

    if end != -1:
        skills = skills_text[:end].strip()
    else:
        skills = skills_text.strip()

    print("Skills:", skills)