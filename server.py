from flask import Flask, render_template, request, redirect, url_for, jsonify
app = Flask(__name__)
from random import randint

quiz_res = []

lessons= {
    "1": {"lesson_id": "1",
    "unit": 1,
    "num": 1,
    "title": "Learn to sign \"Here\"",
    "video": "/static/files/here.mp4",
    "text": "To sign \"here\", open your palms and lay them flat in front of your stomach with palms facing up. Create an outward circular motion with both hands at the same time.",
    "next_lesson": "2",
    "prev_lesson": "beg"
    },
    "2": {"lesson_id": "2",
    "unit": 1,
    "num": 2,
    "title": "Learn to sign \"Turn Left\"",
    "video": "/static/files/left.mp4",
    "text": "To sign \"turn left\", extend your left hand's thumb and pointer finger while keeping the rest of your hand closed. Point your thumb towards you and your pointer finger towards the sky. Then, turn your hand to the left.",
    "next_lesson": "3",
    "prev_lesson": "1"
    },
     "3": {"lesson_id": "3",
    "unit": 1,
    "num": 3,
    "title": "Learn to sign \"Turn Right\"",
    "video": "/static/files/right.mp4",
    "text": "To sign \"turn right\", twist your right hand's index and middle finger together, and point them to the sky. Have your palm facing towards you. Then, twist your right hand to the right so your palm faces forward.", 
    "next_lesson": "4",
    "prev_lesson": "2"
    },
     "4": {"lesson_id": "4",
    "unit": 1,
    "num": 4,
    "title": "Learn to sign \"Behind\"",
    "video": "/static/files/behind.mp4",
    "text": "To sign \"behind\", create two fists, one with each hand. Place one fist behind the other, almost like you're hitting the back of one fist with the other.",
    "next_lesson": "5",
    "prev_lesson": "3"
    },
    "5": {"lesson_id": "5",
    "unit": 1,
    "num": 5,
    "title": "Learn to sign \"Go Forward\"",
    "video": "/static/files/proceed.mp4",
    "text": "To sign \"go forward\", on both hands, keep your palms facing towards you, with the fingers together and facing each other. Move both hands in a forward motion.",
    "next_lesson": "end",
    "prev_lesson": "4"
    },
    "6": {"lesson_id": "6",
    "unit": 2,
    "num": 1,
    "title": "Learn to sign \"Gate\"",
    "video": "/static/files/gate.mp4",
    "text": "To sign \"gate\", extend your index and middle fingers together, hold your hand at chest height with palm facing inward, and make a small horizontal swinging motion to simulate opening a gate.",
    "next_lesson": "7",
    "prev_lesson": "beg"
    },
    "7": {"lesson_id": "7",
    "unit": 2,
    "num": 2,
    "title": "Learn to sign \"Traffic\"",
    "video": "/static/files/traffic.mp4",
    "text": "To sign \"traffic\", extend both hands in front of you with palms facing each other and fingers spread, then move them back and forth alternately, mimicking the flow of vehicles in traffic.",
    "next_lesson": "8",
    "prev_lesson": "6"
    },
    "8": {"lesson_id": "8",
    "unit": 2,
    "num": 3,
    "title": "Learn to sign \"Door\"",
    "video": "/static/files/door.mp4",
    "text": "To sign \"door\" , use your dominant hand to mimic the action of opening and closing a door by forming a \"C\" shape with your fingers and thumb and moving your hand as if opening a door.",
    "next_lesson": "9",
    "prev_lesson": "7"
    },
    "9": {"lesson_id": "9",
    "unit": 2,
    "num": 4,
    "title": "Learn to sign \"Road\"",
    "video": "/static/files/road.mp4",
    "text": "To sign \"road\", extend both hands in front of you with palms facing down and fingers spread, then move them forward in a smooth motion, representing the path or surface of a road.",
    "next_lesson": "end2",
    "prev_lesson": "8"
    }
}

#Still need to add more quiz questions
quiz_questions = {
    "1": {"quiz_id": "1",
    "unit": 1,
    "num": 1,
    "title": "What is the sign for \"Behind\" ",
    "video1": "/static/files/left.mp4",
    "video2": "/static/files/behind.mp4",
    "video3": "/static/files/proceed.mp4",
    "correct_answer": "/static/files/behind.mp4",
    "next_q": "2",
    "prev_q": "beg"
    },
    "2": {
        "quiz_id": "2",
        "unit": 1,
        "num": 2,
        "title": "What is the sign for \"Right\"",
        "video1": "/static/files/behind.mp4",
        "video2": "/static/files/left.mp4",
        "video3": "/static/files/right.mp4",
        "correct_answer": "/static/files/right.mp4",
        "next_q": "3",
        "prev_q": "1"
    },
    "3": {
        "quiz_id": "3",
        "unit": 1,
        "num": 3,
        "title": "What is the sign for \"Here\"",
        "video1": "/static/files/left.mp4",
        "video2": "/static/files/here.mp4",
        "video3": "/static/files/proceed.mp4",
        "correct_answer": "/static/files/here.mp4", 
        "next_q": "end",
        "prev_q": "2"
    },
    "4": {
        "quiz_id": "4",
        "unit": 2,
        "num": 1,
        "title": "What is the sign for \"Gate\"",
        "video1": "/static/files/door.mp4",
        "video2": "/static/files/traffic.mp4",
        "video3": "/static/files/gate.mp4",
        "correct_answer": "/static/files/gate.mp4", 
        "next_q": "5",
        "prev_q": "beg"
    },
    "5": {
        "quiz_id": "5",
        "unit": 2,
        "num": 2,
        "title": "What is the sign for \"Traffic\"",
        "video1": "/static/files/gate.mp4",
        "video2": "/static/files/road.mp4",
        "video3": "/static/files/traffic.mp4",
        "correct_answer": "/static/files/traffic.mp4", 
        "next_q": "6",
        "prev_q": "4"
    },
    "6": {
        "quiz_id": "6",
        "unit": 2,
        "num": 3,
        "title": "What is the sign for \"Door\"",
        "video1": "/static/files/gate.mp4",
        "video2": "/static/files/door.mp4",
        "video3": "/static/files/traffic.mp4",
        "correct_answer": "/static/files/door.mp4", 
        "next_q": "7",
        "prev_q": "5"
    },
    "7": {
        "quiz_id": "7",
        "unit": 2,
        "num": 4,
        "title": "What is the sign for \"Road\"",
        "video1": "/static/files/road.mp4",
        "video2": "/static/files/gate.mp4",
        "video3": "/static/files/traffic.mp4",
        "correct_answer": "/static/files/road.mp4", 
        "next_q": "end",
        "prev_q": "6"
    }

    
}

