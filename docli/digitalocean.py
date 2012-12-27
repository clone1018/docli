
from cement.core import controller
import dop.client

class Droplets(controller.CementBaseController):
    class Meta:
        label = 'droplets'
        interface = controller.IController
        stacked_on = None
        description = "Droplets controller"

    @controller.expose(help="Returns a list of droplets")
    def default(self):
        dop.Client.show_active_droplets()

    def show(self):
        return True

    def new(self):
        return True

    def reboot(self):
        return True

    def power_cycle(self):
        return True

    def shutdown(self):
        return True

    def power_on(self):
        return True

    def reset_root_password(self):
        return True

    def resize(self):
        return True

    def restore(self):
        return True

    def rebuild(self):
        return True

    """
    Move enable_backups and disable_backups to backups(enable/disable)
    """
    def enable_backups(self):
        return True

    def disable_backups(self):
        return True