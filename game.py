from grid import Grid
from blocks import *
import random
import pygame
import json


class Game:
    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.high_score = self.load_high_score()  # Load the saved high score

    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        self.score += move_down_points

        # Update high score if current score is higher
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()  # Save the new high score

    def load_high_score(self):
        try:
            with open("highscore.json", "r") as file:
                data = json.load(file)
                return data.get("high_score", 0)
        except (FileNotFoundError, json.JSONDecodeError):
            return 0  # Default to 0 if file doesn't exist or is invalid

    def save_high_score(self):
        with open("highscore.json", "w") as file:
            json.dump({"high_score": self.high_score}, file)

    def reset(self):
        self.grid.reset()
        self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0
        self.game_over = False

    def get_random_block(self):
        # Když dojdou bloky, znovu se vytvoří seznam všec
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), OBlock(), SBlock(), TBlock(), ZBlock()]
        # Náhodně vybere blok a odstraní ho ze seznamu
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    def move_left(self):
        # Posune blok doleva
        self.current_block.move(0, -1)
        # Pokud není uvnitř nebo nesedí, vrátí zpět
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)

    def move_right(self):
        # Posune blok doprava
        self.current_block.move(0, 1)
        # Pokud není uvnitř nebo nesedí, vrátí zpět
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, -1)

    def move_down(self):
        # Posune blok dolů
        self.current_block.move(1, 0)
        # Pokud nesedí, posune zpět a zablokuje ho (uloží do mřížky)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0)
            self.lock_block()

    def lock_block(self):
        # Získá pozice buněk aktuálního bloku
        tiles = self.current_block.get_cell_positions()
        # Uloží je do mřížky (blok "spadl" a už se nehýbe)
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        # Nastaví nový aktuální blok a připraví další
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        # Smaže plné řádky a přidá body
        rows_cleared = self.grid.clear_full_rows()
        if rows_cleared > 0:
            self.update_score(rows_cleared, 0)
        # Pokud nový blok nejde umístit, hra končí
        if self.block_fits() == False:
            self.game_over = True

    def block_fits(self):
        # Kontroluje, jestli blok může být na aktuální pozici (nenaráží)
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True

    def rotate(self):
        #otočí blok
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()


    def block_inside(self):
        # Kontroluje, jestli je blok uvnitř hracího pole
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    def draw(self, screen):
        # Vykreslí mřížku a aktuální blok
        self.grid.draw(screen)
        self.current_block.draw(screen, 11, 11)

        # Vykreslí blok, který přijde jako další (na základě typu bloku se mění pozice)
        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)


