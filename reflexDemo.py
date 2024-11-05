import reflex as rx 

class State(rx.State):
    name: str = "Alex"
    id: int = 1

    def showName(self):
        return self.name
    
def index():
    return rx.text("Root Page")

def name():
    return rx.text(State.showName)
   
app = rx.App()
app.add_page(index)
app.add_page(name)