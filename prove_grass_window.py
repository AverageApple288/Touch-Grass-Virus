import sys
import gi
import base64
import openai
from openai import OpenAI

gi.require_version('Gtk', '4.0')
gi.require_version('Adw', '1')
from gi.repository import Gtk, Adw, Gdk, Gio, GLib

css_provider = Gtk.CssProvider()
css_provider.load_from_path('style.css')
Gtk.StyleContext.add_provider_for_display(Gdk.Display.get_default(), css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

class ProveGrassWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Things will go here
        self.set_default_size(500, 500)
        self.set_title("Touch Grass Virus")

        # Text
        self.label = Gtk.Label(label="Before you can use this app you must prove that you have touched grass first.")
        self.label2 = Gtk.Label(label="Please upload an image of you touching grass for verification.")
        self.label.set_css_classes(['title'])

        # Button
        self.button = Gtk.Button(label="Select a File")
        self.button.connect("clicked", self.show_open_dialog)

        self.open_dialog = Gtk.FileDialog.new()
        self.open_dialog.set_title("Select a File")

        f = Gtk.FileFilter()
        f.set_name("Image files")
        f.add_mime_type("image/jpeg")
        f.add_mime_type("image/png")

        filters = Gio.ListStore.new(Gtk.FileFilter)  # Create a ListStore with the type Gtk.FileFilter
        filters.append(f)  # Add the file filter to the ListStore. You could add more.

        self.open_dialog.set_filters(filters)  # Set the filters for the open dialog
        self.open_dialog.set_default_filter(f)

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
        self.label_box.append(self.label2)
        self.label_box.append(self.spacer1)
        self.label_box.append(self.button)
        self.label_box.append(self.spacer2)

    def show_open_dialog(self, button):
        self.open_dialog.open(self, None, self.open_dialog_open_callback)

    def open_dialog_open_callback(self, dialog, result):
        try:
            file = dialog.open_finish(result)
            if file is not None:
                file_path = f"File path is {file.get_path()}"
                # Handle loading file from here
                client = OpenAI(
                )

                prompt = "Is this an image of someone touching grass? Please only answer with 'yes' or 'no'."
                with open(file_path, "rb") as image_file:
                    b64_image = base64.b64encode(image_file.read()).decode("utf-8")

                response = client.responses.create(
                    model="gpt-4o-mini",
                    input=[
                        {
                            "role": "user",
                            "content": [
                                {"type": "input_text", "text": prompt},
                                {"type": "input_image", "image_url": f"data:image/png;base64,{b64_image}"},
                            ],
                        }
                    ],
                )

                print(response)
        except GLib.Error as error:
            print(f"Error opening file: {error.message}")



    def close_window(self, window):
        self.destroy()

class ProveGrass(Adw.Application):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.connect('activate', self.on_activate)

    def on_activate(self, app):
        self.win = ProveGrassWindow(application=app)
        self.win.present()

def prove_grass_run():
    prove_grass= ProveGrass(application_id="com.touch-grass.Intro")
    prove_grass.run(sys.argv)

prove_grass_run()