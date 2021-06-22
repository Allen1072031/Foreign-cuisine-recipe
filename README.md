# Foreign-cuisine-recipe
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FAllen1072031%2FForeign-cuisine-recipe&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

## Introduction
在全球化的社會中，網路與交通的發達，讓大家能夠輕輕鬆鬆的品嚐到來自不同國家的美食。這些異國美食不但替我們的味蕾帶來了與平常更加不同的享受，同時也讓我們能夠更加深入了解和欣賞異國的文化。
而每個人的喜好不盡相同，有些人喜歡中華料理那講究的精神、有些人喜歡義大利菜那種簡單浪漫的氣氛、又或許有些人偏好美式風格那樣的飽足餐點。

為了滿足每個人對於美食的期待與需求，因此在這個網站中，會隨機出現一道美食的圖片，並顯示這道美食的名稱與國家，以及製作這道美食的料理步驟、所需食材以及相關的影片提供參考，讓喜歡嘗試異國料理的人們，不僅能夠透過網路交通來品嚐，更能夠自己嘗試製作，享受到最新鮮的美味。

期待每個使用過這個網站的使用者，都能夠被「美食」串連起來，不單是為了美食，也為了能夠更貼近人與人之間的生活、文化，甚至是內心。

本程式透過Free Meal API所提供的可以隨機產生一道料理的API，並經過一些Python的處理，接著透過remi這個套件來處理成網頁的形式，
使得原本複雜的資料能夠經由簡單明瞭的網站呈現來讓使用者能夠輕易地看懂。



## Build process
首先必須先安裝requests
```
pip3 install requests
```
再來必須要安裝remi
```
pip3 install remi
```

## Execute
```
python3 myfood.py
```


## Detail
使用themealdb所提供的API來獲取資料
```
url = "https://www.themealdb.com/api/json/v1/1/random.php"
        text = requests.get(url)
```
這邊為隨機接收到一道料理的json的形式，可以從strMeal取得食物的名稱，strArea取得食物的國家，strInstructions取得食物的步驟，strIngredient取得食物所需的食材,strMealThumb取得食物的照片，strYoutube取得食物在youtube的教學影片。
```json
{
    "meals": [
        {
            "idMeal": "53050",
            "strMeal": "Ayam Percik",
            "strDrinkAlternate": null,
            "strCategory": "Chicken",
            "strArea": "Malaysian",
            "strInstructions": "In a blender, add the ingredients for the spice paste and blend until smooth.\r\nOver medium heat, pour the spice paste in a skillet or pan and fry for 10 minutes until fragrant. Add water or oil 1 tablespoon at a time if the paste becomes too dry. Don't burn the paste. Lower the fire slightly if needed.\r\nAdd the cloves, cardamom, tamarind pulp, coconut milk, water, sugar and salt. Turn the heat up and bring the mixture to boil. Turn the heat to medium low and simmer for 10 minutes. Stir occasionally. It will reduce slightly. This is the marinade/sauce, so taste and adjust seasoning if necessary. Don't worry if it's slightly bitter. It will go away when roasting.\r\nWhen the marinade/sauce has cooled, pour everything over the chicken and marinate overnight to two days.\r\nPreheat the oven to 425 F.\r\nRemove the chicken from the marinade. Spoon the marinade onto a greased (or aluminum lined) baking sheet. Lay the chicken on top of the sauce (make sure the chicken covers the sauce and the sauce isn't exposed or it'll burn) and spread the remaining marinade on the chicken. Roast for 35-45 minutes or until internal temp of the thickest part of chicken is at least 175 F.\r\nLet chicken rest for 5 minutes. Brush the chicken with some of the oil. Serve chicken with the sauce over steamed rice (or coconut rice).",
            "strMealThumb": "https://www.themealdb.com/images/media/meals/020z181619788503.jpg",
            "strTags": null,
            "strYoutube": "https://www.youtube.com/watch?v=9ytR28QK6I8",
            "strIngredient1": "Chicken Thighs",
            "strIngredient2": "Challots",
            "strIngredient3": "Ginger",
            "strIngredient4": "Garlic Clove",
            "strIngredient5": "Cayenne Pepper",
            "strIngredient6": "Turmeric",
            "strIngredient7": "Cumin",
            "strIngredient8": "Coriander",
            "strIngredient9": "Fennel",
            "strIngredient10": "Tamarind Paste",
            "strIngredient11": "Coconut Milk",
            "strIngredient12": "Sugar",
            "strIngredient13": "Water",
            "strIngredient14": "",
            "strIngredient15": "",
            "strIngredient16": "",
            "strIngredient17": "",
            "strIngredient18": "",
            "strIngredient19": "",
            "strIngredient20": "",
            "strMeasure1": "6",
            "strMeasure2": "16",
            "strMeasure3": "1 1/2 ",
            "strMeasure4": "6",
            "strMeasure5": "8",
            "strMeasure6": "2 tbs",
            "strMeasure7": "1 1/2 ",
            "strMeasure8": "1 1/2 ",
            "strMeasure9": "1 1/2 ",
            "strMeasure10": "2 tbs",
            "strMeasure11": "1 can ",
            "strMeasure12": "1 tsp ",
            "strMeasure13": "1 cup ",
            "strMeasure14": " ",
            "strMeasure15": " ",
            "strMeasure16": " ",
            "strMeasure17": " ",
            "strMeasure18": " ",
            "strMeasure19": " ",
            "strMeasure20": " ",
            "strSource": "http://www.curiousnut.com/roasted-spiced-chicken-ayam-percik/",
            "strImageSource": null,
            "strCreativeCommonsConfirmed": null,
            "dateModified": null
        }
    ]
}
```
Remi是python能夠輕鬆地來處理網頁前端的一個套件，使用的方法也與HTML與CSS相似，非常容易就能夠上手。
以下是個簡單的remi範例，下方的程式碼是用來顯示食物的名稱，透過第二行所寫的style可以用來更改成自己想要的樣子。
```
self.name = gui.Label('Food name: '+a["meals"][0]["strMeal"])
self.name.style["text-align"] = "center"
self.name.style["padding"]="5px"
container.append(self.name)
```
## Result
從結果的圖片來看，上方顯示出了這道料理的名稱以及國家，左邊顯示出了料理的照片，右邊則是顯示了料理的詳細步驟，所需食材以及相關的影片提供參考，如果網頁無法成功顯示，請再重新跑一次程式
![image](https://github.com/Allen1072031/Foreign-cuisine-recipe/blob/main/result.jpg)

## Reference
1. [Free Meal API](https://www.themealdb.com/api.php)
2. [remi document](https://remi.readthedocs.io/en/latest/_modules/remi/gui.html)
3. [remi container example](https://github.com/dddomodossola/remi/blob/master/examples/widgets_overview_app.py)
