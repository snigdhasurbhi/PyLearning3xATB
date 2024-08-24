class MyClass:
    def __init__(self):
        self.value = "value"
        self.name = "amit"
    def public_function(self):
        print("This is a public function.")

    def _protected_function(self):
        print("This is a protected function.")

    def __private_function(self):
        print("This is a private function.")

    def public_fn_private(self):
        print("private function")
        self.__private_function()

Map=MyClass()
Map.public_function()
Map.public_fn_private()
