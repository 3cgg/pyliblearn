


class Kls(object):
    no_inst=0
    def __init__(self):
        Kls.no_inst=Kls.no_inst+1


def get_no_of_instances(cls_obj):
    return cls_obj.no_inst



ik1=Kls()
ik2=Kls()

print(get_no_of_instances(Kls))


class Date_test(object):
    day=0
    month=0
    year=0
    def __init__(self,year=0,month=0,day=0):
        self.year=year
        self.month=month
        self.day=day

    @classmethod
    def get_date(cls,string_date):
        year, month, day = map(int, string_date.split('-'))
        date1=cls(year,month,day)
        return date1

    def out_date(self):
        print('year : '), print(self.year), print('month : ') , print(self.month),print('day : '),print(self.day)


t=Date_test(2016,8,1)
t.out_date()

year,month,day=map(int,'2016-9-1'.split('-'))
t1=Date_test(year,month,day)
t1.out_date()

r=Date_test.get_date('2016-10-10')
r.out_date()






