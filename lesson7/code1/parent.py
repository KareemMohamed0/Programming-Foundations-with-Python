class Parent():
    def __init__(self, last_name, eye_color):
        print("parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("p-last name " + self.last_name)
        print("p-eye color " + self.eye_color)


class Child(Parent):
    def __init__(self, last_name, eye_color, num_of_toys):
        print("child constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.num_of_toys = num_of_toys

    def show_info(self):
        print("c-last name " + self.last_name)
        print("c-eye color " + self.eye_color)
        print("c-number of toys " + str(self.num_of_toys))


crys = Parent('crys', 'blue')
ahmed = Child('crys', 'blue', 20)
print(ahmed.show_info())
print(crys.show_info())
