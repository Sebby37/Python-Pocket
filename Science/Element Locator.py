__author__ = "Kevin"
__Liscence  = "Unliscenced"
print("Hello, welcome to the Element Locator\n")

user_element = input("Input the symbol of your element: ")

def findElement(symbol = "H"):
    Elements = {
        #source = (https://en.wikipedia.org/wiki/List_of_chemical_elements)
        "H": "Hydrogen",
        "He": "Helium",
        "Li": "Lithium",
        "Be": "Beryllium",
        "B": "Boron",
        "C": "Carbon",
        "N": "Nitrogen",
        "O": "Oxygen",
        "F": "Fluorine",
        "Ne": "Neon",
        "Na": "Sodium",
        "Mg": "Magnesium",
        "Al": "Aluminium",
        "Si": "Silicon",
        "P": "Phosphours",
        "S": "Sulfur",
        "Cl": "Chlorine",
        "Ar": "Argon",
        "K": "Potassium",
        "Ca": "Calcium",
        "Sc": "Scandium",
        "Ti": "Titanium",
        "V": "Vanadium",
        "Cr": "Chromium",
        "Mn": "Manganese",
        "Fe": "Iron",
        "Co": "Colbolt",
        "Ni": "Nikel",
        "Cu": "Copper",
        "Zn": "Zinc",
        "Ga": "Gallium",
        "Ge": "Germanium",
        "As": "Arsenic",
        "Se": "Selenium",
        "Br": "Bromine",
        "Kr": "Krypton",
        "Rb": "Rubidium",
        "St": "Strontium",
        "Y": "Yittrium",
        "Zr": "Zinconium",
        "Nb": "Niobium",
        "Mo": "Molybdenum",
        "Tc": "Technetium",
        "Ru": "Ruthenium",
        "Rh": "Rhodium",
        "Pd": "Palladium",
        "Ag": "Silver",
        "Cd": "Cadmium",
        "In": "Indium",
        "Sn": "Tin",
        "Sb": "Anitmony",
        "Te": "Tellurium",
        "I": "Iodine",
        "Xe": "Xenon",
        "Cs": "Caesium",
        "Ba": "Barium",
        "La": "Lanthanum",
        "Ce": "Cerium",
        "Pr": "Praseodymium",
        "Nd": "Neodymium",
        "Pm": "Promethium",
        "Sm": "Samarium",
        "Eu": "Europium",
        "Gd": "Gadolinium",
        "Tb": "Terbium",
        "Dy": "Dysprosium",
        "Ho": "Holmium",
        "Er": "Erbium",
        "Tm": "Thulium",
        "Yb": "Yitterbium",
        "Lu": "Lutetium",
        "Hf": "Hafnium",
        "Ta": "Tantalum",
        "W": "Tungsten",
        "Re": "Rhenium",
        "Os": "Osmium",
        "Ir": "Iridium",
        "Pt": "Platinum",
        "Au": "Gold",
        "Hg": "Mercury",
        "Tl": "Thallium",
        "Pb": "Lead",
        "Bi": "Bismuth",
        "Po": "Polonium",
        "At": "Astatine",
        "Rn": "Radon",
        "Fr": "Francium",
        "Ra": "Radium",
        "Ac": "Actinium",
        "Th": "Thorium",
        "Pa": "Protactinium",
        "U": "Uranium",
        "Np": "Neptunium",
        "Pu": "Plutonium",
        "Am": "Americium",
        "Cm": "Curium",
        "Bk": "Berkelium",
        "Cf": "Californium",
        "Es": "Einsteinium",
        "Fm": "Fermium",
        "Md": "Mendelevium",
        "No": "Nobelium",
        "Lr": "Lawrencium",
        "Rf": "Rutherfordium",
        "Db": "Dubnium",
        "Sg": "Seaborgium",
        "Bh": "Bohrium",
        "Hs": "Hassium",
        "Mt": "Meitnerium",
        "Ds": "Darmstadtium",
        "Rg": "Roentgenium",
        "Cn": "Coppernicium",
        "Nh": "Nihonium",
        "Fl": "Flevorium",
        "Mc": "Moscovium",
        "Lv": "Livermorium",
        "Ts": "Tennessine",
        "Of": "Oganesson"
    }
    #for symbol in Elements.keys():
    if user_element in Elements:
        print(f"The element is:", Elements[user_element])
findElement(user_element)