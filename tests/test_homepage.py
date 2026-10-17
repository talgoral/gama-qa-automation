def test_homepage_title(page):
    expected_title = "הפניקס גמא - פתרונות אשראי ומימון לעסקים בתנאים מעולים"

    #ניווט לאתר
    page.goto("https://www.gamaf.co.il/")  

    #קריאת כותרת העמוד בפועל
    actual_title = page.title()            

    #השוואה בין התוצאה בפועל לצפויה
    assert actual_title == expected_title  