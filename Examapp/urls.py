from django.urls import path
from . import views

urlpatterns = [

    # ================= HOME =================
    path('', views.Home, name='home'),

    # ================= QUESTION CRUD =================
    path('givemequestioncurd/', views.Give_Me_Questioncurd_Page),
    path('giveaddquestion/', views.Give_Me_AddQuestion_Page),
    path('giveviewquestion/', views.Give_Me_ViewQuestion_Page),
    path('giveupdatequestion/', views.Give_Me_UpdateQuestion_Page),
    path('givedeletequestion/', views.Give_Me_DeleteQuestion_Page),
    path('givemeshowallquestion/', views.Give_Me_ShowAllQuestion_Page),

    path('addquestion/', views.AddQuestions),
    path('viewquestion/', views.View_Question),
    path('updatequestion/', views.UpdateQuestion),
    path('deletequestion/', views.DeleteQuestion),

    path('viewquestionupdate/', views.View_Question_Update),
    path('viewquestiondelete/', views.View_Question_Delete),

    # ================= TEST FLOW =================
    path('starttestpage/', views.StartTestPage),
    path('nextquestion/', views.NextQuestion),
    path('previousquestion/', views.PreviousQuestion),
    path('endtest/', views.End_Test),

    # ================= STUDENT =================
    path('givemeregister/', views.GiveMeRegisterPage),
    path('givemelogin/', views.GiveMeLoginPage),
    path('givemestudentcurd/', views.GiveMeStudentCurdPage),

    path('givemeaddstudent/', views.GiveMeAddstudentpage),
    path('givemeupdatestudent/', views.GiveMeUpdatestudentpage),
    path('givemeviewstudent/', views.GiveMeViewstudentpage),
    path('givemedeletestudent/', views.GiveMeDeletestudentpage),
    path('givemescorepage/', views.GiveMeScorePage), 

    path('register/', views.Register),
    path('login/', views.login),

    path('addstudent/', views.AddUser),
    path('showstudent/', views.ShowUser),
    path('updatestudent/', views.UpdateUser),
    path('deletestudent/', views.DeleteUser),

    path('showallstudent/', views.ShowAllUsers),
    path('deleteusershowall/', views.DeleteUserForShowAllPage),

    # ================= RESULT =================
    path('getallresultpage/', views.GetAllResultPage),

    # ================= LOGOUT =================
    path('logoutuser/', views.LogoutUser),
    path('subject/', views.SubjectPage),
    path('score/', views.ScorePage),
]