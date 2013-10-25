from datastore.core import Query

class ManagedQuery(Query):
  '''Query that knows its manager so that it can run directly'''

  def __init__(self, key, manager=None):
    super(ManagedQuery, self).__init__(key)
    # The manager to perform this query
    self._manager = manager

  def perform(self):
    ''' Perform the query on the manager '''
    return self._manager.query(self)

  def __repr__(self):
    return '<%s %s>' % (self.__class__.__name__, super(ManagedQuery, self).__repr__())