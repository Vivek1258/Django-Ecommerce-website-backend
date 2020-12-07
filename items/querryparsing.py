
from ml_models import QPmodel


class QP(object):

	"""docstring for  QuerryParsingModel"""

	def __init__(self):
		super( QP , self).__init__()
		self.model = QPmodel.model


	def parse(self,querry):

		item_type, item_sub_type = self.model(querry)

		return {
		"item_type" : item_type,
		"item_sub_type" : item_sub_type
		}
		

