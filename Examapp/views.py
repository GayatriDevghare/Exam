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
    
    if request.method == "POST":

        qno = request.POST.get("qno")
        qtext = request.POST.get("qtext")
        op1 = request.POST.get("op1")
        op2 = request.POST.get("op2")
        op3 = request.POST.get("op3")
        op4 = request.POST.get("op4")
        subject = request.POST.get("subject")
        ans = request.POST.get("ans")

        # Check duplicate question number

        if ExamInfo.objects.filter(qno=qno).exists():

            return render(
                request,
                "question/add_question.html",
                {
                    "msg": f"Question number {qno} already exists."
                }
            )

        ExamInfo.objects.create(
            qno=qno,
            qtext=qtext,
            op1=op1,
            op2=op2,
            op3=op3,
            op4=op4,
            subject=subject,
            ans=ans
        )

        return redirect("show_all_question_page")

    return render(
        request,
        "question/add_question.html"
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
    
    if request.method == "POST":

        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        if not username or not password:

            return render(
                request,
                "student/register.html",
                {
                    "msg": "Username and password are required."
                }
            )

        if UserData.objects.filter(
            username=username
        ).exists():

            return render(
                request,
                "student/register.html",
                {
                    "msg": "Username already exists."
                }
            )

        UserData.objects.create(
            username=username,
            password=password
        )

        return render(
            request,
            "student/login.html",
            {
                "msg": "Registration successful. Please login."
            }
        )

    return render(
        request,
        "student/register.html"
    )

def login(request):
    
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        try:
            user = UserData.objects.get(
                username=username,
                password=password
            )

            request.session["username"] = username

            print("Login successful:", username)

            # Go to subject selection page
            return redirect("start_test_page")

        except UserData.DoesNotExist:

            return render(
                request,
                "student/login.html",
                {
                    "msg": "Invalid username or password"
                }
            )

    return render(
        request,
        "student/login.html"
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

def StartTestPage(request):
    return render(
        request,
        "question/start_test_page.html"
    )
# ---------------- TEST FLOW ----------------
# def StartTestPage(request):
    
#     # ==============================
#     # STEP 1: SHOW SUBJECT PAGE
#     # ==============================
#     if request.method == "GET":

#         return render(
#             request,
#             "start_test.html"
#         )

#     # ==============================
#     # STEP 2: SUBJECT SELECTED
#     # ==============================
#     if request.method == "POST":

#         subject = request.POST.get("subject")

#         print("Selected Subject:", subject)
#         print("Username:", request.session.get("username"))

#         if not subject:
#             return render(
#                 request,
#                 "start_test.html",
#                 {
#                     "msg": "Please select a subject."
#                 }
#             )

#         questions = list(
#             ExamInfo.objects.filter(subject=subject)
#         )

#         if not questions:

#             return render(
#                 request,
#                 "start_test.html",
#                 {
#                     "msg": f"No questions found for {subject}."
#                 }
#             )

#         # Save exam information in session
#         request.session["subject"] = subject
#         request.session["index"] = 0
#         request.session["score"] = 0

#         qids = [q.qno for q in questions]

#         request.session["qids"] = qids

#         # First question
#         return render(
#             request,
#             "question/start_question.html",
#             {
#                 "question": questions[0]
#             }
#         )


def StartTest(request):
    
    if request.method == "POST":

        subject = request.POST.get("subject")

        questions = ExamInfo.objects.filter(
            subject=subject
        ).order_by("qno")

        qids = list(
            questions.values_list("qno", flat=True)
        )

        request.session["subject"] = subject
        request.session["qids"] = qids
        request.session["index"] = 0
        request.session["score"] = 0

        if not qids:
            return render(
                request,
                "question/start_test_page.html",
                {
                    "msg": "No questions available for this subject."
                }
            )

        question = ExamInfo.objects.get(qno=qids[0])

        return render(
            request,
            "start_test.html",
            {
                "question": question,
                "index": 0,
                "total": len(qids),
            }
        )
def NextQuestion(request):
    
    qids = request.session.get("qids", [])
    index = request.session.get("index", 0)
    score = request.session.get("score", 0)

    # Save answer
    if request.method == "POST":

        selected_answer = request.POST.get("answer")

        answer_map = {
            "1": "op1",
            "2": "op2",
            "3": "op3",
            "4": "op4",
        }

        selected_option = answer_map.get(selected_answer)

        question = ExamInfo.objects.get(qno=qids[index])

        print("Selected Answer:", selected_answer)
        print("Selected Option:", selected_option)
        print("Correct Answer:", question.ans)

        if selected_option == question.ans:
            score += 1
            print("Answer Correct")
        else:
            print("Answer Wrong")

        request.session["score"] = score

    # Move to next question
    index += 1
    request.session["index"] = index

    # No more questions
    if index >= len(qids):
        return redirect("end_test")

    question = ExamInfo.objects.get(qno=qids[index])

    return render(
        request,
        "start_test.html",
        {
            "question": question,
            "index": index,
            "total": len(qids),
        }
    )
    
def PreviousQuestion(request):
    
    qids = request.session.get("qids", [])
    index = request.session.get("index", 0)

    if not qids:
        return redirect("start_test_page")

    index -= 1

    if index < 0:
        index = 0

    request.session["index"] = index

    qno = qids[index]

    try:

        question = ExamInfo.objects.get(
            qno=qno
        )

    except ExamInfo.DoesNotExist:

        return redirect("start_test_page")

    return render(
        request,
        "start_test.html",
        {
            "question": question
        }
    )
    
def End_Test(request):
    
    username = request.session.get("username")
    subject = request.session.get("subject")
    score = request.session.get("score", 0)

    print("Username:", username)
    print("Subject:", subject)
    print("Score:", score)

    if username and subject:

        try:
            user = UserData.objects.get(username=username)

            Result.objects.create(
                username=user,
                subject=subject,
                marks=score
            )

        except UserData.DoesNotExist:
            pass

    # Clear exam session
    request.session.pop("qids", None)
    request.session.pop("index", None)
    request.session.pop("score", None)
    request.session.pop("subject", None)

    return render(
        request,
        "result/score.html",
        {
            "score": score,
            "subject": subject
        }
    )
    
def ScorePage(request):
    
    username = request.session.get("username")

    if not username:

        return render(
            request,
            "result/score.html",
            {
                "msg": "Please login first."
            }
        )

    try:

        user = UserData.objects.get(
            username=username
        )

        result = (
            Result.objects
            .filter(username=user)
            .order_by("-id")
            .first()
        )

        return render(
            request,
            "result/score.html",
            {
                "result": result
            }
        )

    except UserData.DoesNotExist:

        return render(
            request,
            "result/score.html",
            {
                "msg": "No Result Found"
            }
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

    return render(
        request,
        "student/show_all_students.html",
        {"udata": data}
    )
