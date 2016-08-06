

from hackutils import sh


a=sh('date')
a=a.split(' ')
print(a)
time=a[4]
time=time.split(":")
print(time)
sh('cd /home/sourabh/Downloads/wallpaper')
 
#if time[1] <= 20
#	sh(gsettings set org.gnome.desktop.background picture-uri file:///home/serrano/Pictures/y.jpg)


#s=sh('cd work && cat test.sh')

"""
s=s.split(' ')
w = []
for x in s:
	if len(x) == 5:
		w.append(x)
print(w)

"""
