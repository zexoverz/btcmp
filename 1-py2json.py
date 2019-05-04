import json
ariandy = {}
ariandy.update({'name':'Ariandy'})
ariandy.update({'address':'Pipit Raya Street, G5, 75119'})
ariandy.update({'hobbies':['Reading about Philosophy', 'Playing with a cat']})
ariandy.update({'is_married':False})

hs  = {'highSchool':'SMKN 7 Samarinda'}
uni = {'university':'STMIK Widya Cipta Dharma'}
ariandy.update({'school':[hs,uni]})

linux_cli = ['Debian-based', 'Arch-based']
compsci = ['Basic Computer Architecture & Organization']
programming = ['Python','Arduino']
other = ['RaspberryPi']

ariandy.update({'skills':[{'linux_cli':linux_cli},{'compsci':compsci},{'programming':programming},{'other':other}]})

def return2json():
	py2json = json.dumps(ariandy)
	print(py2json)

return2json()
