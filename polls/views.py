from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Choice, Question, Etc
from django.urls import reverse
from django.views import generic
from django.contrib import messages


# class IndexView(generic.ListView):
#     template_name = 'polls/index.html'
#     context_object_name = 'latest_question_list'
#
#     def get_queryset(self):
#         return Question.objects.order_by('-pub_date')[:5]
#
#
# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'
#
#
#
# class ResultsView(generic.DetailView):
#     model = Question
#     template_name = 'polls/results.html'

# def Results(request, question_id):
#     questions=get_object_or_404(Question, pk=question_id)
#     Etc_FIl = Etc.objects.filter(question_id=question_id).order_by('-count')
#     return render(request, 'polls/results.html',{'question':questions, 'Etc_FIl': Etc_FIl})

def index(request):
   latest_question_list = Question.objects.order_by('-pub_date')[:5]
   context = {'latest_question_list': latest_question_list}
   return render(request, 'polls/index.html', context)
def detail(request, question_id):
   question = get_object_or_404(Question, pk=question_id)
   return render(request, 'polls/detail.html', {'question': question})
def results(request, question_id):
   questions = get_object_or_404(Question, pk=question_id)
   Etcs_orderby = Etc.objects.filter(question_etc_id=question_id).order_by('-count')
   return render(request, 'polls/results.html', {'question': questions, 'Etcs_orderby': Etcs_orderby})



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # selected_choice = question.choice_set.get
    # messages.add_message(request, messages.INFO, request.POST.getlist('choice'))

    Etc_count = ' '
    selected_choice_list = request.POST.getlist('choice')
    try:
        for choice_list_re in selected_choice_list:
            selected_choice = question.choice_set.get(pk=choice_list_re)
            selected_choice.votes += 1
            selected_choice.save()

    except(ValueError):
        if(choice_list_re !=''):
            #   Choice.objects.create(choice_text=choice_list_re, votes=1, question_id=question_id)
            for etc_list in Etc.objects.filter(question_etc_id=question_id).order_by('-count'):
                if(choice_list_re == str(etc_list)):
                    Etc_count = Etc.objects.get(question_etc_id=question_id , Etc_text=choice_list_re)
                    Etc_count.count += 1
                    Etc_count.save()
                    break
            if(choice_list_re != str(Etc_count)):
                Etc.objects.create(Etc_text=choice_list_re, count=1, question_etc_id=question_id)
        else:
            return render(request, 'polls/detail.html',{
                'question': question,
                'error_message': "You didn't select a choice",
            })

    except(KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't only number ",
        })

    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))



    # ETC_FIL=Etc.objects.filter(question_etc_id=question_id).order_by('count')
    # render(request, 'polls/results.html', ETC_FIL)


# def index(request):
#     latest_question_list=Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list' : latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))
#
# def details(request,question_id):
#     try:
#         return HttpResponse("You're looking at question %s. " % question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})
#
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html',{'question': question})
#
# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except(KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html',{
#             'question' : question,
#             'error_message':"You didn't select a choice",
#         })
#     else:
#         selected_choice.votes +=1
#         selected_choice.save()
#     return HttpResponseRedirect(reverse("polls:results " , args = (question_id)))


# return render(request, 'polls/detail.html', {
#     'question': question,
#     'error_message': "You didn't select a choice",
# })


 # for choice_list_re in selected_choice_list:
        #     he = question.choice_set.all()
        #     jur = len(question.choice_set.all())
        #     for list_number in range(1, len(question.choice_set.all())+1):
        #         if (choice_list_re == str(list_number)):
        #             selected_choice = question.choice_set.get(pk=choice_list_re)
        #             selected_choice.votes += 1
        #             selected_choice.save()
        #             break