class _Colors(object):
	esc = '\x1b['
	colors = {
		'reset':     '0',
		'bright':    '1',
		'underline': '4',
		'reverse':   '7',
	}
	color_names = 'black','red','green','yellow','blue','magenta','cyan','white'

	def __init__(self):
		for i,color in enumerate(self.color_names):
			self.colors[color] = str(i + 30)
		self.colors['purple'] = self.colors['magenta']


	def format(self, text, color):
		"""Format text with a color and attributes:
			color   - normal color
			!color! - bright color
			*color* - reverse color (black on color)
			_color_ - underlined color

			Supported colors: black, red, green, yellow, blue, magenta (or
			purple), cyan, white.
		"""
		if color is None:
			return text
		codes = ''
		while(color and color[0] == color[-1] and color[0] in '!*_'):
			if color[0] == '*':
				codes += self.colors['reverse'] + ';'
				color = color[1:-1]
			elif color[0] == '!':
				codes += self.colors['bright'] + ';'
				color = color[1:-1]
			elif color[0] == '_':
				codes += self.colors['underline'] + ';'
				color = color[1:-1]
		if color:
			codes += self.colors[color] + 'm'
		else:
			codes += 'm'

		return self.esc + codes + text + self.esc + self.colors['reset'] + 'm'

import sys
if sys.platform == 'win32':
	colortext = lambda x: x
else:
	colortext = _Colors().format
