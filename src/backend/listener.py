class Listener():
	def __init__(self):
		self.is_listening = False

	def notify(self, event):
		if self.is_listening:
			self.handle_event(event)

	def handle_event(self, event):
		pass