

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
        "a cat sitting",
        "a dog standing",
        "a fish swimming",
        "a bird flying",
        "a lion face",
        "an elephant with big ears",
        "a monkey with a tail",
        "a giraffe with a long neck",
        "a penguin standing",
        "a turtle with a shell",
        "a rabbit with long ears",
        "a bear face",
        "a frog sitting",
        "a pig face",
        "a cow with spots",
        "a mouse small",
        "a duck floating",
        "a snake long body",
        "a spider with legs",
        "a bee flying"
    ],

    "Flowers": [
        "a rose flower",
        "a tulip flower",
        "a daisy flower",
        "a sunflower",
        "a lotus flower",
        "a lily flower",
        "an orchid flower",
        "a cactus plant",
        "a mushroom",
        "a tree",
        "a leaf",
        "a palm tree",
        "a pine tree",
        "a flower with petals",
        "a clover",
        "a vine",
        "a bamboo",
        "a fern",
        "a bush",
        "a small plant"
    ],

    "Emojis": [
        "a happy face",
        "a sad face",
        "an angry face",
        "a crying face",
        "a laughing face",
        "a heart eyes face",
        "a sunglasses face",
        "a surprised face",
        "a winking face",
        "a kissing face",
        "a sleeping face",
        "a sick face",
        "a nerd face",
        "a cowboy face",
        "a clown face",
        "a skull",
        "a ghost",
        "an alien face",
        "a robot face",
        "a poop emoji"
    ],

    "Vehicles": [
        "a car",
        "a bus",
        "a train",
        "an airplane",
        "a helicopter",
        "a boat",
        "a ship",
        "a bicycle",
        "a motorcycle",
        "a truck",
        "a rocket",
        "a submarine",
        "a hot air balloon",
        "a scooter",
        "a skateboard",
        "a tractor",
        "an ambulance",
        "a fire truck",
        "a police car",
        "a taxi"
    ]
}
#medium
phrases_list_medium = {
    "Animals": [
        "a cat sleeping on a pillow",
        "a dog wagging its tail",
        "a fish in a bowl",
        "a bird on a branch",
        "a lion with a mane",
        "an elephant spraying water",
        "a monkey holding a banana",
        "a giraffe eating leaves",
        "a penguin on ice",
        "a turtle near water",
        "a rabbit eating a carrot",
        "a bear holding honey",
        "a frog on a lily pad",
        "a pig in mud",
        "a cow in a field",
        "a mouse holding cheese",
        "a duck swimming in a pond",
        "a snake coiled",
        "a spider on a web",
        "a bee near a flower"
    ],

    "Flowers": [
        "a rose with leaves",
        "a tulip in a pot",
        "a daisy with a stem",
        "a sunflower facing the sun",
        "a lotus on water",
        "a lily with long petals",
        "an orchid on a stem",
        "a cactus with spikes",
        "a mushroom with spots",
        "a tree with branches",
        "a leaf falling",
        "a palm tree on an island",
        "a pine tree in snow",
        "a blooming flower",
        "a clover with four leaves",
        "a hanging vine",
        "a bamboo forest",
        "a fern with many leaves",
        "ivy on a wall",
        "a round bush in a garden"
    ],

    "Emojis": [
        "a happy face with open mouth",
        "a sad face with tears",
        "an angry red face",
        "a crying face with big tears",
        "a laughing face with eyes closed",
        "a face with heart eyes",
        "a cool face with sunglasses",
        "a shocked face with open mouth",
        "a winking face smiling",
        "a face blowing a kiss",
        "a sleeping face with Z",
        "a sick face with thermometer",
        "a nerd face with glasses",
        "a cowboy face with hat",
        "a clown face with makeup",
        "a skull with cracks",
        "a ghost floating",
        "an alien with big eyes",
        "a robot with square eyes",
        "a smiling poop emoji"
    ],

    "Vehicles": [
        "a car on the road",
        "a bus with windows",
        "a train on tracks",
        "an airplane flying in the sky",
        "a helicopter with blades spinning",
        "a boat on water",
        "a large ship at sea",
        "a bicycle with a rider",
        "a motorcycle moving fast",
        "a truck carrying boxes",
        "a rocket launching",
        "a submarine underwater",
        "a hot air balloon in the sky",
        "a scooter on the street",
        "a skateboard on the ground",
        "a tractor in a farm",
        "an ambulance with a siren",
        "a fire truck with a ladder",
        "a police car with flashing lights",
        "a taxi picking up passengers"
    ]
}
#hard
phrases_list_hard = {
    "Animals": [
        "a cat sleeping under a table",
        "a dog chasing a ball",
        "a fish jumping out of water",
        "a bird flying over a tree",
        "a lion standing on a rock",
        "an elephant near a river",
        "a monkey swinging from a tree",
        "a giraffe beside a tree",
        "a penguin sliding on ice",
        "a turtle hiding in its shell",
        "a rabbit inside a hole",
        "a bear catching fish",
        "a frog jumping into water",
        "a pig rolling in mud",
        "a cow eating grass",
        "a mouse running away",
        "a duck flying over a pond",
        "a snake wrapped around a branch",
        "a spider hanging from a web",
        "a bee flying between flowers"
    ],

    "Flowers": [
        "a rose in a vase on a table",
        "a tulip field under the sun",
        "a daisy in the grass",
        "a sunflower in a field",
        "a lotus floating in a pond",
        "a lily beside water",
        "an orchid in a pot",
        "a cactus in the desert",
        "a mushroom in the forest",
        "a tree with birds on it",
        "a leaf on the ground",
        "a palm tree by the beach",
        "a pine tree in a forest",
        "flowers growing in a garden",
        "a clover in the grass",
        "a vine climbing a wall",
        "bamboo in a forest",
        "a fern under a tree",
        "ivy covering a wall",
        "a bush with flowers"
    ],

    "Emojis": [
        "a happy face with tears of joy",
        "a sad face looking down",
        "an angry face with steam",
        "a crying face covering eyes",
        "a laughing face leaning back",
        "a face with hearts around it",
        "a cool face with tilted sunglasses",
        "a shocked face with hands on cheeks",
        "a winking face with tongue out",
        "a face blowing a heart kiss",
        "a sleeping face on a pillow",
        "a sick face lying down",
        "a nerd face reading a book",
        "a cowboy face smiling",
        "a clown face juggling balls",
        "a skull with cracks and shadows",
        "a ghost flying at night",
        "an alien glowing eyes",
        "a robot with antenna",
        "a poop emoji with flies"
    ],

    "Vehicles": [
        "a car parked beside a house",
        "a bus stopping at a station",
        "a train passing through a tunnel",
        "an airplane above clouds",
        "a helicopter over a city",
        "a boat near the shore",
        "a ship in the ocean",
        "a bicycle leaning on a wall",
        "a motorcycle on a highway",
        "a truck on a bridge",
        "a rocket flying into space",
        "a submarine deep underwater",
        "a hot air balloon over mountains",
        "a scooter parked on a sidewalk",
        "a skateboard under a foot",
        "a tractor plowing a field",
        "an ambulance in traffic",
        "a fire truck near a building",
        "a police car chasing another car",
        "a taxi in a busy street"
    ]
}