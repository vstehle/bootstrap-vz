import base


class Manifest(base.Manifest):
	def validate(self, data):
		from os import path
		schema_path = path.normpath(path.join(path.dirname(__file__), 'manifest-schema.json'))
		self.schema_validate(data, schema_path)
		super(Manifest, self).validate(data)

	def parse(self, data):
		super(Manifest, self).parse(data)
		self.credentials    = data['credentials']
		self.virtualization = data['virtualization']
