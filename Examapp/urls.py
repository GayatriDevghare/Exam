from django.urls import path
from . import views


urlpatterns = [

    # ==================================================
    # HOME
    # ==================================================

    path(
        "",
        views.Home,
        name="home"
    ),


    # ==================================================
    # QUESTION CRUD PAGES
    # ==================================================

    path(
        "questioncurd/",
        views.Give_Me_Questioncurd_Page,
        name="question_curd"
    ),

    path(
        "addquestion/",
        views.Give_Me_AddQuestion_Page,
        name="add_question_page"
    ),

    path(
        "viewquestion/",
        views.Give_Me_ViewQuestion_Page,
        name="view_question_page"
    ),

    path(
        "updatequestion/",
        views.Give_Me_UpdateQuestion_Page,
        name="update_question_page"
    ),

    path(
        "deletequestion/",
        views.Give_Me_DeleteQuestion_Page,
        name="delete_question_page"
    ),

    path(
        "showallquestion/",
        views.Give_Me_ShowAllQuestion_Page,
        name="show_all_question_page"
    ),


    # ==================================================
    # QUESTION ACTIONS
    # ==================================================

    path(
        "addquestions/",
        views.AddQuestions,
        name="add_questions"
    ),

    path(
        "view-question/",
        views.View_Question,
        name="view_question"
    ),

    path(
        "update-question/",
        views.View_Question_Update,
        name="view_question_update"
    ),

    path(
        "delete-question/",
        views.View_Question_Delete,
        name="view_question_delete"
    ),

    path(
        "updatequestion-action/",
        views.UpdateQuestion,
        name="update_question"
    ),

    path(
        "deletequestion-action/",
        views.DeleteQuestion,
        name="delete_question"
    ),


    # ==================================================
    # STUDENT PAGES
    # ==================================================

    path(
        "givemeregister/",
        views.GiveMeRegisterPage,
        name="register_page"
    ),

    path(
        "givemelogin/",
        views.GiveMeLoginPage,
        name="login_page"
    ),

    path(
        "studentcurd/",
        views.GiveMeStudentCurdPage,
        name="student_curd"
    ),

    path(
        "addstudent/",
        views.GiveMeAddstudentpage,
        name="add_student_page"
    ),

    path(
        "updatestudent/",
        views.GiveMeUpdatestudentpage,
        name="update_student_page"
    ),

    path(
        "viewstudent/",
        views.GiveMeViewstudentpage,
        name="view_student_page"
    ),

    path(
        "deletestudent/",
        views.GiveMeDeletestudentpage,
        name="delete_student_page"
    ),

    path(
        "showallstudents/",
        views.GiveMeShowAllPage,
        name="show_all_students"
    ),


    # ==================================================
    # STUDENT ACTIONS
    # ==================================================

    path(
        "register/",
        views.Register,
        name="register"
    ),

    path(
        "login/",
        views.login,
        name="login"
    ),

    path(
        "adduser/",
        views.AddUser,
        name="add_user"
    ),

    path(
        "showuser/",
        views.ShowUser,
        name="show_user"
    ),

    path(
        "updateuser/",
        views.UpdateUser,
        name="update_user"
    ),

    path(
        "deleteuser/",
        views.DeleteUser,
        name="delete_user"
    ),

    path(
        "deleteuser-showall/",
        views.DeleteUserForShowAllPage,
        name="delete_user_showall"
    ),


    # ==================================================
    # EXAM FLOW
    # ==================================================

    # Login -> Select Subject
    path(
        "starttestpage/",
        views.StartTestPage,
        name="start_test_page"
    ),

    # Select Subject -> First Question
    path(
        "starttest/",
        views.StartTest,
        name="start_test"
    ),

    # Next Question
    path(
        "nextquestion/",
        views.NextQuestion,
        name="next_question"
    ),

    # Previous Question
    path(
        "previousquestion/",
        views.PreviousQuestion,
        name="previous_question"
    ),

    # End Test
    path(
        "endtest/",
        views.End_Test,
        name="end_test"
    ),


    # ==================================================
    # RESULT
    # ==================================================

    path(
        "score/",
        views.ScorePage,
        name="score_page"
    ),

    path(
        "getallresultpage/",
        views.GetAllResultPage,
        name="get_all_result_page"
    ),


    # ==================================================
    # LOGOUT
    # ==================================================

    path(
        "logout/",
        views.LogoutUser,
        name="logout"
    ),

    path(
    "showallusers/",
    views.ShowAllUsers,
    name="show_all_users"
),
]