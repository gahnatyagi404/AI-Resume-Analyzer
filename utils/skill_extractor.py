import json
import os


def load_skills():
    """
    Load skills from the skills.json file.
    """

    project_root = os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))
    )

    skills_path = os.path.join(
        project_root,
        "data",
        "skills.json"
    )

    with open(
        skills_path,
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


def extract_skills(text):
    """
    Find skills present in the given text.
    """

    skills_data = load_skills()

    text = text.lower()

    found_skills = []

    for category, skills in skills_data.items():

        for skill in skills:

            if skill.lower() in text:

                found_skills.append(skill)

    return sorted(set(found_skills))