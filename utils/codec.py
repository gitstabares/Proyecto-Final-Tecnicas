import jsonpickle as jp

def json_serialize(obj, filename):
    with open(filename,'w') as file:
        file.write(jp.encode(obj, indent=4))
        file.close()

def json_deserialize(filename):
    with open(filename,'r') as file:
        output = jp.decode(file.read())
        file.close()
    return output