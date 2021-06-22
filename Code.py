import requests
import remi.gui as gui
from remi import start, App
def get_access_token():
    # API網址
    url = "https://www.themealdb.com/api/json/v1/1/random.php"
    text = requests.get(url)
    print(text.json())
    a = text.json()
    #mystr=a["meals"][0]["strIngredient1"]+
    count=0
    for i in range(1,21):
        if a["meals"][0]["strIngredient"+str(i)]!="":
            count+=1
            print(a["meals"][0]["strIngredient"+str(i)])
            print(f"https://www.google.com/search?q={a['meals'][0]['strIngredient'+str(i)].replace(' ','%20')}")
    print(count)

    #print(a["meals"][0]["strMeal"])
    #print(a["meals"][0]["strYoutube"])
    #print(a["meals"][0]["strMealThumb"])
    #print(a["meals"][0]["strInstructions"])
    #mystr = a["meals"][0]["strYoutube"]
    #mystr=mystr.split('=')
    #print(mystr[1])

class Recipe(App):
    def __init__(self,*args):
        super(Recipe,self).__init__(*args)

    def main(self):

        container = gui.Container(width='100%',height='100%', margin='0px auto',style={'display': 'block', 'overflow': 'hidden'})
        horizontalContainer = gui.Container(width='100%', layout_orientation=gui.Container.LAYOUT_HORIZONTAL,margin='0px', style={'display': 'block', 'overflow': 'auto'})
        container = gui.Container(width="100%",display="block")
        subContainerLeft = gui.Container(width="40%",style={'display': 'block', 'overflow': 'auto', 'text-align': 'center'})
        subContainerRight = gui.Container(style={'width':"60%",'display': 'block', 'overflow': 'auto', 'text-align': 'center'})
        container.style["background-color"] = 'rgb(235,148,24)'
        url = "https://www.themealdb.com/api/json/v1/1/random.php"
        text = requests.get(url)
        print(text.json())
        a = text.json()
        self.name = gui.Label('Food name: '+a["meals"][0]["strMeal"])
        self.name.style["text-align"] = "center"
        self.name.style["padding"]="5px"
        self.area=gui.Label('Country: '+a["meals"][0]["strArea"])
        self.area.style["text-align"] = "center"
        self.area.style["padding"] = "3px"
        mystr = a["meals"][0]["strYoutube"]
        mystr = mystr.split('=')
        sor = "https://www.youtube.com/embed/"+mystr[1]
        self.link = gui.Widget()
        self.link.add_child('iframe','<iframe width="350" height="350" src='+sor+' title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')
        self.link.style.update({"float":"left","border-left":"1px solid black","margin":"0px auto","padding-left":"25%","padding-top":"1%","padding-bottom":"1%"})
        self.photo = gui.Image(a["meals"][0]["strMealThumb"],width="60%",height="60%")
        self.photo.attributes["position"]="absolute"
        self.myimg = gui.Image("http://img.yao51.com/jiankangtuku/nllhohlhcv.jpeg",width="33%",height="33%")
        subContainerLeft.style.update({"border-top":"1px solid black","margin-top":"0.5%"})
        subContainerRight.style.update({"border-top": "1px solid black", "margin-top": "0.5%"})
        self.ins=gui.Label('Instructions: ')
        self.ins.style["text-align"] = "left"
        self.ins.style["font-size"] = "20px"
        self.ins.style["color"] = "red"
        self.ins.style["margin-top"] = "1px auto"
        self.ins.style["padding-left"] = "1%"
        self.ins.style["border-left"]="1px solid black"

        self.st = gui.Label(a["meals"][0]["strInstructions"])
        self.name.style["font-size"] = "30px"
        self.area.style["font-size"] = "20px"
        self.photo.style.update({"float": "left", "display": "block", "margin": "0 auto", "padding-left": "17%", "padding-top": "10%"})
        self.myimg.style.update({"float": "left", "display": "block", "margin": "0 auto", "padding-left": "3%", "padding-top": "8%"})
        self.st.style.update({"border-left":"1px solid black","border-bottom":"1px solid black","margin":"0px auto","padding":"1%"})
        self.st.style["text-align"] = "left"
        self.st.style["font-size"] = "16px"
        self.st.style["float"] = "left"

        container.append(self.name)
        container.append(self.area)
        subContainerLeft.append(self.photo)

        subContainerRight.append(self.ins)
        subContainerRight.append(self.st)

        subContainerRight.append(self.link)
        subContainerRight.append(self.myimg)
        self.subContainerRight = subContainerRight
        self.subContainerLeft = subContainerLeft
        horizontalContainer.append([subContainerLeft, subContainerRight])
        container.append(horizontalContainer)

        return container

start(Recipe)
get_access_token()

