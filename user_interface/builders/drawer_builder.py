from user_interface.drawers.display import Display


class DrawerBuilder:
    @staticmethod
    def build_drawer() -> Display:
        return Display()
