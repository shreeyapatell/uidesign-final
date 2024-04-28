from flask import Flask, render_template, request, redirect, url_for, jsonify
app = Flask(__name__)
from random import randint

quiz_res = []

lessons= {
    "1": {"lesson_id": "1",
    "title": "Learn to sign \"Here\"",
    "video": "/static/files/here.mp4",
    "text": "To sign \"here\", open your palms and lay them flat in front of your stomach with palms facing up. Create an outward circular motion with both hands at the same time.",
    "next_lesson": "2",
    "prev_lesson": "beg"
    },
    "2": {"lesson_id": "2",
    "title": "Learn to sign \"Turn Left\"",
    "video": "/static/files/left.mp4",
    "text": "To sign \"turn left\", extend your left hand's thumb and pointer finger while keeping the rest of your hand closed. Point your thumb towards you and your pointer finger towards the sky. Then, turn your hand to the left.",
    "next_lesson": "3",
    "prev_lesson": "1"
    },
     "3": {"lesson_id": "3",
    "title": "Learn to sign \"Turn Right\"",
    "video": "/static/files/right.mp4",
    "text": "To sign \"turn right\", extend your right hand's index and middle finger, twist them together, and point them to the sky. Have your palm facing towards you. Then, move your right hand to the right so your palm faces forward.", 
    "next_lesson": "4",
    "prev_lesson": "2"
    },
     "4": {"lesson_id": "4",
    "title": "Learn to sign \"Behind\"",
    "video": "/static/files/behind.mp4",
    "text": "To sign \"behind\", create two fists, one with each hand. Place one fist behind the other, almost like you're hitting the back of one fist with the other.",
    "next_lesson": "5",
    "prev_lesson": "3"
    },
    "5": {"lesson_id": "5",
    "title": "Learn to sign \"Go Forward\"",
    "video": "/static/files/proceed.mp4",
    "text": "To sign \"go forward\", on both hands, keep your palms facing towards you, with the fingers together and facing each other. Move both hands in a forward motion.",
    "next_lesson": "end",
    "prev_lesson": "4"
    }
}

#Still need to add more quiz questions
quiz_questions = {
    "1": {"quiz_id": "1",
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
        "title": "What is the sign for \"Here\"",
        "video1": "/static/files/left.mp4",
        "video2": "/static/files/here.mp4",
        "video3": "/static/files/proceed.mp4",
        "correct_answer": "/static/files/here.mp4", 
        "next_q": "end",
        "prev_q": "2"
    }
}

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
        # process submitted quiz answers
        selected_answer = request.form.get('video')
        user_responses = {quiz_id: selected_answer}
        quiz_res.append(user_responses)  # Store the user responses
        
        # redirect to quiz results page if it's the last question
        if question["next_q"] == "end":
            score_percentage = calculate_score(quiz_res)
            return render_template('quiz_results.html', score_percentage=score_percentage)
        
        # render the next question
        next_question_id = question["next_q"]
        next_question = quiz_questions.get(next_question_id)
        if not next_question:
            return "Next question not found", 404
        return render_template('quiz.html', question=next_question)
            
    return render_template('quiz.html', question=question)

def calculate_score(quiz_res):
    total_questions = len(quiz_res)
    total_correct = sum(1 for responses in quiz_res for question_id, user_response in responses.items() if user_response == quiz_questions[question_id]["correct_answer"])
    score_percentage = (total_correct / total_questions) * 100
    return score_percentage


if __name__ == '__main__':
    app.run(debug=True)