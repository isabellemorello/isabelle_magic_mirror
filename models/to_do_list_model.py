# import json
from microsoft_to_do_list.ricorda_di_task import ricorda_di_task
from microsoft_to_do_list.routine_task import routine_task


class ToDoList:
    def __init__(self, to_do_file):
        self.to_do_file = to_do_file
        self.title_list = self.get_title()

    def get_title(self):
        val = []
        title_list = []
        for key,value in self.to_do_file.items():
            if key == "value":
                val.append(value)
        value_list = val[0]
        for el in value_list:
            title_list.append(el["title"])
        # print(title_list)
        return title_list


td = ToDoList(routine_task)
# td = ToDoList("../microsoft_to_do_list/ricorda_di_task.py")
td.get_title()