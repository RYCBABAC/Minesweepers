from pipelines.ui_logic_accessor_builder import UILogicAccessorBuilder
from user_interface.builders.drawer_builder import DrawerBuilder
from user_interface.builders.event_manager_builder import EventManagerBuilder
from user_interface.builders.table_creator import TableCreator
from user_interface.runner.ui_runner import UIRunner


class UIBuilder:
    @staticmethod
    def build_ui(ui_logic_accessor_builder: UILogicAccessorBuilder) -> UIRunner:
        table = TableCreator.create_table()
        display = DrawerBuilder.build_drawer()
        ui_logic_accessor = ui_logic_accessor_builder.build_accessor(table)
        event_manager = EventManagerBuilder.build_event_manager(table, display, ui_logic_accessor)
        return UIRunner(table, display, event_manager)