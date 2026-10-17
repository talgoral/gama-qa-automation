import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page():                                #הגדרת פונקציה שמספקת לטסט אובייקט בשם page
    with sync_playwright() as p:           #הפעלת playwright
        browser = p.chromium.launch()      #פתיחת דפדפן כרום
        
        try:                                   #ניסיון לפתוח את האתר 
            page = browser.new_page()          #פתיחת עמוד חדש בדפדפן
            yield page                         #מוסר את העמוד לטסט ומשהה את המשך הפונקציה
        finally:                               #יתרחש גם אם האתר לא יצליח להפתח
        browser.close()                    #מתבצע לאחר שהטסט מסתיים, גם אם הוא נכשל
