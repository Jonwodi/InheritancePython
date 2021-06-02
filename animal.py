class Animal:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def speak(self):
    return f"My anme is {self.name}"

class Husky(Animal):
  def __init__(self, name, age):
    super().__init__(name, age)

  def speak(self):
      return "whoof whoof"

class Pitbull(Animal):
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def speak(self):
    return f"My anme is {self.name}"


class Cat(Animal):
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def speak(self):
    return f"My anme is {self.name}"