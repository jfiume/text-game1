class Room(object):

    def enter(self):
        exit(1)

class Engine(object):

    def __init__(self, room_map):
        self.room_map = room_map

    def play(self):
        current_room = self.room_map.first_room()
        last_room = self.room_map.next_room('finished')

        while current_room != last_room:
            next_room_name = current_room.enter()
            current_room = self.room_map.next_room(next_room_name)

        # be sure to print out the last scene
        current_room.enter()
