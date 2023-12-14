import json
import pickle
import dill

def ser(obj):
    try:
        json_obj = json.loads(json.dumps(obj))
        print(f"Object was successfully serialized by JSON, here's the result: {json_obj}")
        return json_obj
    except:
        print("JSON serialization failed.")

        try:
            pickle_obj = pickle.loads(pickle.dumps(obj))
            print(f"Object was successfully serialized by Pickle, here's the result: {pickle_obj}")
            return pickle_obj
        except:
            print("Pickle serialization failed.")

            try:
                dill_obj = dill.loads(dill.dumps(obj))
                print(f"Object was successfully serialized by Dill, here's the result: {dill_obj}")
                return dill_obj
            except:
                print("Dill serialization failed: Object can't be serialized.")
        
def deser(sered_obj):
    try:
        desered_obj = json.loads(json.dumps(sered_obj))
        print("Object successfully deserialized by JSON.")
        return desered_obj
    except:
        print("JSON deserialization failed.")

        try:
            desered_obj = pickle.loads(pickle.dumps(sered_obj))
            print("Object successfully deserialized by Pickle.")
            return desered_obj
        except:
            print("Pickle deserialization failed.")

            try:
                desered_obj = dill.loads(dill.dumps(sered_obj))
                print("Object successfully deserialized by Dill.")
                return desered_obj
            except:
                print("Dill deserialization failed: Object can't be deserialized.")



somedict = {
    "name": "John",
    "lastname": "Doe",
    "height": 175.5,
    "mass": 70.0
}

sered_dict = ser(somedict)
desered_dict = deser(sered_dict)

somelist = [1, 2, 3, 4, 5]

sered_list = ser(somelist)
desered_list = deser(sered_list)

somestring = "Hello, World!"

sered_string = ser(somestring)
desered_string = deser(sered_string)

someint = 42

sered_int = ser(someint)
desered_int = deser(sered_int)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person_obj = Person(name="Alice", age=30)

sered_obj = ser(person_obj)
desered_obj = deser(sered_obj)

some_lambda = lambda x: x * 2

sered_lambda = ser(some_lambda)
desered_lambda = deser(sered_lambda)