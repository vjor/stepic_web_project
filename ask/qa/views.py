from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 

from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.core.exceptions import  DoesNotExist
from django.http         import Http404 

from django.http import HttpResponseRedirect

from .models import Question,Answer, AskForm, AnswerForm


def test(request, *args, **kwargs):
    return HttpResponse('OK1')


def mainpage(request):
    qs = Question.objects.all()
    qs = qs.order_by('-id')
    limit =  10
    try:
        page = request.GET.get('page', 1)
    except ValueError:
        raise Http404

    paginator = Paginator(qs, limit)
    paginator.baseurl = '/question/'

    try:
	page = paginator.page(page)
    except EmptyPage:
	page = paginator.page(paginator.num_pages)

    return render(request, 'main.html', {
	'qs': 		page.object_list,
	'paginator': paginator, 'page': page,
    })


def pop(request):
    qs = Question.objects.all()
    qs = qs.order_by('-rating')
    limit =  10
    try:
        page = request.GET.get('page', 1)
    except ValueError:
        raise Http404

    paginator = Paginator(qs, limit)
    paginator.baseurl = '/question/'

    try:
	page = paginator.page(page)
    except EmptyPage:
	page = paginator.page(paginator.num_pages)

    return render(request, 'main.html', {
	'qs': 		page.object_list,
	'paginator': paginator, 'page': page,
    })



def qs_ans(request, slug ):

    try:
        qs = Question.objects.get(id=slug)
    except Question.DoesNotExist:
	raise Http404
    ans = Answer.objects.filter(question =qs) 


    return render(request, 'qs_ans.html', {
	'qs': 	qs,
	'ans':	ans,
    })



def qs_add(request):

    if request.method == "POST":
		form = AskForm(request.POST)

		if form.is_valid():
			qspost = form.save()
			#		url = post.get_url()
			url = '/question/%d' %  qspost.pk
	
			return HttpResponseRedirect(url)
			#return HttpResponseRedirect(reverse('/question:results', args=(qspost.id,)))
    else:
		form = AskForm()
		return render(request, 'qs_add.html', {
		'form': form,
		})


def ans_add(request):

    if request.method == "POST":
		form = AnswerForm(request.POST)

		if form.is_valid():
			ans = form.save()
			#		url = post.get_url()
			url = '/question/%d' %  ans.question_id
			#url = '/question/1' 
			return HttpResponseRedirect(url)
			#return HttpResponseRedirect(reverse('/question:results', args=(qspost.id,)))
    else:
		form = AnswerForm()
		return render(request, 'ans_add.html', {
		'form': form,
		})





def paginate(request, qs):
    try:
	limit = int(request.GET.get('limit', 10))
    except ValueError:
	limit = 10
    if limit > 100:
	limit = 10
    try:
	page = int(request.GET.get('page', 1))
    except ValueError:
	raise Http404
    paginator = Paginator(qs, limit)
    try:
	page = paginator.page(page)
    except EmptyPage:
	page = paginator.page(paginator.num_pages)
    return page

