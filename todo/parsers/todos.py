from todo.parsers.base import BaseParser, set_value


class TodosParser(BaseParser):
    def _interpret(self, parsed_args):
        if parsed_args.add_todo:
            return {"add_todo": {"name": parsed_args.add_todo, "group_name": parsed_args.group}}
        elif parsed_args.interactive:
            return {"interactive": {"state": parsed_args.state, "group_name": parsed_args.group}}
        else:
            return {"list_todos": {"state": parsed_args.state, "group_name": parsed_args.group}}

    def _add_arguments(self):
        self.parser.add_argument('--interactive', '-i', action='store_true')

        parser_group = self.parser.add_mutually_exclusive_group()
        parser_group.add_argument(
            '--completed',
            '-c',
            dest='list_todos',
            nargs=0,
            action=set_value(STATES.COMPLETED),
        )
        parser_group.add_argument(
            '--uncompleted',
            '-u',
            dest='list_todos',
            nargs=0,
            action=set_value(STATES.UNCOMPLETED),
        )
        parser_group.add_argument('--add', '-a', dest='add_todo', action='store')
