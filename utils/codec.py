import jsonpickle as jp

def serialize(obj, filename):
    '''
    Serialize an object in the JSON format and dumps the content the given file
    Args:
        obj(object): Object to be serialized
        filename(str): File's path. Relative to data's folder
    '''
    with open('data/' + filename,'w') as file:
        file.write(jp.encode(obj, indent=4))
        file.close()

def deserialize(filename):
    '''
    Deserialize the given JSON file and unpack its content in a variable
    Args:
        filename(str): File's path. Relative to data's folder
    Returns:
        object: Instance of the object dumped in the JSON file
    '''
    try:
        with open('data/' + filename,'r') as file:
            output = jp.decode(file.read())
            file.close()
        return output
    except:
        return []