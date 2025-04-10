class Colors:
	#barvy blocku
	tmava_seda = (26, 31, 40)
	zelena = (0, 255, 0)
	cervena = (255, 0, 0)
	oranzova = (226, 116, 17)
	zluta = (237, 234, 4)
	fialova = (166, 0, 247)
	tyrkysova = (21, 204, 209)
	modra = (0, 0, 255)
	#barvy čísel a rectanglu
	bila = (255, 255, 255)
	tmava_modra = (44, 44, 127)
	#barvy na pozadí
	svetla_modra = (59, 85, 162)
	cerna = (0, 0, 0)
	lososova = (255, 102, 102)

	@classmethod
	def get_cell_colors(cls):
		return [cls.tmava_seda, cls.zelena, cls.cervena, cls.oranzova, cls.zluta, cls.fialova, cls.tyrkysova, cls.modra]