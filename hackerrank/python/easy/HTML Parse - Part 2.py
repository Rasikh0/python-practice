from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if(data!= "\n"):
            print(">>> Data")
            print(data)
    
    def handle_comment(self, data):
        lst = data.split("\n")
        if(len(lst)==1):
            print(">>> Single-line Comment")
            print(lst[0])
        else:
            print(">>> Multi-line Comment")
            print(*lst, sep="\n")
    
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()
