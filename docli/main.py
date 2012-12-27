__author__ = 'clone1018'

from cement.core import foundation, controller, handler
import digitalocean

# define application controllers
class DOcliBaseController(controller.CementBaseController):
    class Meta:
        label = 'base'
        interface = controller.IController
        description = "My Application Does Amazing Things"
        arguments = [
            (['--base-opt'], dict(help="option under base controller")),
            ]

    @controller.expose(help="base controller default command", hide=True)
    def default(self):
        print "Inside MyAppBaseController.default()"

    @controller.expose(help="another base controller command")
    def command1(self):
        print "Inside MyAppBaseController.command1()"

try:
    # create the application
    app = foundation.CementApp('docli', base_controller=MyAppBaseController)

    # register non-base controllers
    handler.register(digitalocean.Droplets)

    # setup the application
    app.setup()

    app.run()
finally:
    app.close()