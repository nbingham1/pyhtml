import HTMLParser
import html
import css

class Parser(HTMLParser.HTMLParser):
	def __init__(self):
		self.syntax = html.Document()
		self.stack = [self.syntax]
		HTMLParser.HTMLParser.__init__(self)

	def handle_starttag(self, tag, attrs):
		dattrs = dict(attrs)
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

	def handle_endtag(self, tag):
		if tag == self.stack[-1].name:
			self.stack.pop()

	def handle_data(self, data):
		if self.stack and data:
			self.stack[-1] << data

	def handle_entityref(self, data):
		if self.stack and data:
			self.stack[-1] << self.unescape("&" + data + ";")


def walk(syntax, func, parent=None, left=None):
	if isinstance(syntax, html.Tag):
		for i,elem in enumerate(syntax.content):
			syntax.content[i] = walk(elem, func, syntax, syntax.content[i-1] if i > 0 else None)
		return func(syntax, parent, left)
	else:
		return syntax

