# word_lists.py


def get_phrase(category_index, phrase_index):
    category_name = categories[category_index]
    return category_name, phrases_list[str(category_name)][phrase_index]
categories = ["Animals", "Flowers", "Emoji", "Vehicles"]
#easy
phrases_list = {
    "Animals": [
        "a cat sleeping",
        "a dog sitting",
        "a fish swimming",
        "a bird flying",
        "a lion roaring",
        "an elephant with a trunk",
        "a monkey eating a banana",
        "a giraffe with a long neck",
        "a penguin standing",
        "a turtle walking",
        "a rabbit with long ears",
        "a bear holding honey",
        "a frog on a leaf",
        "a pig in mud",
        "a cow with spots",
        "a mouse with cheese",
        "a duck in water",
        "a snake coiled up",
        "a spider in a web",
        "a bee near a flower"
    ],

    "Flowers": [
        "a red rose",
        "a yellow tulip",
        "a white daisy",
        "a tall sunflower",
        "a pink lotus",
        "a lily in a pond",
        "a purple orchid",
        "a cactus in a pot",
        "a spotted mushroom",
        "a big tree",
        "a falling leaf",
        "a palm tree on a beach",
        "a pine tree with cones",
        "a cherry blossom branch",
        "a four leaf clover",
        "a hanging vine",
        "a bamboo stalk",
        "a curly fern",
        "ivy on a wall",
        "a round bush"
    ],

    "Emoji": [
        "a happy smiley face",
        "a frowning sad face",
        "an angry red face",
        "a face crying tears",
        "a face laughing hard",
        "a face with heart eyes",
        "a cool face with sunglasses",
        "a shocked surprised face",
        "a face winking",
        "a face blowing a kiss",
        "a face sleeping with Zs",
        "a sick face with thermometer",
        "a nerdy face with glasses",
        "a cowboy face with hat",
        "a clown face with red nose",
        "a white skull",
        "a cute ghost",
        "a green alien head",
        "a robot face",
        "a poop emoji"
    ],

    "Vehicles": [
        "a small red car",
        "a big yellow bus",
        "a long train with smoke",
        "an airplane in the sky",
        "a helicopter with blades",
        "a sailboat on water",
        "a large cruise ship",
        "a bicycle with two wheels",
        "a fast motorcycle",
        "a big dump truck",
        "a rocket blasting off",
        "a yellow submarine",
        "a colorful hot air balloon",
        "a small scooter",
        "a skateboard with wheels",
        "a green tractor",
        "an ambulance with siren",
        "a red fire truck",
        "a police car with lights",
        "a yellow taxi cab"
    ]
}