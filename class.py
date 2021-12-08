
class dog:

    def eat(**kwargs):
        return "Eating "+kwargs['name']

    def bark():
        print("Barking...")

    def running():
        print("Running...")
    
    def sleep():
        print("Sleeping...")

class cat:

    def eat(**kwargs):
        return "Eating "+kwargs['name']

    def bark():
        print("Barking...")

    def running():
        print("Running...")
    
    def sleep():
        print("Sleeping...")

if __name__ == "__main__":

    dg = dog
    action = dg.eat(name="Saver")
    print (action)

    ct = cat
    action = ct.eat(name="Tom")
    print (action)