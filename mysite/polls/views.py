from django.http import Http404
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question, Rating

def index(request):
    return render(request, 'polls/index.html')

def search(request):
    if request.method == "POST":
        query = request.POST.get("question")
        try:
            question = Question.objects.get(question_text__icontains=query)
            return render(request, "polls/outcome.html", {"item": question, "question": question})
        except Question.DoesNotExist:
            return render(request, "polls/outcome.html", {"item": None})
'''
def search(request, question_id):
    latest_question_list = Question.objects.order_by("-pub_date")
    question = get_object_or_404(Question, pk=question_id)
    for item in latest_question_list:
        if item == question:
            context = {"item": item, "question": question}

            return render(request, "polls/outcome.html", context)
'''

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def add_rating(request, question_id):
    if request.method == "POST":
        question = get_object_or_404(Question, pk=question_id)
        

        rating_text = request.POST.get("rating_str")
        
        if rating_text:
            Rating.objects.create(question=question, rating_str=rating_text, votes=0)

        return HttpResponseRedirect(reverse("polls:detail", args=(question.id,)))
    else:
        return HttpResponseRedirect(reverse("polls:detail", args=(question.id,)))

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))

def outcome(request, question_id):
    latest_question_list = Question.objects.order_by("-pub_date")
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/outcome.html", context)
