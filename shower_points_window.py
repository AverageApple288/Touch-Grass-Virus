import sys
import gi

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gdk

css_provider = Gtk.CssProvider()
css_provider.load_from_path('style.css')
Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

class ShowerPointsWindow(Gtk.ApplicationWindow):
    def __init__(self, shower_points, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Things will go here
        self.set_default_size(500, 500)
        self.set_title("Touch Grass Virus")
        self.shower_points = shower_points

        # Text
        self.label = Gtk.Label(label=f"You have {shower_points} shower points")
        self.label.set_css_classes(['title'])

        # Button
        self.button = Gtk.Button(label="Touch Grass")
        self.button.connect("clicked", self.close_window)

        # Main box
        self.main_box = Gtk.Box(spacing=10, orientation=Gtk.Orientation.HORIZONTAL)

        # Label box
        self.label_box = Gtk.Box(spacing=10, orientation=Gtk.Orientation.VERTICAL)

        # Spacers
        self.spacer1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        self.spacer2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)

        # Add button and label
        self.set_child(self.main_box)
        self.main_box.set_css_classes(['background'])
        self.main_box.append(self.label_box)
        self.label_box.append(self.label)
        self.label_box.append(self.spacer1)
        self.label_box.append(self.button)
        self.label_box.append(self.spacer2)

    def close_window(self, window):
        self.destroy()

class ShowerPoints(Adw.Application):
    def __init__(self, shower_points, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)
        self.shower_points = shower_points

    def on_activate(self, app):
        self.win = ShowerPointsWindow(self.shower_points, application=app)
        self.win.present()

def shower_points_run(shower_points):
    shower_points_app = ShowerPoints(shower_points, application_id="com.touch-grass.ShowerPoints")
    shower_points_app.run(sys.argv)
    return shower_points_app

def shower_points_destroy(shower_points_app):
    shower_points_app.close()