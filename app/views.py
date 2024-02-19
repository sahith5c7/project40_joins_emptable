from django.shortcuts import render

# Create your views here.

from app.models import *
def equijoins(request):
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024)
    
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024,sal__gt=2500)
    
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=10)
    
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='Accounting')
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dlocation='Dallas')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    EMPOBJECTS=Emp.objects.select_related('deptno').all()[2:5:]
    d={'EMPOBJECTS':EMPOBJECTS}
    return render(request,'equijoins.html',d)


def selfjoins(request):
    empmgrobjects=Emp.objects.select_related('mgr').all()
    
    empmgrobjects=Emp.objects.select_related('mgr').filter(sal=2500)
    
    empmgrobjects=Emp.objects.select_related('mgr').filter(mgr__ename='KING')
    d={'empmgrobjects':empmgrobjects}
    return render(request,'selfjoins.html',d)


def emp_mgr_dept(request):
    emd=Emp.objects.select_related('deptno','mgr').all()
    
    emd=Emp.objects.select_related('deptno','mgr').filter(deptno__dname='Research')
    emd=Emp.objects.select_related('deptno','mgr').filter(mgr__ename='Blake')
    emd=Emp.objects.select_related('deptno','mgr').filter(ename='Martin')
    emd=Emp.objects.select_related('deptno','mgr').all()
    emd=Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname='Research') | Q(mgr__ename='JOHNS'))
    
    d={'emd':emd}
    return render(request,'emp_mgr_dept.html',d)



def emp_salgrade(request):
    #EO=Emp.objects.all()
    #SO=SalGrade.objects.all()
    #Retrieving the data of employess who belongs to grade 4
    #SO=SalGrade.objects.filter(grade=4)#[grade4 SalgradeObjects]

    #EO=Emp.objects.filter(sal__range=(SO[0].losal,SO[0].hisal))
    #Retrieving the data of employess who belongs to grade 3,4
    SO=Salgrade.objects.filter(grade__in=(3,4))

    EO=Emp.objects.none()
    for sgo in SO:
        EO=EO|Emp.objects.filter(sal__range=(sgo.low_sal,sgo.high_sal))
    d={'EO':EO,'SO':SO}
    return render(request,'emp_salgrade.html',d)
