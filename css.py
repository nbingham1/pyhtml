class Style:
	def __init__(self, prop = dict()):
		self.prop = dict()
		for key,value in prop.iteritems():
			self.set(key, value)

	def __str__(self):
		return " ".join(self.emit())

	def emit(self):
		result = []
		for key,value in self.prop.iteritems():
			result.append(str(key) + ": " + str(value) + ";")

	def get(self, key):
		return self.prop[key]

	def set(self, key, value):
		if key == "background":
		elif key == "border":
		elif key == "border-bottom":
		elif key == "border-image":
		elif key == "border-left":
		elif key == "border-radius":
		elif key == "border-right":
		elif key == "border-top":
		elif key == "margin":
		elif key == "padding":
		elif key == "font":
		elif key == "list-style":
		elif key == "animation":
		elif key == "outline":
		elif key == "column-rule":
		else:
			self.prop[key] = value

	def __getitem__(self, key):
		return self.get(key)

	def __setitem__(self, key, value):
		self.set(key, value)

class Css:
	def __init__(self, elems = dict()):
		self.elems = elems

	def __str__(self):
		return "\n".join(self.emit())

	def emit(self):
		result = []
		for selector,style in self.elems.iteritems():
			result.append(selector + " {")
			lines = style.emit()
			for line in lines:
				result.append("\t" + line)
			result.append("}")
			result.append("")
		return result

	
