import tkinter as tk
from tkinter import messagebox
from PyDictionary import PyDictionary

class Dictionary:
    def __init__(self):

        self.dictionary = PyDictionary()
        self.all_words = self.get_all_word()
    
    def get_all_word(self):
        list_of_word = ["apple", "airplane", "anchor", "alphabet", "avenue", "ant", "angle", "actor", "artist", "album", "aroma", "answer", "ancient", "animal", "angel", "ash", "august", "apricot", "arch", "arctic", "armadillo", "aspirin", "asteroid", "atom", "asterisk", "atmosphere", "atlas", "athlete", "attic", "auction", "audience", "author", "autumn", "avalanche", "award", "axe", "azure", "aquarium", "antenna", "alloy", "algebra", "algae", "albumen", "altitude", "amber", "ample", "amphibian", "amusement", "analysis", "anomaly",
                    "ball", "balloon", "bakery", "bamboo", "banana", "band", "banner", "barrel", "base", "basket", "bat", "beach", "beacon", "bean", "bear", "beast", "bed", "bee", "beef", "beer", "beetle", "bell", "belt", "bench", "berry", "bicycle", "bird", "biscuit", "blade", "blanket", "blast", "blimp", "block", "blossom", "boat", "body", "bolt", "bone", "book", "boot", "bottle", "bow", "box", "boy", "brain", "branch", "bread", "brick", "bridge", "broom", 
                    "car", "cat", "cake", "candle", "canyon", "cap", "card", "carpet", "cart", "castle", "cave", "chair", "chalk", "chance", "chart", "chase", "cheese", "cherry", "chest", "chicken", "child", "chimney", "chip", "chocolate", "church", "circle", "circus", "city", "cliff", "clock", "cloud", "clover", "coat", "cobra", "coffee", "coin", "comb", "comic", "compass", "computer", "cone", "copper", "coral", "corn", "cottage", "cotton", "couch", "cough", "country", "cow", 
                    "dog", "door", "desk", "duck", "doll", "dust", "dawn", "dance", "deer", "dart", "dime", "date", "dome", "dock", "drum", "dream", "drift", "dress", "drop", "disk", "dish", "dove", "dial", "daisy", "drink", "donkey", "denim", "diary", "ditch", "drive", "demon", "delta", "dingo", "doubt", "dwarf", "draw", "depot", "drill", "drain", "drake", "drape", "druid", "drone", "dance", "dance", "dingo", "delta", "decal", "douse", "diode"
                    "eagle", "earth", "echo", "edge", "eel", "egg", "elbow", "elephant", "emerald", "energy", "engine", "entry", "epic", "epoch", "equal", "eraser", "essay", "estate", "event", "ever", "evil", "exam", "exit", "extra", "eye", "eyebrow", "ear", "earn", "east", "easy", "eater", "eclipse", "eddy", "editor", "effect", "effort", "ego", "eight", "elapse", "elder", "elect", "element", "elite", "elope", "ember", "emblem", "emerge", "emit", "end"
                    "fish", "fork", "fox", "frog", "fan", "face", "fair", "fall", "farm", "fast", "fear", "feed", "feel", "film", "fire", "flag", "flame", "flash", "flat", "flood", "floor", "flower", "fly", "foam", "fog", "fold", "food", "foot", "force", "forest", "fork", "fort", "frame", "free", "freeze", "fresh", "friend", "frost", "fruit", "fuel", "full", "fun", "fuse", "fuzzy", "fiber", "fabric", "feather", "fence", "fever"
                    "goat", "gate", "gift", "goose", "grain", "grape", "grass", "green", "grid", "ground", "group", "grow", "guest", "guide", "guitar", "gum", "gym", "garage", "garden", "garlic", "gas", "gasp", "gear", "genius", "germ", "ghost", "giant", "globe", "glove", "glow", "glue", "goal", "goat", "gold", "good", "goose", "gown", "grade", "grain", "grant", "grape", "graph", "grass", "grave", "great", "greed", "grill"
                    "hat", "hand", "hawk", "heart", "hill", "house", "horse", "home", "hope", "hen", "honey", "horn", "hook", "hoop", "hose", "hot", "hour", "hug", "hum", "hut", "hawk", "health", "heat", "heir", "hero", "hill", "hint", "hip", "hire", "hit", "hobby", "hold", "hole", "holiday", "hollow", "holy", "home", "honey", "hood", "hoof", "hope", "horn", "horror", "horse", "host", "hot", "hour", "house", "hover"
                    "ice", "icon", "idea", "idol", "igloo", "ill", "image", "impact", "inch", "index", "ink", "inn", "input", "iron", "island", "issue", "item", "ivy", "iceberg", "iconic", "idea", "identify", "idiom", "idle", "ignite", "ignore", "illness", "illustrate", "image", "imagine", "impact", "implement", "impress", "improve", "impulse", "include", "income", "increase", "indicate", "indigo", "industry", "infant", "inform", "inject", "injury", "insect", "inside", "inspire"
                    "jam", "jar", "jet", "jewel", "job", "jog", "joy", "juice", "jump", "jungle", "junior", "jury", "jacket", "jaguar", "jail", "janitor", "jazz", "jeans", "jeep", "jelly", "jester", "jewel", "join", "joint", "joke", "jolly", "jolt", "journal", "journey", "judge", "juggle", "juice", "jump", "junk", "jury", "justice", "javelin", "jeopardy", "jersey", "jet", "job", "jog", "join", "joint", "joker", "jovial", "judo", "jump"
                    "kite", "key", "kid", "king", "knee", "knife", "knight", "knot", "koala", "kettle", "kangaroo", "karate", "kayak", "keel", "keep", "keg", "kernel", "keyboard", "kick", "kidney", "kiln", "kilo", "kimono", "kind", "kiss", "kit", "kite", "kitten", "knack", "knit", "knob", "knock", "knot", "know", "knowledge", "koala", "koi", "krill", "kudos", "knee", "knife", "knob", "knot", "known", "kayak", "keen", "kite", "kit", "kick"
                    "lamp", "land", "lake", "ladder", "lady", "lamb", "lamp", "language", "lark", "laser", "laugh", "lava", "law", "lawn", "lead", "leaf", "leap", "learn", "lease", "lemon", "lend", "lens", "leopard", "letter", "level", "library", "life", "lift", "light", "lime", "line", "link", "lion", "lip", "list", "litter", "live", "load", "loaf", "loan", "lock", "lodge", "log", "long", "look", "loop", "lord", "loud", "love"
                    "man", "map", "mango", "market", "mask", "mass", "mat", "match", "mate", "meal", "meat", "medal", "media", "melon", "menu", "mess", "metal", "meter", "microphone", "midnight", "might", "mile", "milk", "mill", "mind", "mine", "mint", "minute", "mirror", "miss", "mist", "mix", "mob", "model", "modern", "mold", "money", "month", "moon", "more", "morning", "moss", "mother", "mountain", "mouse", "mouth", "move", "mud", "muffin"
                    "nail", "name", "nap", "narrow", "nation", "nature", "navy", "neck", "need", "neon", "nest", "net", "news", "night", "nine", "noble", "node", "noise", "none", "noon", "north", "nose", "note", "notion", "novel", "number", "nurse", "nut", "nail", "name", "nature", "naughty", "navy", "neck", "need", "neon", "nest", "net", "news", "night", "nine", "noon", "north", "note", "novel", "number", "nurse", "nut"
                    "oak", "oat", "oasis", "oath", "ocean", "octopus", "oil", "olive", "onion", "opera", "orange", "orbit", "orchard", "order", "organ", "origin", "ornament", "ostrich", "otter", "outlet", "oven", "owl", "oxygen", "oyster", "oak", "oath", "ocean", "octopus", "oil", "olive", "onion", "opera", "orange", "orbit", "order", "organ", "origin", "ostrich", "otter", "outlet", "oven", "owl", "oxygen", "oyster", "ounce"
                    "palm", "panda", "pan", "pant", "paper", "parrot", "pass", "paste", "path", "peach", "peak", "pear", "peg", "pen", "pencil", "pepper", "person", "pet", "phone", "photo", "piano", "picnic", "pie", "pig", "pillar", "pin", "pine", "pipe", "pirate", "pizza", "place", "plane", "plant", "plate", "play", "plow", "plug", "plum", "plus", "pocket", "poem", "point", "pole", "police", "pond", "pony", "pool", "pop", "pot"
                    "quail", "quake", "quality", "quarter", "quartz", "queen", "query", "question", "quick", "quiet", "quill", "quilt", "quit", "quiz", "quote", "quiver", "quack", "quad", "quail", "quake", "quality", "quarter", "quartz", "queen", "query", "question", "quick", "quiet", "quill", "quilt", "quit", "quiz", "quote", "quiver", "quack", "quad", "quest", "queue", "quilt", "quirk", "quarry", "quota", "quorum", "quotient", "quintet", "quokka"
                    "rabbit", "race", "rack", "radar", "radio", "rail", "rain", "raise", "rake", "rally", "ranch", "range", "rank", "rap", "rat", "rate", "raven", "ray", "razor", "reach", "read", "ready", "real", "reason", "rebel", "record", "red", "reef", "refuse", "regret", "reign", "relay", "relax", "release", "relief", "remind", "rent", "repair", "repeat", "report", "request", "rescue", "reset", "rest", "retail", "retire", "return", "reveal"
                    "sack", "sad", "safe", "sail", "salt", "same", "sand", "sat", "save", "scale", "scan", "scar", "scene", "school", "scout", "scrap", "screw", "seal", "seat", "see", "seed", "seek", "seem", "seen", "self", "sell", "send", "sense", "serve", "set", "seven", "shade", "shake", "shame", "shape", "share", "shark", "sharp", "she", "sheep", "sheet", "shelf", "shell", "shift", "shine", "ship", "shirt", "shock", "shoe"
                    "talk", "take", "task", "tank", "tack", "tale", "tame", "tape", "tap", "tick", "tock", "teak", "teal", "term", "team", "twin", "town", "torn", "tart", "turf", "turn", "tarn", "tang", "tape", "tote", "tot", "ton", "top", "toe", "toad", "tea", "tie", "tip", "tall", "tell"
                    "umbrella", "uncle", "under", "uniform", "union", "unique", "unit", "universe", "university", "unknown", "up", "urban", "urge", "use", "user", "usual", "utility", "utmost", "utopia", "utter", "ugly", "ultra", "ultimate", "umpire", "unanimous", "uncover", "undergo", "underneath", "understand", "undertake", "undress", "uneven", "unfold", "unicorn", "unify", "unimaginable", "uninterested", "unite", "universal", "unleash", "unlock", "unoccupied", "unpack", "unseen", "unstable", "untidy", "untie", "until"
                    "vase", "vast", "vane", "value", "van", "vaccine", "vacuum", "vague", "valid", "valley", "valve", "vampire", "vanilla", "vanish", "variety", "various", "vase", "vault", "vector", "vehicle", "veil", "vein", "velvet", "vendor", "venture", "venue", "verb", "verify", "version", "vessel", "vest", "veteran", "vex", "vibe", "victim", "victory", "video", "view", "vigil", "vigor", "village", "vine", "vintage", "violin", "virtual", "virus", "visit", "visual", "vital"
                    "wall", "water", "wave", "wax", "web", "wheat", "wheel", "whip", "whistle", "wide", "wife", "wild", "will", "wind", "window", "wine", "wing", "winter", "wipe", "wire", "wise", "wish", "wit", "witch", "with", "wolf", "wood", "wool", "word", "work", "world", "worm", "worry", "worship", "worth", "wound", "wrap", "wreck", "wrench", "wrestle", "wrist", "write", "wrong", "wrote", "wrinkle", "wriggle", "wrestle", "wrought"
                    "x-ray", "xenon", "xerox", "xylem", "xylophone", "xenolith", "xenophobia", "xenon", "xylem", "xylophone", "x-axis", "xenopus", "xeric", "xeroderma", "xerography", "xerophyte", "xylene", "xylocarp", "xylotomy", "xanthan", "xanthate", "xanthi", "xenial", "xenogenesis", "xenon", "xerothermic", "xylophagous", "xylophage", "xylophone", "xanthous", "xantho", "xanthelasma", "xenobiotic", "xenobiology", "xenodochial", "xenogamy", "xenogeny", "xenogenesis", "xenograft", "xenolith", "xenon", "xenophobia", "xenopus", "xeric", "xeroderma", "xerography", "xerophilous"
                    "yarn", "yard", "yawn", "year", "yellow", "yes", "yesterday", "yet", "yield", "yogurt", "yoke", "young", "youth", "yoyo", "yucca", "yacht", "yak", "yam", "yap", "yard", "yarn", "year", "yell", "yelp", "yen", "yeast", "yes", "yet", "yield", "yolk", "yoyo", "yucca", "yank", "yearn", "yellow", "yes", "yesterday", "yet", "yield", "young", "youth", "yule", "yummy", "yacht", "yak", "yam"
                    "zebra", "zero", "zinc", "zipper", "zone", "zoo", "zoom", "zeal", "zenith", "zigzag", "zip", "zombie", "zonal", "zygote", "zodiac", "zoology", "zephyr", "zombie", "zigzag", "zoom", "zone", "zealot", "zen", "zeolite", "zucchini", "zooid", "zootomy", "zoster", "zygoma", "zymology", "zymurgy", "zircon", "zirconium", "zebrawood", "zebrine", "zephyr", "zeppelin", "zeroth", "zircaloy", "zoster", "zygospore", "zymogram", "zymogen", "zoologist", "zoolatry", "zoography", "zoogamy"
                    ]
        return list_of_word

    def check_spelling(self, word):
        lowercase_word = word.lower()
        if self.dictionary.meaning(lowercase_word):
            meaning = self.dictionary.meaning(lowercase_word)
            meaning_str = "\n".join(f"{key.capitalize()}: {', '.join(value)}" for key, value in meaning.items())
            
            synonyms = self.dictionary.synonym(lowercase_word)
            antonyms = self.dictionary.antonym(lowercase_word)

            synonym_str = ", ".join(synonyms[:3]) if synonyms else "No synonyms found"
            antonym_str = ", ".join(antonyms[:3]) if antonyms else "No antonyms found"

            messagebox.showinfo("Meaning", f"Definition! {lowercase_word}!\n\nMeaning:\n{meaning_str}\n\nSynonyms:\n{synonym_str}\n\nAntonyms:\n{antonym_str}")
        else:
            all_words = self.get_all_word()
            closest_words = sorted(all_words, key=lambda x: self.edit_distance(lowercase_word, x))[:3]
            closest_words_str = ", ".join(closest_words)
                # Check if any suggestion has a similar prefix with the input word
            suggestions_with_prefix = [w for w in closest_words if w.startswith(lowercase_word)]
            if suggestions_with_prefix:
                    closest_words_str = ", ".join(suggestions_with_prefix)
            messagebox.showwarning("Spell Checker", f"Incorrect Spelling! Did you mean: {closest_words_str}?")

    
    @staticmethod
    def edit_distance(s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        i = j = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                cost = 0 if s1[i - 1] == s2[j - 1] else 1
                dp[i][j] = min(dp[i - 1][j] + 1,       
                            dp[i][j - 1] + 1,       
                            dp[i - 1][j - 1] + cost 
                            )
        return dp[m][n]

class DictionaryApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Dictionary")
        self.geometry("400x300")
        self.resizable(width=False, height=False)
        self.config(bg="gray")

        label = tk.Label(self, text="Enter a word:",fg= "cyan" ,bg="gray",font=("Cascadia Code", 12))
        label.pack(padx=5, pady=30)

        self.entry = tk.Entry(self, font=("Cascadia Code", 12))
        self.entry.pack(padx=0)

        check_button = tk.Button(self, text="Search", bg= "green", fg="white", command=self.check_spelling, font=("Cascadia Code", 12))
        check_button.pack(pady=10)

        close_button = tk.Button(self, text="Exit", bg="red", fg="black", command=self.quit, font=("Cascadia Code", 12))
        close_button.pack(pady=5)

    def check_spelling(self):
        word = self.entry.get().strip()
        if word:
            spell_checker_facade = Dictionary()
            spell_checker_facade.check_spelling(word)
        else:
            messagebox.showwarning("Spell Checker", "Please enter a word to check.")

if __name__ == "__main__":
    app = DictionaryApp()
    app.mainloop()