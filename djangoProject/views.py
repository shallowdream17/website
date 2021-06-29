import json
import uuid
from audioop import reverse

from django.contrib.auth.hashers import make_password, check_password
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect


from OAUser.models import OAUser
from SongInfomation.models import Infomation
from individual.models import individual
from comment.models import Comment
from djangoProject import settings
from login.models import test_login
from register.models import test_register
# def index_view(request):
#     dic={'shuju1':'yu','shuju2':'666'}
#     return render(request,'index.html',dic)

# def page1_view(request):
#     html='zheshiyigewangye'
#     return HttpResponse(html)
#
# def page2_view(request):
#     html='zheshiyigewangye'
#     return HttpResponse(html)
#
# def pg_view(request,pg):
#     html='zheshibianhaowei%s'%(pg)
#     return HttpResponse(html)
#
# def cal_view(request,a1,op,a2):
#     if op not in ['add','sub','mul']:
#         return HttpResponse('Your op is wrong')
#     if op == 'add':
#         return HttpResponse('结果:%s'%(a1+a2))
#     if op == 'sub':
#         return HttpResponse('结果:%s'%(a1-a2))
#     if op == 'mul':
#         return HttpResponse('结果:%s'%(a1*a2))

# def cal2_view(request,a1,op,a2):
#     return HttpResponse('shuru:%s,%s,%s'%(a1,op,a2))

# def test_mycal(request):
#     if request.method=='GET':
#         return render(request,'test.html')
#     elif request.method=='POST':
#
#         x =int(request.POST['x'])
#         y =int(request.POST.get('y'))
#         op =request.POST.get('op')
#
#         x=int(x)
#         y=int(y)
#         result=0
#         if op=='add':
#             result=x+y
#         elif op=='sub':
#             result=x-y
#         elif op=='mul':
#             result=x*y
#         elif op=='div':
#             result=x/y
#         return render(request, 'test.html', locals())


def index(request):
    username=request.session.get('username')
    users=OAUser.objects.filter(name=username).first()
    return render(request,'index.html',{'users':users})

def zhuanji(request):
    username = request.session.get('username')
    users = OAUser.objects.filter(name=username).first()
    zanshi_duixiang=Infomation.objects.all()
    return render(request,'zhuanji.html',{'users':users,'items':zanshi_duixiang})

def yyh(request):
    username = request.session.get('username')
    users = OAUser.objects.filter(name=username).first()#取session
    return render(request, 'yyh.html', {'users': users,})

def shbk(request):
    username = request.session.get('username')
    users = OAUser.objects.filter(name=username).first()  # 取session
    return render(request, 'shbk.html', {'users': users, })

def wsrcxx(request):
    username = request.session.get('username')
    users = OAUser.objects.filter(name=username).first()  # 取session
    return render(request, 'wsrcxx.html', {'users': users, })

def sjmr(request):
    username = request.session.get('username')
    users = OAUser.objects.filter(name=username).first()  # 取session
    return render(request, 'sjmr.html', {'users': users, })


    #return render(request, 'yyh.html', {'users': users,'comments':duixiang2})


def jicheng(request):
     return render(request,'jicheng.html')

#处理登录功能
def test_loginv(request):
    if(request.method=='GET'):
        return render(request,'test_login.html')
    else:
        #1、获取请求参数
        uname=request.POST.get('uname1','')
        pwd = request.POST.get('pwd1', '')

        #2、查询数据库
        if uname and pwd:
            cc=test_login.objects.filter(lo_name=uname,lo_pwd=pwd).count()
        #3、判断是否登录成功
            if cc!=0:
                return HttpResponse('登录成功')
            else:
                return HttpResponse('登录失败')
        else:
            return HttpResponse('登录失败')

#测试注册
def test_registerv(request):
    if request.method=='GET':
        return render(request,'test_register.html')
    else:
        # 1、接收请求参数
        uname=request.POST.get('uname','')
        pwd=request.POST.get('pwd','')
        # 2、非空判断
        if uname and pwd:
            # 3、创建模型对象
            duixiang=test_register(re_name=uname,re_pwd=pwd)
            # 4、插入数据库
            duixiang.save()
        # 5、页面响应
            return HttpResponse('注册成功')
        return HttpResponse('注册失败')

def show_view(request):
    #return render(request,'index.html')
    stus=test_register.objects.all()
    #print(stus)
    return render(request,'xianshi.html',{'sss':stus})

def register(request):#注册处理
    if request.method == 'POST':
        username=request.POST.get('user_name','')
        pwd=request.POST.get('user_pwd','')
        email=request.POST.get('user_email','')
        phone=request.POST.get('user_phone','')
        ccc = OAUser.objects.filter(name=username).count()
        if ccc!=0:
            return render(request,'register.html',{'errmsg':'用户名已存在！'})
        pwd=make_password(password=pwd)
        duixiang=OAUser.objects.create(name=username,password=pwd,phone=phone,email=email,is_active=0)
        duixiang.save()

        # 发送邮件

        token = str(uuid.uuid4()).replace('-', '')
        # request.session获取一个session对象 当成一个字典
        #print(duixiang.id)
        request.session[token] = duixiang.name
        #print(duixiang.id)
        path='http://127.0.0.1:8000/active?token={}'.format(token)

        subject='浅梦网激活邮件'
        message='''
        欢迎注册浅梦网！亲爱的用户请赶快激活使用！ 
        <br> <a href='{}'>点击激活</a>
        <br>
        如果链接不可用可以复制以下内容到浏览器激活：
        {}
        <br>
        &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;浅梦网开发者
        '''.format(path,path)
        result=send_mail(subject=subject,message="",from_email=settings.EMAIL_HOST_USER,
                         recipient_list=[email,],html_message=message)
        #print(result)

        return HttpResponse('注册成功!')



    return render(request,'register.html')

