import roundsetting.phrases
import random

class GameConfig:
    def __init__(self):
        self.difficulty_config = DifficultyConfig(0)
        self.categories = ["Animals", "Flowers", "Vehicles", "Emojis"]

    def set_difficulty(self, level):
        self.difficulty_config = DifficultyConfig(level)

    def add_category(self, category):
        self.categories.append(category)
    def remove_category(self, category):
        self.categories.remove(category)

    def get_categories_phrases(self):
        filtered_phrases = []

        for category in self.categories:
            filtered_phrases.extend(self.difficulty_config.phrases[category])
        return filtered_phrases
    def get_single_phrase(self):
        # random by default pag kuha og phrase
        category_name = random.choice(self.categories)
        phrase = random.choice(self.difficulty_config.phrases[category_name])
        return category_name,str(phrase)

class DifficultyConfig:
    def __init__(self, level):
        self.difficulty = difficulty_level_settings[level][0]
        self.initial_time = difficulty_level_settings[level][1]
        self.phrases = difficulty_level_settings[level][2]

difficulty_level_settings = [
    ( "Easy", 90, roundsetting.phrases.phrases_list_easy),
    ( "Medium",60,roundsetting.phrases.phrases_list_medium),
    ( "Hard", 30 , roundsetting.phrases.phrases_list_hard)
]

game_config = GameConfig()
