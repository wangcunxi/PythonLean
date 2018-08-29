
import ctypes

class Array:
	def __init__(self,size):
		assert size > 0, "Array size must be > 0"
		self._size = size
		PyArrayType = ctypes.py_object * size
		self._elements = PyArrayType()
		self.clear(None)
	
	def len(self):
		return self._size

	def getitem(self,index):
		assert index >= 0 and index < self._size, "Array subscrpt out of range"
		return self._elements[index]

	def setitem(self,index,value):
		assert index >=0 and index < self._size, "Array subscript out of range"
		self._elements[index] = value

	def clear(self, value):
		for i in range(self._size):
			self._elements[i] = value

		

class Array2D:
	def __init__(self,numRows,numCols):
		self._theRows = Array(numRows)

		for i in range(numRows):
			self._theRows[i] = Array(numCols)

	def numRows(self):
		return self._theRows._size

	def numCols(self):
		return self._theRows[0]._size

	def clear(self,value):
		for row in range(self.numRows):
			row.clear(value)

	def getitem(self, ndxTuple):
		assert len(ndxTuple) == 2, "Invalid number of array subscripts"
		row = ndxTuple[0]
		col = ndxTuple[1]

		assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), "Array subscript out of range"

		rowArray = self._theRows[row]
		return rowArray[col]

	def setitem(self,ndxTuple,value):
		assert len(ndxTuple) == 2, "Invalid number of array subscripts"
		row = ndxTuple[0]
		col = ndxTuple[1]
		assert row >= 0 and row < self.numRows() and col >= 0 and col < self.numCols(), "Array subscript out of range"
		rowArray = self._theRows[row]
		rowArray[col] = value

