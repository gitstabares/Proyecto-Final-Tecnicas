import jsonpickle as jp

def serialize(obj, filename):
    with open('data/' + filename,'w') as file:
        file.write(jp.encode(obj, indent=4))
        file.close()

def deserialize(filename):
    try:
        with open('data/' + filename,'r') as file:
            output = jp.decode(file.read())
            file.close()
        return output
    except:
        return []