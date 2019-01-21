
def InitGlobalDef():
	global g_global_dict
	g_global_dict = {}
	pass

def SetValue( name, value ):
	g_global_dict[name] = value
	pass

def GetValue( name, default_value = None ):
	try:
		return g_global_dict[name]
	except Exception as e:
		return default_value
	pass

def GetGlobalDefLen():
	return len( g_global_dict )
	pass