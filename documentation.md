# Speed Sketch - Documentation

## File Structure

```
drawing_game/
├── ContainerPage.py      # App entry point
├── MainPage.py           # Main menu
├── StartingPage.py      # Category selection
├── PlayPage.py          # Game canvas
└── ui/                  # Auto-generated PyQt UI
    ├── containerForm.py
    ├── mainPage.py
    ├── startingScene.py
    └── playScene.py
```

## OOP Structure

```
ContainerPage                  #Window Container
    stack_pages
        0-MainPage
        1-StartingPage
        2-PlayPage


MainPage                      #Main Menu
    button_easy
    button_medium
    button_hard
    analytics_container


StartingPage                  #Category Selection
    label_difficulty
    listwidget_categories
    button_start


PlayPage                      #Drawing Canvas
    label_difficulty
    label_timer
    label_category
    label_phrase
    drawing_space
        DrawingCanvas
```
ContainerPage                  #Window Container
    stack_pages
        0-MainPage
        1-StartingPage
        2-PlayPage


MainPage                      #Main Menu
    button_easy
    button_medium
    button_hard


StartingPage                  #Category Selection
    button_animals
    button_flowers
    button_art
    button_expression
    button_start


PlayPage                      #Drawing Canvas
    drawing_canvas
    label_timer
    label_phrase
```

## Navigation

```
MainPage -> StartingPage -> PlayPage
   |              |            |
Difficulty    Category    Drawing
Selection    Selection     Canvas
```

## Key Concepts

- **Composition**: ContainerPage contains MainPage, StartingPage, PlayPage
- **Parent Widget**: Passing `self` to child pages enables signal/slot communication
- **QStackedWidget**: Manages page switching by index