def login(request):#登录处理
    if request.method=='POST':
        username = request.POST.get('user_name', '')
        pwd = request.POST.get('user_pwd', '')
        duixiang=OAUser.objects.filter(name=username).first()
        if duixiang:
            if check_password(pwd,duixiang.password):
                if duixiang.is_active=='1':
                    request.session['username']=duixiang.name
                    #request.COOKIES['uname']=duixiang.name
                    #return HttpResponse('登录成功!')
                    users = OAUser.objects.filter(name=username).first()
                    return render(request, 'login.html', {'users': users,'okmsg':'ok了'})
                else:
                    return render(request, 'login.html', {'errmsg': '用户未激活!'})
            else:
                return render(request, 'login.html', {'errmsg': '用户名或者密码有误!'})
        else:
            return render(request,'login.html',{'errmsg':'用户名或者密码有误!'})
    return render(request,'login.html')

def user_active(request): #激活账号
    #print(666)
    token=request.GET.get('token')
    #print(token)
    uname = request.session.get(token)
    #print(uid)
    #获取session中的值
    duixiang=OAUser.objects.get(name=uname)
    duixiang.is_active='1'
    duixiang.save()
    #利用reverse函数反转url：找到urls.py中name='login'的路径
    #return redirect(reverse('login'))
    return render(request,'login.html')

def logout(request):
    #logout(request)
    request.session.flush()  #清除session
    return render(request,'index.html')


def songs(request):
    #print(request.GET.get('shoucang'))
    result = ""
    shoucang=0
    for k, v in request.GET.items():
        result = v
        # print(k)
        # print(v)
        if k=="shoucang" and v=="01":
            shoucang=1

    #print(result)
    ############################################################################################################
    username = request.session.get('username')#用户session
    users = OAUser.objects.filter(name=username).first()#取session
    duixiang2 = Comment.objects.filter(code_id=result).order_by('-id')#评论列表
    duixiang3=Infomation.objects.filter(code=result).first()#文章信息
    #print(duixiang3)
    # jsinfo=[{'jsinfo':duixiang3.code}]
    # dl = json.dumps(jsinfo)
    # print(dl[0])
    jsinfo={'jsinfo':duixiang3.code} #返回给ajax
    dl=json.dumps(jsinfo)
    ############################################################################################################

    #########################################################################################################
    if (shoucang == 1):  # 点赞请求
        zanshi=individual.objects.filter(code_id=result,user_id=users.name).first()
        if zanshi:
            pass
        else:
            duixiang3.good = duixiang3.good + 1
            duixiang3.save()
            duixiang4=individual.objects.create(code_id=result,user_id=users.name,once_good=1,title=duixiang3.title)
            duixiang4.save()
        # duixiang = OAUser.objects.create(name=username, password=pwd, phone=phone, email=email, is_active=0)
        # duixiang.save()
    ###########################################################################################################


    ############################################################################################################
    if request.method=='POST': #处理ajax
        text=request.POST.get('text')
        if text:
            duixiang = Comment.objects.create(text=text, user_id=users.name,code_id=result)
            duixiang.save()
            # 返回数据
            data = {}
            data['status'] = 'SUCCESS'
            data['username']=duixiang.user_id
            data['comment_time']=duixiang.comment_time.strftime('%Y-%m-%d %H:%M:%S')
            data['text']=duixiang.text
            data['code']=duixiang.code_id

        else:
            # 返回数据
            data = {}
            data['status '] = 'ERROR'
            data['message']='评论不能为空！'
        return JsonResponse(data)
    else:
        return render(request,'songs.html',{'users':users,'info':duixiang3,'comments':duixiang2,'jsinfo':dl})
    ############################################################################################################


def mypage(request):

    username = request.session.get('username')  # 用户session
    users = OAUser.objects.filter(name=username).first()  # 取session

    duixiang = individual.objects.filter(user_id=users.name).all()

    params=request.GET
    #print(params.get('id'))
    if params:
        del_id=params.get('id')
        zanshi1=individual.objects.filter(id=del_id).first()
        zanshi2=Infomation.objects.filter(code=zanshi1.code_id).first()
        zanshi2.good=zanshi2.good-1
        zanshi2.save()
        individual.objects.filter(id=del_id).delete()

    return render(request,'individual_page.html',{'users':users,'articals':duixiang})

def changepwd(request):
    username = request.session.get('username')  # 用户session
    users = OAUser.objects.filter(name=username).first()  # 取session

    if request.method=='POST':
        pwd1 = request.POST.get('user_pwd1', '')
        pwd2 = request.POST.get('user_pwd2', '')
        if check_password(pwd1, users.password):
            ppwwdd=make_password(pwd2)
            users.password=ppwwdd
            users.save()
            return render(request, 'change_pwd.html', {'users': users,'okmsg':'ok了'})
        else:
            return render(request,'change_pwd.html',{'users': users,'errmsg':'密码错误!'})

    return render(request, 'change_pwd.html', {'users': users, })