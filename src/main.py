def greet(name):
    return f"Hello, {name}!"

def agecheck(age):
    if age < 18:
        return "You are underage."
    elif age == 18:
        return "You just became an adult."
    else:
        return "You are an adult."

if __name__ == '__main__':   
    print("test")
    print(greet("Alice"))
    agecheck(18)
    
