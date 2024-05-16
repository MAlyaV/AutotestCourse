from controls import *


@templatename('Staff/selectionNew:Stack')
class StaffSelector(CatalogTemplateList):
    """Выбор сотрудника"""

    list_grid = ControlsListView(SabyBy.DATA_QA, 'controls-Render__field')

