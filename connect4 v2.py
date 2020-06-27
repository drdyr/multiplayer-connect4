import pygame
import sys

pygame.init()
clock = pygame.time.Clock()


class Board:
    def __init__(self):
        self.slots = []
        self.entry_slots = []
        self.disks = []
        for i in range(7):
            self.entry_slots.append(EntrySlot(i))
            for j in range(6):
                self.slots.append(Slot(i, j))

    def add_disk(self, disk):
        self.disks.append(disk)

    def draw(self):
        for slot in self.slots:
            slot.draw()
        for entry_slot in self.entry_slots:
            entry_slot.draw()
        for disk in self.disks:
            disk.draw()

class Slot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.colour = white
        self.rect = (100 * self.x + 15, 100 * self.y + 15, 70, 70)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def draw(self):
        self.rect = (100 * self.x + 15, 100 * self.y + 35, 70, 70)
        pygame.draw.ellipse(screen, self.colour, self.rect)


class EntrySlot:
    def __init__(self, x):
        self.x = x
        self.rect = (100 * self.x, 0, 100, 20)
        self.colour = black

    def draw(self):
        if self.is_cursor():
            self.colour = green
        else:
            self.colour = black
        pygame.draw.rect(screen, self.colour, self.rect)

    def is_cursor(self):
        return self.x * 100 < pygame.mouse.get_pos()[0] < (self.x + 1) * 100 and 0 < pygame.mouse.get_pos()[1] < 20

    def create_disk(self):
        pass


class Disk:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour
        self.rect = (100 * self.x + 15, 100 * self.y + 15, 70, 70)

    def draw(self):
        print("drawing disk")
        self.rect = (100 * self.x + 15, 100 * self.y + 35, 70, 70)
        pygame.draw.ellipse(screen, self.colour, self.rect)


white = (255, 255, 255)
yellow = (255, 255, 0)
red = (255, 0, 0)
blue = (50, 50, 255)
grey = (150, 150, 150)
black = (0, 0, 0)
green = (0, 255, 0)

screen = pygame.display.set_mode((700, 620))
screen.fill(blue)

board = Board()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for entry_slot in board.entry_slots:
                if entry_slot.is_cursor():
                    board.add_disk(Disk(entry_slot.x, 0, red))

    board.draw()
    pygame.display.flip()
    clock.tick(60)