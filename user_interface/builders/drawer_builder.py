from user_interface.drawers.display import Display
from user_interface.resource_managers.grid_image_mapper import GridImageMapper


class DrawerBuilder:
    @staticmethod
    def build_drawer() -> Display:
        grid_image_mapper = GridImageMapper()
        return Display(grid_image_mapper)
