from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import *
from submit.models import Submit
from problem.forms import UploadFileForm
from os import system

# Create your views here.

def check_solution(sol, problem, user):
    out_file = "check/" + str(user.id) + ".out"
    system("python3 " + str(sol) + " < " + str(problem.test_in) + " > " + out_file)
    out = open(out_file, "r")
    ans = open(str(problem.test_out), "r")
    return out.readline() == ans.readline()

def problem(request, problem_id):
    verdict = ""
    problem = get_object_or_404(Problem, pk=problem_id)

    #REDIRECT IF NOT AUTHENTIFICATED
    if (not request.user.is_authenticated()):
        return redirect('/admin/')
    #SUBMIT BUTTON PRESSED, CHECK SOLUTION
    if (request.method == "POST"):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            submit = Submit(sol=file, verdict="", user=request.user)
            submit.save()
            if (check_solution(submit.sol, problem, request.user)):
                verdict = "ACCEPTED, GOOD JOB!"
            else:
                verdict = "WRONG ANSWER, TRY AGAIN.."
            submit.verdict = verdict
            submit.save()
    return render(request, 'problem/problem.html', {'problem':problem,
                                                    'verdict':verdict,
                                                    })