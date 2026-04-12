

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
#medium
phrases_list_medium = {
    "Animals & Actions": [
        "a cat stretching its back",
        "a dog catching a frisbee",
        "a fish jumping out of water",
        "a bird building a nest",
        "a lion yawning showing teeth",
        "an elephant spraying water",
        "a monkey hanging by its tail",
        "a giraffe eating leaves from a tall tree",
        "a penguin sliding on its belly",
        "a turtle hiding in its shell",
        "a rabbit hopping over a log",
        "a bear scratching its back on a tree",
        "a frog catching a fly with its tongue",
        "a pig wearing a crown",
        "a cow jumping over the moon",
        "a mouse peeking out of a hole",
        "a duck wearing a rain hat",
        "a snake wrapped around a branch",
        "a spider dangling from a thread",
        "a bee stuck inside a jar"
    ],

    "Food & Objects": [
        "a pizza missing one slice",
        "a burger stacked very high",
        "a hot dog in a bun with mustard zigzag",
        "a melting ice cream cone with drips",
        "a cupcake with a cherry on top",
        "a donut with colorful sprinkles",
        "a banana peel on the floor",
        "a loaf of bread sliced in the middle",
        "a teapot pouring tea into a cup",
        "a leaking faucet with a single drop",
        "a lightbulb glowing above a head",
        "a closed treasure chest",
        "a key stuck inside a lock",
        "a clock with its hands at midnight",
        "a pair of scissors cutting paper",
        "a pencil writing on its own",
        "an open book with pages flying",
        "a broken umbrella blown inside out",
        "a ladder leaning against a cloud",
        "a balloon tied to a heavy brick"
    ],

    "Emotions & Faces": [
        "a face looking up with eyes closed",
        "a face peeking around a corner",
        "a face with a finger to lips shushing",
        "a face eating a lemon sour",
        "a face holding back a sneeze",
        "a face sweating nervously with a smile",
        "a face crying but trying to smile",
        "a face rolling eyes upward",
        "a face with dollar signs for eyes",
        "a face with steam coming out of ears",
        "a face with a lightbulb above it",
        "a face underwater holding breath",
        "a face in the dark with wide eyes",
        "a face disguised with a fake nose and glasses",
        "a face looking in a mirror seeing something different",
        "a face with a zipper over the mouth",
        "a face wearing a monocle",
        "a face with a unibrow",
        "a face wearing headphones",
        "a face with a crown slightly tilted"
    ],

    "Scenes & Settings": [
        "a house on a steep hill",
        "a boat on a stormy sea with lightning",
        "a campfire with marshmallows on sticks",
        "a swing set in an empty park",
        "a door slightly open with light spilling out",
        "a snowman melting in the sun",
        "a city skyline reflected in sunglasses",
        "a bridge collapsing at one end",
        "a staircase leading up into clouds",
        "a car driving on a winding road",
        "a fishbowl with a castle inside",
        "a kite tangled in power lines",
        "a window with raindrops racing down",
        "a streetlamp flickering at dusk",
        "a well with a bucket halfway down",
        "a mailbox overflowing with letters",
        "a telescope pointed at the moon",
        "a cactus with a single flower blooming",
        "a fence with a small hole at the bottom",
        "a hammock tied between two palm trees"
    ]
}
#hard
phrases_list_hard = {
    "Absurd Interactions": [
        "a fish wearing a diving helmet filled with water",
        "a dog walking a human on a leash",
        "a mouse trap holding a slice of cheese hostage",
        "a birdcage with the door open but the bird sleeping inside",
        "an elephant balancing on a beach ball",
        "a snail leaving a glowing trail of slime",
        "a cat looking in a mirror and seeing a lion reflection",
        "a skeleton watering a living flower",
        "a giraffe wearing a too-short scarf",
        "a pig flying with tiny angel wings",
        "a penguin in a desert next to a cactus",
        "a bear trying to fit through a cat door",
        "a spider knitting a web into the shape of a heart",
        "a turtle with a rocket strapped to its shell",
        "a cow being abducted by a tiny UFO",
        "a frog wearing a crown and sitting on a lily pad throne",
        "an octopus juggling its own detached arms",
        "a squirrel burying a lightbulb in a flower pot",
        "a flamingo standing on one leg holding an umbrella with the other foot",
        "a chameleon on a mirror completely mismatched in color"
    ],

    "Complex Scenes & Metaphors": [
        "a lightbulb inside a head half filled with water and a ship",
        "a clock melting over the edge of a table",
        "a tree growing upside down with roots in the clouds",
        "a keyhole shaped exactly like a person's silhouette",
        "a house of cards being built on the back of a sleeping cat",
        "a door floating in the middle of the ocean",
        "a ladder leaning against the moon with one footprint on a rung",
        "a person's shadow detaching from their feet and waving goodbye",
        "a broken hourglass with sand spilling upward",
        "a teacup holding a tiny thunderstorm with lightning",
        "a pair of eyes peeking out from a crack in the sky",
        "a candle burning at both ends held by a robot hand",
        "a paper boat floating in a puddle reflecting a different world",
        "a bookshelf where the books are arranged in rainbow order but one is missing",
        "a wall with a painted hole that looks so real a cartoon character is walking into it",
        "a globe where the land is made of puzzle pieces falling off",
        "an iceberg with a massive glowing neon sign underwater",
        "a pair of scissors cutting a hole in the fabric of the background",
        "a telescope looking at the back of the viewer's own head",
        "a mousetrap baited with a fully set dinner table"
    ],

    "Emoji & Abstract Expressions (Advanced)": [
        "a face where one half is smiling and the other half is melting",
        "a face made entirely of geometric shapes falling apart",
        "a face with a zipper for a mouth but the zipper is slightly open revealing static",
        "a face crying but the tears are floating upward into a cloud",
        "a face wearing a mask that looks identical to the face underneath",
        "a face where the eyes are replaced with spinning loading icons",
        "a face looking through a magnifying glass making one eye comically huge",
        "a face with a storm cloud inside its head visible through a window",
        "a face screaming but the sound is represented by a visible jagged line bouncing off walls",
        "a face with a plant growing out of the top of its head",
        "a face being erased by a giant pencil from the bottom up",
        "a face as a cracked porcelain doll with darkness inside the cracks",
        "a face with a third eye that is a simple closed door",
        "a face behind frosted glass with a hand wiping a peephole",
        "a face made of stone but the lips are moving slightly",
        "a face where the nose is a light switch turned to the 'off' position",
        "a face with a finger puppet on its thumb giving a side-eye",
        "a face reflected in a spoon upside down and distorted",
        "a face wearing glasses that show a reflection of a completely different face",
        "a face inside a thought bubble thinking about its own thought bubble"
    ],

    "Surreal Vehicles & Tech": [
        "a bicycle with square wheels riding down a staircase",
        "a hot air balloon tangled in its own strings dragging a tree",
        "a car driving on the ceiling of a tunnel with wheels pointed up",
        "a submarine flying through clouds dropping anchor on a bird",
        "a rocket ship made of pencils and erasers",
        "a train track that loops like a rollercoaster knot",
        "a helicopter with leaves instead of blades hovering silently",
        "a sailboat where the sail is a giant closed eye",
        "a robot vacuum cleaner fighting a dog over a bone",
        "a typewriter with keys that are tiny trampolines",
        "a satellite dish aimed at a houseplant",
        "a clockwork robot winding its own key in its back",
        "a spaceship crashing into an invisible wall leaving a crack in the air",
        "a tractor tilling a field of computer keyboards",
        "a cable car stuck halfway with a yeti inside",
        "a motorcycle with a sidecar containing a full orchestra",
        "a plane towing a banner that says nothing but a question mark",
        "a vending machine in the middle of a jungle with fresh snow on top",
        "a wheelbarrow carrying a single enormous diamond",
        "a traffic light with four colors and all are lit at once"
    ]
}