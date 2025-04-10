from colors import Colors
import pygame
from position import Position

class Block:
	def __init__(self, id):
		self.id = id							# ID bloku (1–7), slouží i pro výběr barvy
		self.cells = {}						 	# Slovník s rotacemi a pozicemi bloků
		self.cell_size = 30						# Velikost jednoho čtverce bloku
		self.row_offset = 0						# Posunutí bloku dolů (řádky)
		self.column_offset = 0					# Posunutí bloku do strany (sloupce)
		self.rotation_state = 0					# Určuje, jaká rotace bloku je aktuální
		self.colors = Colors.get_cell_colors() 	# Získá barvy podle ID

	# Posune blok o daný počet řádků a sloupců
	def move(self, rows, columns):
		self.row_offset += rows
		self.column_offset += columns

	# Vrací aktuální pozice všech čtverců bloku podle posunutí a rotace
	def get_cell_positions(self):
		tiles = self.cells[self.rotation_state]	# Získá tvar podle aktuální rotace
		moved_tiles = []
		for position in tiles:
			# Posune každý čtverec podle offsetu
			position = Position(position.row + self.row_offset, position.column + self.column_offset)
			moved_tiles.append(position)
		return moved_tiles

	# Otočí blok (změní rotaci)
	def rotate(self):
		self.rotation_state += 1
		if self.rotation_state == len(self.cells): 	# Pokud už jsme za poslední rotací
			self.rotation_state = 0		# Vrať se na začátek

	# Vrátí poslední rotaci (např. když rotace není možná)
	def undo_rotation(self):
		self.rotation_state -= 1
		if self.rotation_state == -1:
			self.rotation_state = len(self.cells) - 1

	# Vykreslí blok na obrazovku (screen)
	def draw(self, screen, offset_x, offset_y):
		tiles = self.get_cell_positions()	# Získá pozice všech čtverců bloku
		for tile in tiles:
			tile_rect = pygame.Rect(offset_x + tile.column * self.cell_size,
				offset_y + tile.row * self.cell_size, self.cell_size -1, self.cell_size -1)

			# Vykreslí čtverec s příslušnou barvou podle ID
			pygame.draw.rect(screen, self.colors[self.id], tile_rect)