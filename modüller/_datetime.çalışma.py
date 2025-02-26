import datetime
result = dir(datetime)
print(result)


result = datetime.datetime.now()
result = datetime.datetime.now().month
print(result)


simdi = datetime.datetime.now()
result = datetime.datetime.ctime(simdi)
result = datetime.datetime.strftime(simdi,"%y")
result = datetime.datetime.strftime(simdi,"%x")
result = datetime.datetime.strftime(simdi,"%d")
result = datetime.datetime.strftime(simdi,"%A")
result = datetime.datetime.strftime(simdi,"%b")
result = datetime.datetime.strftime(simdi,"%Y %b %A")
print(result)


t = "15 april 2019 hour 10:12:30"
time = datetime.datetime.strptime(t,'%d %B %Y hour %H:%M:%S')
print(time)