def quiz_questions_generator():
    generated_questions = []
    selected_ids = set()
    while len(generated_questions) < 3:
        random_num = randint(1, 7)
        if random_num not in selected_ids:
            selected_ids.add(random_num)
            generated_questions.append(quiz_questions[str(random_num)])
    return generated_questions

# Routes
@app.route('/')
def layout():
    return render_template('layout.html')

import datetime

@app.route('/learn/<lesson_id>')
def learn(lesson_id):
    lesson = lessons[lesson_id]
    
    # Calculate progress
    total_lessons = len(lessons)
    current_lesson_index = int(lesson_id)
    progress = (current_lesson_index / total_lessons) * 100
    lesson['progress'] = progress
    
    # Add start time
    lesson['start_time'] = datetime.datetime.now().strftime("%B %d, %Y %I:%M %p")
    
    return render_template('learn.html', lesson=lesson)


@app.route('/quiz/<quiz_id>', methods=['GET', 'POST'])
def quiz(quiz_id):
    global quiz_res

    question = quiz_questions.get(quiz_id)
    if not question:
        return "Question not found", 404
    
    if request.method == 'POST':
        # Process submitted quiz answers
        selected_answer = request.form.get('video')
        user_responses = {quiz_id: selected_answer}
        quiz_res.append(user_responses)  # Store the user responses
        
        if "prev_button" in request.form:  # If the "Back" button was clicked
            prev_question_id = question["prev_q"]
            prev_question = quiz_questions.get(prev_question_id)
            if not prev_question:
                return "Previous question not found", 404
            return render_template('quiz.html', question=prev_question)
        
        # Redirect to quiz results page if it's the last question
        if question["next_q"] == "end":
            score_percentage = calculate_score(quiz_res)
            correct_answers, incorrect_answers = user_answers(quiz_res)
            quiz_res = []
            return render_template('quiz_results.html', 
                                   score_percentage=score_percentage, 
                                   correct_answers=correct_answers,
                                   incorrect_answers=incorrect_answers,
                                   quiz_id=quiz_id)
        
        # Render the next question
        next_question_id = question["next_q"]
        next_question = quiz_questions.get(next_question_id)
        if not next_question:
            return "Next question not found", 404
        return render_template('quiz.html', question=next_question)
            
    return render_template('quiz.html', question=question)


@app.route('/final_quiz', methods=['GET'])
def final_quiz():
    questions = quiz_questions_generator()
    return render_template('final_quiz.html', questions=questions)

@app.route('/final_quiz/submit', methods=['POST'])
def submit_final_quiz():
    global quiz_res

    # Retrieve the question IDs and selected answers from the form
    question_ids = request.form.getlist('question_id')
    selected_answers = request.form.getlist('video')

    # Store the user responses as a list of dictionaries
    user_responses = [{question_id: selected_answer} for question_id, selected_answer in zip(question_ids, selected_answers)]
    quiz_res.extend(user_responses)  # Append the user responses to the quiz_res list

    print(user_responses)
    print(quiz_res)

    correct_answers, incorrect_answers = user_answers(quiz_res)
    print("correct: ", correct_answers)
    print("incorrect: ", incorrect_answers)

    # If all questions are answered, calculate the score
    score_percentage = calculate_score(quiz_res)
    print(score_percentage)
    quiz_res = []  # Reset quiz responses
    return render_template('final_quiz_results.html', 
                           score_percentage=score_percentage, 
                           correct_answers=correct_answers, 
                           incorrect_answers=incorrect_answers)

def calculate_score(quiz_res):
    total_questions = len(quiz_res)
    total_correct = sum(1 for responses in quiz_res for question_id, user_response in responses.items() if user_response == quiz_questions[question_id]["correct_answer"])
    print(total_correct)
    for responses in quiz_res:
        for question_id, user_response in responses.items():
            print("Question ID:", question_id)
            print("User response:", user_response)
            print("Correct answer:", quiz_questions[question_id]["correct_answer"])
    score_percentage = round(((total_correct / total_questions) * 100), 1)
    return score_percentage

def user_answers(quiz_res):
    correct_answers = []
    incorrect_answers = []
    for responses in quiz_res:
        for question_id, user_response in responses.items():
            if user_response == quiz_questions[question_id]["correct_answer"]:
                correct_answers.append(quiz_questions[question_id])
            else: 
                incorrect_answers.append(quiz_questions[question_id])
    return correct_answers, incorrect_answers


if __name__ == '__main__':
    app.run(debug=True)