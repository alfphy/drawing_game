import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc
import ui.startingScene
from PlayPage import PlayPage
import analyzer

class StartingPage(qtw.QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.ui = ui.startingScene.Ui_startingScene()
        self.ui.setupUi(self)
        self.ui.button_start.clicked.connect(self.button_start_click)


        #cateogires
        self.category_cards_states = {}
        self.ui.animals_card.installEventFilter(self)
        self.ui.flowers_card.installEventFilter(self)
        self.ui.vehicles_card.installEventFilter(self)
        self.ui.emojis_card.installEventFilter(self)

        for card in [self.ui.animals_card, self.ui.flowers_card, self.ui.vehicles_card, self.ui.emojis_card]:
            self.category_cards_states[card] = True

    def eventFilter(self, obj, event):
        if obj not in self.category_cards_states:
            return False
        if event.type() == event.Type.MouseButtonPress:
            if event.button() == qtc.Qt.MouseButton.LeftButton:
                if obj in self.category_cards_states:

                    state = self.category_cards_states[obj]
                    self.check_toggle_card(obj, state)
                    self.border_toggle_card(obj, state)
                    self.category_cards_states[obj] = not state

                    return True

        return super().eventFilter(obj, event)
    def border_toggle_card(self, obj, state):
        obj.setProperty("selected", str(not state).lower())
        obj.style().unpolish(obj)
        obj.style().polish(obj)
    def check_toggle_card(self, obj, state):
        if obj.objectName() == "animals_card":
            self.ui.label_checked_animals.setVisible(not state)
        elif obj.objectName() == "flowers_card":
            self.ui.label_checked_flowers.setVisible(not state)
        if obj.objectName() == "vehicles_card":
            self.ui.label_checked_vehicles.setVisible(not state)
        elif obj.objectName() == "emojis_card":
            self.ui.label_checked_emojis.setVisible(not state)



    def button_start_click(self):
        self.parent.ui.stack_pages.setCurrentIndex(2)
        self.parent.playPage.start_timer(30)

