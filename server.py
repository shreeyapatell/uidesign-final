from flask import Flask, render_template, request, redirect, url_for, jsonify
app = Flask(__name__)
from random import randint



lessons= {
    "1": {"lesson_id": "1",
    "title": "Learn to sign \"Here\" ",
    "video": "https://www.youtube.com/embed/2dALbgMQWmk?si=Lg7LalBfsJB9BdOU",
    "text": "To sign here, open your palms and lay them flat in front of your stomach with palms facing up. Create an outward circular motion with both hands at the same time",
    "next_lesson": "2",
    "prev_lesson": "beg"
    },
    "2": {"lesson_id": "2",
    "title": "Learn to sign \"Turn Left\"",
    "video": "https://www.youtube.com/embed/NJbkr3BerEU?si=McXm3adcEVxfoakx",
    "text": "To sign \"turn left\", extend your left hand's thumb and pointer finger while keeping the rest of your hand closed. Point your thumb towards you and your pointer finger towards the sky. Then, turn your hand to the left.",
    "next_lesson": "3",
    "prev_lesson": "1"
    },
     "3": {"lesson_id": "3",
    "title": "Learn to sign \"Turn Right\"",
    "video": "https://www.youtube.com/embed/dxe-_tQXqC0?si=iL5D65tJfuKZ1yfV",
    "text": "To sign \"turn right\", extend your right hand's index and middle finger, twist them together, and point them to the sky. Have your palm facing towards you. Then, move your right hand to the right so your palm faces forward.", 
    "next_lesson": "4",
    "prev_lesson": "2"
    },
     "4": {"lesson_id": "4",
    "title": "Learn to sign \"Behind\"",
    "video": "https://www.youtube.com/embed/VoetY5cF1Oo?si=m4omJGl_KJk_wUao",
    "text": "To sign \"behind\", create two fists, one with each hand. Place one fist behind the other, almost like you're hitting the back of one fist with the other.",
    "next_lesson": "5",
    "prev_lesson": "3"
    },
    "5": {"lesson_id": "5",
    "title": "Learn to sign \"Go Forward\"",
    "video": "https://www.youtube.com/embed/bsYCP5SEHSk?si=ucJd7EDJxQHm6A9Q",
    "text": "To sign \"go forward\", on both hands, extend all fingers and keep them together. Keep your palms facing towards you, and move both hands in a forward motion.",
    "next_lesson": "end",
    "prev_lesson": "4"
    }
}

#Still need to add more quiz questions
quiz_questions = {
    "1": {"quiz_id": "1",
    "title": "What is the sign for \"Behind\" ",
    "video1": "https://www.youtube.com/embed/NJbkr3BerEU?si=McXm3adcEVxfoakx",
    "video2": "https://www.youtube.com/embed/VoetY5cF1Oo?si=m4omJGl_KJk_wUao",
    "video3": "https://www.youtube.com/embed/bsYCP5SEHSk?si=ucJd7EDJxQHm6A9Q",
    "correct_answer": "question.video2",
    "next_q": "2",
    "prev_q": "beg"
    },
    "2": {
        "quiz_id": "2",
        "title": "What is the sign for \"Right\"",
        "video1": "https://www.youtube.com/embed/VoetY5cF1Oo?si=Xcvr84frYjrnyXRo",
        "video2": "https://www.youtube.com/embed/rVE_TKIclps?si=bwHg9Q2Es8s4uH5G",
        "video3": "https://www.youtube.com/embed/0nq-8ZTXrFo?si=KlR82HUW6y5H70eT",
        "correct_answer": "question.video3",
        "next_q": "3",
        "prev_q": "1"
    },
    "3": {
        "quiz_id": "3",
        "title": "What is the sign for \"Here\"",
        "video1": "https://www.youtube.com/embed/rVE_TKIclps?si=t7pu1oFYsP6turCy",
        "video2": "https://www.youtube.com/embed/2dALbgMQWmk?si=LSCFAD5jdV8bznOw",
        "video3": "https://www.youtube.com/embed/NH2cqOYnQYY?si=PAVMxWhO-8-6SnSf",
        "correct_answer": "question.video2",
        "next_q": "end",
        "prev_q": "2"
    }
}


# Routes
@app.route('/')
def layout():
    return render_template('layout.html')

@app.route('/learn/<lesson_id>')
def learn(lesson_id):
    lesson=lessons[lesson_id]
    return render_template('learn.html', lesson=lesson)


@app.route('/quiz/<quiz_id>', methods=['GET', 'POST'])
def quiz(quiz_id):
    question = quiz_questions.get(quiz_id)
    if not question:
        return "Question not found", 404
    
    if request.method == 'POST':
        # Process submitted quiz answers
        selected_answer = request.form.get('selected_answer')
        user_responses = {quiz_id: selected_answer}
        score_percentage = calculate_score(user_responses)
        return render_template('quiz_results.html', score_percentage=score_percentage)
    
    return render_template('quiz.html', question=question)


def calculate_score(user_responses):
    total_questions = len(user_responses)
    total_correct = sum(1 for question_id, user_response in user_responses.items() if user_response == quiz_questions[question_id]["correct_answer"])
    score_percentage = (total_correct / total_questions) * 100
    return score_percentage




if __name__ == '__main__':
    app.run(debug=True)