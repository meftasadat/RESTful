#!/usr/bin/env python
import web
from xml.dom import minidom


xmldoc = minidom.parse('weather.xml')
itemlist = xmldoc.getElementsByTagName('month')
urls = (
    '/weather', 'list',
    '/weather/(\d+)', 'weatherByYear',
    '/weather/(\d+)/(.*)', 'weatherByMonth',
    '/weather.json', 'weatherJson',
    '/f2c/(\d+)', 'f2c',
     '/c2f/(\d+)', 'c2f',

)

app = web.application(urls, globals())

class list:
    def GET(self):
	output = 'Average Monthly Temperature:\n\n';
	for s in itemlist:
                print(s.attributes['name'].value)
                print(s.childNodes[0].data)
                output += str(s.attributes['year'].value)+"  "+str(s.attributes['name'].value) +" : " + str(s.childNodes[0].data) +'\n\n';
        return output

class weatherByYear:
    def GET(self, year):
        myStr = "Year:"+year+"\n"
        print(year)
        for s in itemlist:
            if(s.attributes['year'].value==year):
                print(s.attributes['name'].value)
                myStr += str(s.attributes['name'].value)+ " " +str(s.childNodes[0].data) +'\n';
	return myStr

class weatherByMonth:
    def GET(self,year, month):
        myStr = "Year:" + year+"\n"
        print(myStr)
        for s in itemlist:
            if(s.attributes['year'].value==year):
                if (s.attributes['name'].value==month):
                    print(s.attributes['name'].value)
                    myStr += str(s.attributes['name'].value)+ " " + str(s.childNodes[0].data);
	return myStr

class weatherJson:
    def GET(self):
	output = '{"Temperature":[';
	for s in itemlist:
                print(s.attributes['name'].value)
                print(s.childNodes[0].data)
                output += "'year'"+":'"+str(s.attributes['year'].value)+"',"+"'month'"+":'"+str(s.attributes['name'].value) +"',"+ "'temp'"+":'"+str(s.childNodes[0].data+"'"+",");
        output = output[:-1]
        output += ']}\n';
        return output

class f2c:
    def GET(self, Far):
        output = str(Far) + " F = " +str(((int(Far) - 32) * 5/9)) + " C";
	return output

class c2f:
    def GET(self, Cel):
        output = str(Cel) + " C = " +str(((int(Cel) * 9/5 + 32))) + " F";

	return output

if __name__ == "__main__":
    app.run()