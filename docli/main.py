__author__ = 'clone1018'

from cement.core import foundation, controller, handler
from docli import digitalocean

# define application controllers
class DOcliBaseController(controller.CementBaseController):
    class Meta:
        label = 'base'
        interface = controller.IController
        description = "My Application Does Amazing Things"
        arguments = [
            (['--base-opt'], dict(help="option under base controller")),
            ]

def run():
    try:
        # create the application
        app = foundation.CementApp('docli',config_files=['~/.docli.conf'], base_controller=DOcliBaseController)

        # register non-base controllers
        handler.register(digitalocean.Droplets)

        # setup the application
        app.setup()

        if not app.config.has_section('digitalocean'):
            app.config.add_section('digitalocean')

            if not app.config.has_key('digitalocean', 'client_id'):
                app.config.set('digitalocean','client_id', True)

                print 'Please set your api key and client id in ~/.docli.conf'
                app.close()
                exit()

        app.run()
    finally:
        app.close()