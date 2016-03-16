from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse 

from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
#from django.core.exceptions import  DoesNotExist
from django.http         import Http404 

from django.http import HttpResponseRedirect

from .models import Question,Answer
from .forms  import  AskForm, AnswerForm, SignForm, LoginForm
from django.contrib.auth import authenticate, login

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
		form._user = request.user

		if form.is_valid():
			qspost = form.save()
			#		url = post.get_url()
			url = '/question/%d' %  qspost.pk
	
			return HttpResponseRedirect(url)
		else:
			return HttpResponseRedirect('/login/%s' %form._user)
    else:
		form = AskForm("")
		return render(request, 'qs_add.html', {
		'form': form,
		})


def ans_add(request):

    if request.method == "POST":
	form = AnswerForm(request.POST)
        form._user = request.user

	if form.is_valid():
		ans = form.save()
		#		url = post.get_url()
		url = '/question/%d/' %  ans.question_id
		#url = '/question/2/' 
		return HttpResponseRedirect(url)
		#return HttpResponseRedirect(reverse('/question:results', args=(qspost.id,)))
    else:
	form = AnswerForm("")
	return render(request, 'ans_add.html', {
	'form': form,
	})

def sign_add(request):

    if request.method == "POST":
	form = SignForm(request.POST)

	if form.is_valid():
		ss=form.save()
		url = '/' 
		return HttpResponseRedirect(url)
    else:
	form = SignForm()
	return render(request, 'form_reg.html', {
	'form': form,
	})

def login11(request):

    if request.method == "POST":
	username = request.POST.get('username')
	password = request.POST.get('password')
	url = request.POST.get('continue', '/')
	sessid = do_login(username, password)
	if sessid:
	    response = HttpResponseRedirect(url)
	    response.set_cookie('sessid', sessid,
		domain='localhost', httponly=True,
		expires = datetime.now()+timedelta(days=5)
		)
	    return response
	else:
	    error = 'error login/pass'
    else:
	form = LoginForm()
	return render(request, 'form_login.html', {
	'form': form,
	})

def do_login(login, password):
    try:
	user = User.objects.get(login=login)
    except User.DoesNotExist:
	return None
    hashed_pass = salt_and_hash(password)
    if user.password != hashed_pass:
	return None
    session = Session()
    session.key = generate_long_random_key()
    session.user = user
    session.expires = datetime.now() + timedelta(days=5)
    session.save()
    return session.key



def my_login(request):

    if request.method == "POST":
	form = LoginForm(request.POST)
        username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)

#	user= form.get_user()
        if user is not None:
    	    if user.is_active:
    		login(request, user)
	
		return HttpResponseRedirect('/')
	else:
		form.username="11"
		return HttpResponseRedirect('/login/%s' %username )
    else:
	form = LoginForm()
	return render(request, 'form_login.html', {
	'form': form,
	})


def my_login1(request):
     
        username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
    	    if user.is_active:
        	login(request, user)
		return HttpResponseRedirect('/')
            # Redirect to a success page.
    	    else:
        	print(" Return a 'disabled account' error message")
            
	else:
    	    print(" Return an 'invalid login' error message.")

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

