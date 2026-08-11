from django.shortcuts import render, redirect
from .models import ExamInfo, UserData, Result
from collections import defaultdict

from django.contrib.auth import authenticate, login




# ---------------- HOME ----------------

def Home(request):
    return render(request, "home.html")


# ---------------- QUESTION PAGES ----------------

def Give_Me_Questioncurd_Page(request):
    return render(request, "question/question_curd.html")


def Give_Me_AddQuestion_Page(request):
    return render(request, "question/add_question.html")


def Give_Me_ViewQuestion_Page(request):
    return render(request, "question/view_question.html")


def Give_Me_UpdateQuestion_Page(request):
    return render(request, "question/update_question.html")


def Give_Me_DeleteQuestion_Page(request):
    return render(request, "question/delete_question.html")




def Give_Me_ShowAllQuestion_Page(request):

    questions = ExamInfo.objects.all().order_by('subject', 'qno')

    subjects = defaultdict(list)

    for q in questions:
        subjects[q.subject].append(q)

    return render(
        request,
        "question/show_all_question.html",
        {
            "subjects": dict(subjects)
        }
    )


# ---------------- QUESTION ACTIONS ----------------

def AddQuestions(request):
    
    try:

        ExamInfo.objects.create(
            qno=request.GET.get("qno"),
            qtext=request.GET.get("qtext"),
            op1=request.GET.get("op1"),
            op2=request.GET.get("op2"),
            op3=request.GET.get("op3"),
            op4=request.GET.get("op4"),
            subject=request.GET.get("subject"),
            ans=request.GET.get("answer")
        )

        msg = "✅ Question Added Successfully"

    except:

        msg = "❌ Question Number Already Exists"

    return render(
        request,
        "question/add_question.html",
        {"msg": msg}
    )


def View_Question(request):
    qno = request.GET.get("qno")

    try:
        data = ExamInfo.objects.get(qno=qno)
        return render(request, "question/view_question.html", {"qdata": data})
    except:
        return render(request, "question/view_question.html",
                    {"msg": "Question Not Found"})


def View_Question_Update(request):
    qno = request.GET.get("qno")

    try:
        data = ExamInfo.objects.get(qno=qno)
        return render(request, "question/update_question.html", {"qdata": data})
    except:
        return render(request, "question/update_question.html",
                    {"msg": "Question Not Found"})


def View_Question_Delete(request):
    qno = request.GET.get("qno")

    try:
        data = ExamInfo.objects.get(qno=qno)
        return render(request, "question/delete_question.html", {"qdata": data})
    except:
        return render(request, "question/delete_question.html",
                {"msg": "Question Not Found"})


def UpdateQuestion(request):
    ExamInfo.objects.filter(
        qno=request.GET.get("qno")
    ).update(
        qtext=request.GET.get("qtext"),
        op1=request.GET.get("op1"),
        op2=request.GET.get("op2"),
        op3=request.GET.get("op3"),
        op4=request.GET.get("op4"),
        subject=request.GET.get("subject"),
        ans=request.GET.get("answer")
    )

    return render(request, "question/update_question.html",
                {"msg": "Question Updated Successfully"})


def DeleteQuestion(request):
    ExamInfo.objects.filter(
        qno=request.GET.get("qno")
    ).delete()

    return render(request, "question/delete_question.html",
                {"msg": "Question Deleted Successfully"})


# ---------------- STUDENT PAGES ----------------

def GiveMeRegisterPage(request):
    return render(request, "student/register.html")


def GiveMeLoginPage(request):
    return render(request, "student/login.html")


def GiveMeStudentCurdPage(request):
    return render(request, "student/student_curd.html")


def GiveMeAddstudentpage(request):
    return render(request, "student/add_student.html")


def GiveMeUpdatestudentpage(request):
    return render(request, "student/update_student.html")


def GiveMeViewstudentpage(request):
    return render(request, "student/view_student.html")


def GiveMeDeletestudentpage(request):
    return render(request, "student/delete_student.html")

def GiveMeScorePage(request):
    return render(request, "result/score.html")


# ---------------- USER ACTIONS ----------------



def Register(request):

    username = request.GET.get("username")
    password = request.GET.get("password")

    if username and password:

        if UserData.objects.filter(username=username).exists():

            return render(
                request,
                "student/register.html",
                {"msg": "Username Already Exists"}
            )

        UserData.objects.create(
            username=username,
            password=password
        )

        return render(
            request,
            "student/register.html",
            {"msg": "Registration Successful"}
        )

    return render(
        request,
        "student/register.html"
    )



def login(request):
    
    username = request.GET.get("username")
    password = request.GET.get("password")

    try:
        user = UserData.objects.get(
            username=username,
            password=password
        )

        request.session["username"] = username

        return redirect('/Examapp/subject/')

    except UserData.DoesNotExist:

        return render(
            request,
            "student/login.html",
            {"msg": "Invalid Username or Password"}
        )


