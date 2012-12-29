from cement.core import controller, foundation
from dop.client import Client
from prettytable import PrettyTable

class Droplets(controller.CementBaseController):
    class Meta:
        label = 'droplets'
        interface = controller.IController
        stacked_on = None
        description = "Droplets controller"

    def __init__(self):
        # todo: fix
        app = foundation.CementApp('docli')
        self.do = Client(app.config.get('digitalocean','client_key'), app.config.get('digitalocean','api_key'))


    @controller.expose(help="Returns a list of droplets")
    def default(self):
        droplets = do.show_active_droplets()

        table = PrettyTable(['Status', 'Name', 'Size', 'Region', 'Image', 'Backups'])

        regions = do.regions()
        images  = do.images()
        sizes = do.sizes()

        for droplet in droplets:
            new_size = None
            new_image = None
            new_region = None

            for size in sizes:
                if size.id == droplet.size_id:
                    new_size = size
                    print size.name
                    break

            for image in images:
                if image.id == droplet.image_id:
                    new_image = image
                    print image.name
                    break

            for region in regions:
                if region.id == droplet.region_id:
                    new_region = region
                    print region.name
                    break

            table.add_row([droplet.status, droplet.name, droplet.size_id, new_region.name, new_image.name, droplet.backups_active])

        print table

    @controller.expose(help="Returns information about a specific droplet")
    def show(self):
        print self.pargs
        #droplet = do.show_droplet(id)
        #return True

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