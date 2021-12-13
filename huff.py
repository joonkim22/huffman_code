# My first python program. In hindsight, could be made better using min-heap but the python heapq library isn't the most clear/intuitive.

data = [
	[0.20, 'x1'],
	[0.15, 'x2'],
	[0.13, 'x3'],
	[0.12, 'x4'],
	[0.10, 'x5'],
	[0.09, 'x6'],
	[0.08, 'x7'],
	[0.07, 'x8'],
	[0.06, 'x9']
]

while len(data) > 1: 
	data.sort()
	data.append([data[0][0]+data[1][0],'',data.pop(0),data.pop(0)])

def traverse(nodes, h_code):
	if not nodes[0][1]:
		traverse([nodes[0][2]],h_code + '0')
		traverse([nodes[0][3]],h_code + '1')
	else: print (nodes[0][1] + " is " + h_code)
traverse(data, '');
