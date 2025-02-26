import random

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, UserScore


def index(request):
    return render(request, 'qstable/index.html')


@login_required
def start_quiz(request):

    if "ready" not in request.session:
        request.session["ready"] = True
        return render(request, "qstable/ready.html")

    # reset session
    if "reset" in request.GET:
        request.session["answered_questions"] = []
        request.session["correct_answers"] = 0
        request.session["current_question"] = None

    answered_questions = request.session.get("answered_questions", [])
    correct_answers = request.session.get("correct_answers", 0)

    unanswered_questions = Question.objects.exclude(id__in=answered_questions)


    if not unanswered_questions:
        return render(request, "qstable/quiz_complete.html", {"correct_answers": correct_answers})

    feedback = None
    if request.method == "POST":
        current_question_id = request.session.get("current_question")
        if not current_question_id:
            return redirect("index")

        current_question = get_object_or_404(Question, id=current_question_id)

        selected_choice_id = request.POST.get("choice")
        if not selected_choice_id:
            feedback = "You must select an answer."
        else:
            selected_choice = get_object_or_404(current_question.choices, id=selected_choice_id)

            answered_questions.append(current_question.id)
            request.session["answered_questions"] = answered_questions

            if selected_choice.is_correct:
                correct_answers += 1
                request.session["correct_answers"] = correct_answers
                user_score, created = UserScore.objects.get_or_create(user=request.user)
                user_score.correct_answers += 1
                user_score.save()

            feedback = "Correct!" if selected_choice.is_correct else "Wrong!"

        return redirect("start_quiz")

    # random logic
    question = random.choice(unanswered_questions)
    request.session["current_question"] = question.id
    choices = list(question.choices.all())
    random.shuffle(choices)

    return render(request, "qstable/start_quiz.html", {
        "question": question,
        "choices": choices,
        "feedback": feedback,
        "correct_answers": correct_answers,
    })


def leaderboard_view(request):
    leaderboard = UserScore.objects.all().order_by('-correct_answers')

    return render(request, 'qstable/leaderboard.html', {'leaderboard': leaderboard})


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'qstable/login.html', {'error': 'Invalid credentials'})
    return render(request, 'qstable/login.html')


def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():
                return render(request, 'qstable/signup.html', {'error': 'Username already exists'})
            user = User.objects.create_user(username=username, password=password)
            user.save()
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'qstable/signup.html', {'error': 'Passwords do not match'})
    return render(request, 'qstable/signup.html')


def question_view(request, question_id):
    question = get_object_or_404(Question, id=question_id)

    if request.method == "POST":
        selected_choice_id = request.POST.get("answer")
        if selected_choice_id:
            selected_choice = question.choices.get(id=selected_choice_id)
            if selected_choice.is_correct:
                return render(request, "qstable/correct.html")
            else:
                return render(request, "qstable/incorrect.html")

    return render(request, "qstable/question_page.html", {"question": question})