

def le(a):
	try:
		t=open(a).read()
	except IOError:
		print 'Ops'
