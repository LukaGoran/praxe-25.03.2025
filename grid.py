import pygame
from colors import Colors

class Grid:
	def __init__(self):
		self.num_rows = 20		# Počet řádků mřížky (výška hrací plochy)
		self.num_cols = 10		# Počet sloupců mřížky (šířka hrací plochy)
		self.cell_size = 30		# Velikost jednoho čtverce (pixely)
		# Vytvoření mřížky naplněné nulami (0 = prázdná buňka)
		self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
		self.colors = Colors.get_cell_colors()	# Načtení barev podle čísel

	# Pomocná funkce pro výpis celé mřížky do konzole
	def print_grid(self):
		for row in range(self.num_rows):
			for column in range(self.num_cols):
				print(self.grid[row][column], end = " ")
			print()

	# Zjišťuje, jestli je daná pozice uvnitř mřížky
	def is_inside(self, row, column):
		if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
			return True
		return False

	# Zjišťuje, jestli je daná buňka prázdná (má hodnotu 0)
	def is_empty(self, row, column):
		if self.grid[row][column] == 0:
			return True
		return False

	# Zjišťuje, jestli je daný řádek plný (neobsahuje žádnou nulu)
	def is_row_full(self, row):
		for column in range(self.num_cols):
			if self.grid[row][column] == 0:
				return False
		return True

	# Vyčistí (vynuluje) jeden konkrétní řádek
	def clear_row(self, row):
		for column in range(self.num_cols):
			self.grid[row][column] = 0

	# Posune řádek o `num_rows` dolů (používá se při odstraňování řádků)
	def move_row_down(self, row, num_rows):
		for column in range(self.num_cols):
			self.grid[row+num_rows][column] = self.grid[row][column]
			self.grid[row][column] = 0

	# Vyčistí všechny plné řádky a posune ostatní dolů
	def clear_full_rows(self):
		completed = 0	# Počet vyčištěných řádků
		for row in range(self.num_rows-1, 0, -1):	# Prochází odspodu nahoru
			if self.is_row_full(row):
				self.clear_row(row)
				completed += 1
			elif completed > 0:
				self.move_row_down(row, completed)
		return completed	# Vrací počet vyčištěných řádků

	# Resetuje celou mřížku do původního (prázdného) stavu
	def reset(self):
		for row in range(self.num_rows):
			for column in range(self.num_cols):
				self.grid[row][column] = 0

	# Vykreslí celou mřížku na obrazovku
	def draw(self, screen):
		for row in range(self.num_rows):
			for column in range(self.num_cols):
				cell_value = self.grid[row][column] # Hodnota buňky (0 = prázdná, 1–7 = blok)
				# Vytvoří obdélník pro danou buňku
				cell_rect = pygame.Rect(column*self.cell_size + 11, row*self.cell_size + 11,
				self.cell_size -1, self.cell_size -1)
				# Vykreslí obdélník s příslušnou barvou
				pygame.draw.rect(screen, self.colors[cell_value], cell_rect)
