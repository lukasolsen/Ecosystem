import pyglet
from pyglet import shapes, text
from manager.Ecosystem import Ecosystem
from manager.Entities.Elf import Elf
from manager.Food import Food


class Game:
    def __init__(self):
        self.window = pyglet.window.Window(800, 600, "Ecosystem Simulation")

        self.coordinates_label = text.Label(
            "Coordinates: (0, 0)",
            font_name='Arial',
            font_size=12,
            x=10, y=self.window.height - 20,
        )

        self.entitiesAmount_label = text.Label(
            "Entities: 0",
            font_name='Arial',
            font_size=12,
            x=10, y=self.window.height - 40,
        )

        self.entitiesList = text.Label(
            "Entities List: ",
            font_name='Arial',
            font_size=12,
            x=10, y=self.window.height - 60,
        )

        self.mouseHover = text.Label(
            "Mouse Hovering: ",
            font_name='Arial',
            font_size=12,
            x=10, y=self.window.height - 80,
        )  # What the mouse is hovering over such as "Grass, Tree, Entity 1: info, etc."

        self.coordinates = (0, 0)
        self.ecosystem = Ecosystem(5)
        self.dragging = False
        self.last_x, self.last_y = 0, 0
        self.offset_x, self.offset_y = 0, 0
        self.window_show_extra = False

        self.camera_rotation = 0.0
        self.camera_rotation_speed = 0.01  # Adjust the rotation speed as needed

        # Schedule the update function to be called regularly
        pyglet.clock.schedule_interval(self.update, 1/60.0)

        # Assign the on_draw method to the window's on_draw event
        self.window.on_draw = self.on_draw
        # Assign the on_mouse_drag method to the window's on_mouse_drag event
        self.window.on_mouse_drag = self.on_mouse_drag
        self.window.on_key_press = self.on_key_press
        self.window.on_mouse_release = self.on_mouse_release
        self.window.on_mouse_motion = self.on_mouse_motion

        pyglet.app.run()

    def update(self, dt):
        self.ecosystem.update(dt)

    def draw(self):
        self.ecosystem.draw(self.offset_x, self.offset_y)

    def on_draw(self):
        self.window.clear()
        self.draw()

        # Draw coordinates
        if self.window_show_extra:
            self.coordinates_label.text = f"Coordinates: ({int(-self.offset_x)}, {int(-self.offset_y)})"
            self.coordinates_label.draw()

            self.entitiesAmount_label.text = f"Entities: {len(self.ecosystem.entities)}"
            self.entitiesAmount_label.draw()

            self.entitiesList.text = "Entities List: \n"
            for i, entity in enumerate(self.ecosystem.entities):
                self.entitiesList.text += f"\nEntity {i}: ({int(entity.x)}, {int(entity.y)}) - {entity.state}\n"
            self.entitiesList.draw()

            self.mouseHover.draw()

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.dragging:
            if buttons & pyglet.window.mouse.LEFT:
                # If left mouse button is pressed, move the camera
                if modifiers & pyglet.window.key.MOD_SHIFT:
                    # If shift is pressed, rotate the camera
                    self.camera_rotation -= dx * self.camera_rotation_speed
                else:
                    # Otherwise, move the camera
                    self.offset_x -= dx
                    self.offset_y -= dy
            else:
                # Move the camera in a way that our coordinates are the same,
                # but our view angle is changed such as we can see from the side, above, or below.
                self.camera_rotation += dx * self.camera_rotation_speed

        else:
            self.dragging = True

        self.last_x, self.last_y = x, y

    def on_mouse_motion(self, x, y, dx, dy):
        # Update coordinates label

        if self.window_show_extra:
            # Check if the mouse is hovering over any entity
            hovered_entity = None
            for entity in self.ecosystem.entities:
                distance = ((x - self.offset_x - entity.x) ** 2 +
                            (y - self.offset_y - entity.y) ** 2) ** 0.5
                if distance < 10:  # Adjust the value based on the size of your entities
                    hovered_entity = entity
                    break

            # Display information about the hovered entity
            if hovered_entity:
                self.mouseHover.text = f"Mouse Hovering: {self.get_entity_info(hovered_entity)}"
                print(
                    f"Mouse Hovering: {self.get_entity_info(hovered_entity)}")
            else:
                self.mouseHover.text = "Mouse Hovering: Nothing"
                print("Mouse Hovering: Nothing")
            self.mouseHover.draw()

    def get_entity_info(self, entity):
        if isinstance(entity, Elf):
            return f"Elf - Race: {entity.race}, Gender: {entity.gender}, State: {entity.state}"
        elif isinstance(entity, Food):
            return "Food"
        else:
            return "Unknown Entity"

    def on_key_press(self, symbol, modifiers):
        print("Symbol = ", symbol, " Pyglet key =",
              pyglet.window.key.symbol_string(symbol))
        if symbol == pyglet.window.key.F11:
            self.window.set_fullscreen(not self.window.fullscreen)
        elif symbol == pyglet.window.key.F4:
            self.window_show_extra = not self.window_show_extra
        elif symbol == pyglet.window.key.SPACE:
            self.offset_x, self.offset_y = 0, 0
        elif symbol == pyglet.window.key.ESCAPE:
            pyglet.app.exit()

    def on_mouse_release(self, x, y, button, modifiers):
        self.dragging = False


game = Game()
