import json
class SchoolImages:
    def __init__(self, file_name):
        json_data = open(file_name, "r")
        rooms = json.load(json_data)
        self.floors = rooms["floors"]

    def create_image_list(self, room):
        images = []
        classroom_found_floor = None
        classroom_found = None
        for floor in self.floors:
            for classroom in floor:
                if floor[classroom] == room:
                    classroom_found_floor = floor
                    classroom_found = classroom
        for floor in self.floors:
            if floor != classroom_found_floor:
                images.append(floor["default"])
            else:
                images.append(floor[classroom_found])

        return images
