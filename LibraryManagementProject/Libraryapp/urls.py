from django.urls import path

from Libraryapp import views

urlpatterns = [
        path('',views.log_fun,name='log'),#it will redirect to html page
        path('logdata',views.logdata_fun),#it will authenticate the superuser
        path('adminreg',views.admin_reg_fun,name='adminreg'),#it will redirect to adminregister.html page
        path('aregdata',views.admin_regdata_fun),#it will create superuser
        path('stdentreg',views.student_reg_fun,name='studentreg'),#it will redirect to studentregister.html page
        path('sregdata',views.student_regdata_fun),#it will read student details
        path('adminhome',views.adminhome,name='adminhome'),#it will redirect to adminhome


        path('adminhome',views.home_fun,name='shome'),
        path('addbooks',views.addbook_fun,name='add'),
        path('readdata',views.readbookdata_fun),
        path('display',views.displaybook_fun,name='display'),
        path('update/<int:id>',views.update_fun,name='update'),
        path('del/<int:id>',views.delete_fun,name='del'),
        path('log_out',views.log_out_fun,name='log_out'),

        path('assigndata',views.assign_fun,name='assign'),
        path('readassigndata',views.assignbook_fun,name='get'),
        path('sreaddata',views.assignbookdata_fun,name='issued'),
        path('issuedata',views.issuebook_fun,name='issue'),
        path('update2/<int:id>',views.update2_fun,name='update2'),
        path('del2/<int:id>',views.delete2_fun,name='del2'),

        # student page urls

        path('studenthome',views.studenthome,name='studenthome'),#it will redirect to studenthome
        path('issuedbk',views.issuebkdet_fun,name='issuedbk'),#it will redirect to issue book.html page
        path('stdprofile',views.Student_pro,name='studenprofile'),
        path('updateprof/<int:id>',views.Update_pro,name='updtprof'),
        path('logoutstd',views.logoutstd_fun,name='logoutstd'),#it will logout from student page

]