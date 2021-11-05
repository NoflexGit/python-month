class AbstractUser:
    def __init__(self, email, name) -> None:
        self.email = email

    def sign_in(self):
        print('logged_in')


class Admin(AbstractUser):
    is_admin = True

    def __init__(self, email, name, admin_lvl) -> None:
        super().__init__(email, name)
        self.admin_lvl = admin_lvl

    def ban_user(self):
        print('I ban an user')


class Writer(AbstractUser):
    is_writer = True

    def __init__(self, email, name, genre) -> None:
        super().__init__(email, name)
        self.genre = genre

    def write_article(self):
        print('I write an article')


class Manager(AbstractUser):
    is_manager = True

    def __init__(self, email, name, branch) -> None:
        super().__init__(email, name)
        self.branch = branch

    def create_project(self):
        print('I create a new project')


admin_1 = Admin('john@mail.com', 'John', 2)
manager_1 = Manager('emily@mail.com', 'Emily', 'IT')
writer_1 = Writer('kate@mail.com', 'Kate', 'Novels')

manager_1.sign_in()
writer_1.sign_in()
admin_1.sign_in()

admin_1.ban_user()
print(admin_1.admin_lvl)