def AddUser(request):
    
    username = request.GET.get("username", "").strip()
    password = request.GET.get("password", "").strip()

    if username == "" or password == "":
        return render(
            request,
            "student/add_student.html",
            {"msg": "Please enter Username and Password"}
        )

    if UserData.objects.filter(username=username).exists():
        return render(
            request,
            "student/add_student.html",
            {"msg": "Username already exists"}
        )

    UserData.objects.create(
        username=username,
        password=password
    )

    return render(
        request,
        "student/add_student.html",
        {"msg": "Student Added Successfully"}
    )


def ShowUser(request):
    
    username = request.GET.get("username")
    udata = None
    msg = ""

    if username:

        try:
            udata = UserData.objects.get(username=username)

        except UserData.DoesNotExist:
            msg = "❌ Student Not Found"

    return render(
        request,
        "student/view_student.html",
        {
            "udata": udata,
            "msg": msg
        }
    )

def UpdateUser(request):
    msg = ""

    if request.GET.get("username"):

        username = request.GET.get("username")
        password = request.GET.get("password")

        try:
            user = UserData.objects.get(username=username)

            user.password = password
            user.save()

            msg = "✅ Student Updated Successfully"

        except UserData.DoesNotExist:

            msg = "❌ Student Not Found"

    return render(
        request,
        "student/update_student.html",
        {"msg": msg}
    )


def DeleteUser(request):
    msg = ""

    if request.GET.get("username"):

        username = request.GET.get("username")

        try:
            user = UserData.objects.get(username=username)
            user.delete()

            msg = "✅ Student Deleted Successfully"

        except UserData.DoesNotExist:

            msg = "❌ Student Not Found"

    return render(
        request,
        "student/delete_student.html",
        {"msg": msg}
    )


def GiveMeShowAllPage(request):
    data = UserData.objects.all()

    return render(request,
                "student/show_all_students.html",
                {"udata": data})


def DeleteUserForShowAllPage(request):
    username = request.GET.get("username")

    UserData.objects.filter(username=username).delete()

    data = UserData.objects.all()

    return render(request,
                "student/show_all_students.html",
                {
                    "udata": data,
                    "msg": "Student Deleted Successfully"
                })


# ---------------- TEST FLOW ----------------

def StartTestPage(request):
    
    subject = request.POST.get("subject")

    questions = list(
        ExamInfo.objects.filter(subject=subject)
    )

    if len(questions) == 0:
        return render(
            request,
            "question/subject.html",
            {"msg": "No Questions Found"}
        )

    request.session["subject"] = subject
    request.session["index"] = 0
    request.session["score"] = 0

    qids = [q.qno for q in questions]
    request.session["qids"] = qids
    print("Username:", request.session.get("username"))
    

    return render(
        request,
        "start_test.html",
        {"question": questions[0]}
    )


def StartTest(request):
    return render(request,
            "start_test.html",
            {"msg": "Login Successful"})
    
    



def NextQuestion(request):
    
    selected = request.GET.get("op")
    correct = request.GET.get("answer")

    score = request.session.get("score", 0)

    if selected == correct:
        score += 1

    request.session["score"] = score

    index = request.session.get("index", 0)
    qids = request.session.get("qids", [])

    index += 1

    if index >= len(qids):
        return End_Test(request)

    request.session["index"] = index

    question = ExamInfo.objects.get(qno=qids[index])

    return render(
        request,
        "start_test.html",
        {"question": question}
    )
def PreviousQuestion(request):
    
    if "index" not in request.session:
        return redirect('/Examapp/subject/')

    index = request.session["index"]

    if index > 0:
        index -= 1

    request.session["index"] = index

    qids = request.session["qids"]

    question = ExamInfo.objects.get(
        qno=qids[index]
    )
    
    print("PREVIOUS")
    print(dict(request.session))

    return render(
        request,
        "start_test.html",
        {"question": question}
    )

def End_Test(request):
    
    username = request.session.get("username")
    subject = request.session.get("subject")
    score = request.session.get("score")

    try:
        user = UserData.objects.get(
            username=username
        )

        Result.objects.create(
            username=user,
            subject=subject,
            marks=score
        )

    except:
        pass

    return render(
        request,
        "result/score.html",
        {
            "finalscore": score,
            "subject": subject
        }
    )
    
def ScorePage(request):
    
    username = request.session.get("username")

    if not username:
        return render(
            request,
            "result/score.html"
        )

    try:

        user = UserData.objects.get(
            username=username
        )

        result = Result.objects.filter(
            username=user
        ).last()

        return render(
            request,
            "result/score.html",
            {"result": result}
        )

    except:
        return render(
            request,
            "result/score.html",
            {"msg": "No Result Found"}
        )


# ---------------- RESULT ----------------

def GetAllResultPage(request):
    data = Result.objects.all()
    return render(request, "result/result.html", {"rdb": data})


# ---------------- LOGOUT ----------------

def LogoutUser(request):
    request.session.flush()
    return redirect('/Examapp/')

def ShowAllUsers(request):
    data = UserData.objects.all()
    return render(request, "student/show_all_students.html", {"udata": data})

def SubjectPage(request):
    subjects = ExamInfo.objects.values_list(
        'subject',
        flat=True
    ).distinct()

    return render(
        request,
        "question/subject.html",
        {"subjects": subjects}
    )
