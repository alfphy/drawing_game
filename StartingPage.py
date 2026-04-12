import PyQt6.QtWidgets as qtw
import PyQt6.QtCore as qtc

import roundsetting.game_state
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
        category = ""
        if obj.objectName() == "animals_card":
            self.ui.label_checked_animals.setVisible(not state)
            category = "Animals"
        elif obj.objectName() == "flowers_card":
            self.ui.label_checked_flowers.setVisible(not state)
            category = "Flowers"
        if obj.objectName() == "vehicles_card":
            self.ui.label_checked_vehicles.setVisible(not state)
            category = "Vehicles"

        elif obj.objectName() == "emojis_card":
            self.ui.label_checked_emojis.setVisible(not state)
            category = "Emojis"

        if not state:
            roundsetting.game_state.game_config.add_category(category)
        else:
            roundsetting.game_state.game_config.remove_category(category)
        self.update_selection()



    def update_selection(self):
        selection = ', '.join(roundsetting.game_state.game_config.categories)
        self.ui.label_selected.setText(str(selection))



    def button_start_click(self):
        if len(roundsetting.game_state.game_config.categories) == 0:
            return
        self.parent.ui.stack_pages.setCurrentIndex(2)
        self.parent.playPage.start_drawing()

