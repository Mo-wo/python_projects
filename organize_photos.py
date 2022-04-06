import os


def extract_place(filename):
    parts = filename.split("_")
    place_name = parts[1]
    return place_name


def make_place_directories(places):
    for place in places:
        os.mkdir(place)


def organize_photos(directory):
    # Change working directory to the directory to be organized
    os.chdir(directory)

    # Extract place names from files in directory
    originals = os.listdir()
    places = []

    for filename in originals:
        place = extract_place(filename)
        if place not in places:
            places.append(place)

    # Make place directories
    make_place_directories(places)

    # Move Files to directories
    for filename in originals:
        place = extract_place(filename)
        path_name = os.path.join(place, filename)
        os.rename(filename, path_name)

# organize_photos("Photos")
print("TEST!")
