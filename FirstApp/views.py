from django.shortcuts import render, redirect
from django.contrib import messages
# from . import config as cfg
import pymysql as sql

def Home(request):
    return render(request, "FirstApp/home.html")

def Login(request):
    if request.method == "POST":
        Email = request.POST.get("email")
        Password = request.POST.get("password")
        Connection = sql.connect(host="localhost", user="root", database="djangodb", password="12345")
        Cursor = Connection.cursor()
        Sql = f"""select * from userinfo where Email = '{Email}' and Password = '{Password}'"""
        try:
            Cursor.execute(Sql)
            Fetch = Cursor.fetchone()
            if not Fetch: # Condition executes when Fetch is  empty ()
                raise Exception("Invalid email or password")
            # Session Storage
            request.session["UserName"] = Fetch[0]
            request.session["Email"] = Fetch[1]
            messages.success(request, "Login successful")
        except Exception as e:
            messages.warning(request, f"{e}")
        finally:
            Cursor.close()
            Connection.close()
    return render(request, "FirstApp/login.html")

def Signup(request):
    if request.method == "POST":
        Name = request.POST.get("name")
        Email = request.POST.get("email")
        Password = request.POST.get("password")
        Connection = sql.connect(host="localhost", user="root", database="djangodb", password="12345")
        Cursor = Connection.cursor()
        Sql = f"""insert into userinfo values('{Name}', '{Email}', '{Password}');"""
        try:
            Cursor.execute(Sql)
            Connection.commit()
            messages.success(request, "Created your account!")
        except Exception as e:
            Connection.rollback()
            messages.warning(request, f"Signup unsuccessful {e}")
        finally:
            Cursor.close()
            Connection.close()
    return render(request, "FirstApp/signup.html")

def ForgetPassword(request):
    if request.method == "POST":
        Email = request.POST.get("email")
        Password = request.POST.get("password")
        Connection = sql.connect(host="localhost", user="root", database="djangodb", password="12345")
        Cursor = Connection.cursor()
        Sql = f"""select * from userinfo where Email = '{Email}';"""
        try:
            Cursor.execute(Sql)
            Fetch = Cursor.fetchone()
            if Fetch:
                SqlUpdate = f"""update userinfo set Password = '{Password}' where Email = '{Email}';"""
                Cursor.execute(SqlUpdate)
                Connection.commit()
                messages.success(request, f"Your password has been updated!")
            else:
                messages.warning(request, f"Oops! We couldn't find your account :(")
        except Exception as e:
            Connection.rollback()
            messages.error(request, f"Password update unsuccessful --> {e}")
        finally:
            Cursor.close()
            Connection.close()
    return render(request, "FirstApp/forget_password.html")

def App(request):
    return render(request, "FirstApp/app.html")

def ShowUsers(request):
    Connection = sql.connect(host="localhost", user="root", database="djangodb", password="12345")
    Cursor = Connection.cursor()
    Sql = f"""select * from userinfo;"""
    try:
        Cursor.execute(Sql)
        Fetch = Cursor.fetchall()
        return render(request, "FirstApp/users_info.html", context={"Users" : Fetch})
    except Exception as e:
        messages.info(request, f"Cannot fetch the userinfo")
    finally:
        Cursor.close()
        Connection.close()

    