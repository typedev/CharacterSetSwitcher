# RoboFont Script
# CharacterSet Switcher
# Alexander Lubovenko
# http://github.com/typedev

from vanilla import *
from mojo.UI import *
from robofab.world import CurrentFont
from defconAppKit.windows.baseWindow import BaseWindowController


extversion = 'v0.1'

class CharsetsSwitcherWindow(BaseWindowController):
	def __init__ (self):
		self.w = FloatingWindow((230, 100), title = 'CharacterSet Switcher ' + extversion)
		self.w.cbCharsetsList = ComboBox((20, 20, -20, 21),
		                                 getCharacterSets().keys(),
		                                 callback = self.cbCharsetsListCallback)
		self.w.btnApply = Button((-80, 50, 60, 21),
		                         title = 'Apply',
		                         callback = self.btnApplyCallback)
		self.w.open()

	def cbCharsetsListCallback (self, info):
		pass

	def btnApplyCallback (self, info):
		font = CurrentFont()
		charsetName = self.w.cbCharsetsList.get()
		font.lib['public.glyphOrder'] = getCharacterSets()[charsetName]
		font.glyphOrder = font.lib['public.glyphOrder']
		print 'CharacterSet switched to', charsetName


CharsetsSwitcherWindow()