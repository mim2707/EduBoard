import json
import random

def generate_university_data(num_universities):
    universities = []
    for i in range(num_universities):
        university = {
            "name": f"University {chr(65 + i)}",
            "min_IELTS": round(random.uniform(6.5, 8.5), 1),
            "max_IELTS": round(random.uniform(8.5, 9.0), 1),
            "min_TOEFL": random.randint(80, 110),
            "max_TOEFL": random.randint(110, 120),
            "min_GMAT": random.randint(600, 750),
            "max_GMAT": random.randint(750, 800),
            "min_GRE": random.randint(300, 330),
            "max_GRE": random.randint(330, 340)
        }
        universities.append(university)
    return universities

def save_to_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

num_universities = 100

university_data = generate_university_data(num_universities)

file_path = 'university_data.json'

save_to_json(university_data, file_path)

print("Data has been saved successfully in JSON file", file_path)