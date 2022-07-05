from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Triggers long running task"

    def add_arguments(self, parser):
        parser.add_argument("error", nargs="+", type=bool)
        # parser.add_argument('poll_ids', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        if options["error"]:
            raise CommandError("This command just raised an error.")

        print("This task runs really really long")
