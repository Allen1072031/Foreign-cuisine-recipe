# 異國美食大全Foreign-cuisine-recipe

## Introduction
在現今的生活中，大家越來越喜歡嘗試異國料理，因此在這個網站中，會隨機的出現一道美食的圖片，並且顯示該美食的步驟、所需食材還有參考影片。

本程式透過Free Meal API所提供的可以隨機產生一道料理的API，並透過remi來處理成網頁的形式，
使得資料能夠經由簡單明瞭的網站讓使用者能夠輕易地看懂。



## Build process
首先必須先安裝requests
```
pip3 install requests
```
再來安裝remi
```
pip3 install remi
```

## Execute
```
python3 food.py
```
## Result
![image](https://github.com/Allen1072031/Foreign-cuisine-recipe/blob/main/result.jpg)

## Detail
Remi是一個能夠很輕鬆地來處理網頁前端的一個套件，使用的方法也與HTML與CSS相似，非常容易就能夠上手。



## Reference
1. [Free Meal API](https://www.themealdb.com/api.php)
2. [remi document](https://remi.readthedocs.io/en/latest/_modules/remi/gui.html)
3. [remi container example](https://github.com/dddomodossola/remi/blob/master/examples/widgets_overview_app.py)
