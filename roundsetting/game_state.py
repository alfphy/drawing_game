import roundsetting.phrases

game_config = None

class GameConfig:
    def __init__(self, level, categories: list[str] = None):
        self.difficulty_config = DifficultyConfig(level)
        self.categories = categories

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

