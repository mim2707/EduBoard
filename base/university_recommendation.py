import json
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import logging


def load_university_data(file_path):
    logger = logging.getLogger(__name__)
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            university_data = json.load(file)
        logger.info("File uploaded: %s", file_path)
        return university_data
    except FileNotFoundError:
        logger.error("File not found: %s", file_path)
        raise
    except Exception as e:
        logger.error("Error while uploading file %s: %s",
                     file_path, str(e))
        raise


def input_student_scores():
    ielts = float(input("Enter your IELTS score: "))
    toefl = float(input("Enter your TOEFL score: "))
    gmat = float(input("Enter your GMAT score: "))
    gre = float(input("Enter your GRE score: "))
    return np.array([ielts, toefl, gmat, gre]).reshape(1, -1)


def train_model(X, y):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model


def predict_university(student_scores, model, universities):
    predicted_university = model.predict(student_scores)
    return universities[predicted_university[0]]


def main():
    while True:

        universities_data = load_university_data('university_data.json')
        universities = {i: university['name']
                        for i, university in enumerate(universities_data)}

        X = np.array([list(university.values())[1:5]
                     for university in universities_data])
        y = np.array(list(universities.keys()))

        student_scores = input_student_scores()

        model = train_model(X, y)

        recommended_university = predict_university(
            student_scores, model, universities)
        print("Recommended University for you:", recommended_university)

        continue_input = input("Do you wish to continue? (yes/no): ")
        if continue_input.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
