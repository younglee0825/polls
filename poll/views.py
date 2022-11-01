from django.shortcuts import render, get_object_or_404
from .models import Question,Choice
from django.template import loader
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views import generic


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'poll/index.html'
    context_object_name = 'latest_question_list'

    """Return the last five published questions."""
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'poll/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'poll/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = request.POST.getlist('choice')
        print(selected_choice)
    except(KeyError, Choice.DoesNotExit):
     return render(request, 'poll/detail.html', {'question':question,
                                                        'error_message': "You didn't select a choice." })
    else:
        for i in selected_choice:
            selection = question.choice_set.get(pk=i)
            selection.votes+=1
            selection.save()
            print(selection)
        return HttpResponseRedirect(reverse('results', args=(question.id,)))