

def get_phrase(category_index, phrase_index):
    category_name = categories[category_index]
    # if category_name == "Animals":
    #     prefix = "a sketch of a"
    # elif category_name == "Flowers":
    #     prefix = "a sketch of a"
    # elif category_name == "Emoji":
    #     prefix = "an emoji of"
    # elif category_name == "Vehicles":
    #     prefix = "a sketch of a"
    # else:
    #     prefix = "a drawing of"
    return category_name, f"{phrases_list_easy[str(category_name)][phrase_index]}"
categories = ["Animals", "Flowers", "Emoji", "Vehicles"]

#easy
phrases_list_easy = {
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
        "a rose with a stem and leaf",
        "a tulip with a curved stem",
        "a daisy with round petals",
        "a sunflower with big petals",
        "a lotus floating on water",
        "a lily with drooping petals",
        "an orchid on a branch",
        "a cactus in a small pot",
        "a mushroom with spots",
        "a tree with branches",
        "a leaf falling down",
        "a palm tree with coconuts",
        "a pine tree with a pointy top",
        "a branch with blossoms",
        "a clover with four leaves",
        "a vine hanging down",
        "a bamboo stalk with lines",
        "a fern with tiny leaves",
        "ivy climbing a wall",
        "a round bush"
    ],

    "Emoji": [
        "a happy smiley face",
        "a sad frowning face",
        "an angry face",
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
        "a clown face with big nose",
        "a skull with eye holes",
        "a cute ghost",
        "an alien head with big eyes",
        "a robot face",
        "a poop emoji"
    ],

    "Vehicles": [
        "a small car",
        "a big bus",
        "a train with smoke",
        "an airplane in the sky",
        "a helicopter with spinning blades",
        "a sailboat on water",
        "a large ship",
        "a bicycle with two wheels",
        "a fast motorcycle",
        "a dump truck",
        "a rocket blasting off",
        "a submarine underwater",
        "a hot air balloon floating",
        "a small scooter",
        "a skateboard with wheels",
        "a tractor in a field",
        "an ambulance with siren",
        "a fire truck with ladder",
        "a police car with lights",
        "a taxi cab"
    ]
}

phrases_list_hard = {}
phrases_list_medium = {}
