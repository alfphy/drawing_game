ContainerPage.py                  #Window Container
MainPage.py                       #Main Menu
StartingPage.py                   #Category Selection
PlayPage.py                       #Drawing


ContainerPage
 stack_pages
    0-MainPage
    1-StartingScene
    2-PlayPage


MainPage
    -button-
        button_easy
        button_medium
        button_hard
    -layout container-
        analytics_container

StartingScene
    -label-
        label_difficulty
    -list widget-
        listwidget_categories
        

PlayScene
    -label-
        label_difficulty
        label_timer
        label_phrase
        