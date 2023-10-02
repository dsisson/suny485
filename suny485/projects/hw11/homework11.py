def get_formal_name_original(fruit):
    """
    Get the scientific name for the supplied `fruit` common name.

    :param fruit: str, common name for a fruit
    :return formal_name: str, the formal name for the supplied fruit
    """
    fruit_dict = {
        'apple': 'Malus domestica',
        'banana': 'Musa acuminata',
        'orange': 'Citrus × sinensis',
        'strawberry': 'Fragaria × ananassa',
        'grape': 'Vitis vinifera',
        'pineapple': 'Ananas comosus',
        'mango': 'Mangifera indica',
        'blueberry': 'Vaccinium corymbosum',
        'peach': 'Prunus persica',
        'watermelon': 'Citrullus lanatus',
        'cherry': 'Prunus avium',
        'pear': 'Pyrus',
        'plum': 'Prunus domestica',
        'raspberry': 'Rubus idaeus',
        'kiwi': 'Actinidia deliciosa',
        'lemon': 'Citrus limon',
        'avocado': 'Persea americana',
        'pomegranate': 'Punica granatum',
        'cranberry': 'Vaccinium macrocarpon',
        'grapefruit': 'Citrus × paradisi'
    }

    formal_name = fruit_dict[fruit]

    return formal_name


def get_formal_name_improved(fruit):
    """
    Get the scientific name for the supplied `fruit` common name.

    :param fruit: str, common name for a fruit
    :return formal_name: str, the formal name for the supplied fruit
    """
    fruit_dict = {
        'apple': 'Malus domestica',
        'banana': 'Musa acuminata',
        'orange': 'Citrus × sinensis',
        'strawberry': 'Fragaria × ananassa',
        'grape': 'Vitis vinifera',
        'pineapple': 'Ananas comosus',
        'mango': 'Mangifera indica',
        'blueberry': 'Vaccinium corymbosum',
        'peach': 'Prunus persica',
        'watermelon': 'Citrullus lanatus',
        'cherry': 'Prunus avium',
        'pear': 'Pyrus',
        'plum': 'Prunus domestica',
        'raspberry': 'Rubus idaeus',
        'kiwi': 'Actinidia deliciosa',
        'lemon': 'Citrus limon',
        'avocado': 'Persea americana',
        'pomegranate': 'Punica granatum',
        'cranberry': 'Vaccinium macrocarpon',
        'grapefruit': 'Citrus × paradisi'
    }

    # made two improvements:
    #   1. lower-cased the `fruit` string to normalize case
    #   2. trap for attribute errors (because only strings have case)
    #      and raise KeyError
    try:
        formal_name = fruit_dict[fruit.lower()]
    except AttributeError:
        raise KeyError(f"Error: '{fruit}' is not a valid key!")

    return formal_name
