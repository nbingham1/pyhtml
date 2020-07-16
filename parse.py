import pyhtml.html as html
import pyhtml.css as css
from collections import OrderedDict

class Parser(object):
	def __init__(self):
		self.syntax = html.Document()
		self.stack = [self.syntax]

	def start(self, tag, attrs):
		dattrs = dict(attrs)
		if "style" in dattrs:
			styles = [prop.split(":") for prop in dattrs["style"].split(";")]
			dattrs["style"] = css.Style(OrderedDict({
				key.strip(): value.strip()
				for key, value in styles
			}))

		if tag in ["area", "base", "br", "col", 
							 "command", "embed", "hr", "img", 
							 "input", "keygen", "link", "meta", 
							 "param", "source", "track", "wbr"]:
			if self.stack:
				self.stack[-1] << html.STag(tag, dattrs, inline=True)
		else:
			insert = html.Tag(tag, list(), dattrs, inline=True)
			if self.stack:
				self.stack[-1] << insert
			self.stack.append(insert)

	def end(self, tag):
		if tag == self.stack[-1].name:
			self.stack.pop()

	def data(self, data):
		if self.stack and data:
			self.stack[-1] << data

	def close(self):
		return self

def walk(syntax, func, parent=None, left=None):
	if isinstance(syntax, html.Tag):
		for i,elem in enumerate(syntax.content):
			syntax.content[i] = walk(elem, func, syntax, syntax.content[i-1] if i > 0 else None)
		return func(syntax, parent, left)
	else:
		return syntax

