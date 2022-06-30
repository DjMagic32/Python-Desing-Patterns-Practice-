class USPlugConnectorInterface:
    def give_electricity(self):
        pass

class USPlugConnector(USPlugConnectorInterface):
    def give_electricity(self):
        print("Esto es un plug estado unidense")

class USElectricalSocket:
    def plug_in(self, us_plug):
        us_plug.give_electricity()

class UKPlugConnectorInterface:
    def provide_electricity(self):
        pass

class UKElectricalSocket(UKPlugConnectorInterface):
    def plug_in(self, uk_plug):
        print ("Esto es un plug de Europa")
        uk_plug.provide_electricity()

class UStoUKPlugAdapter(UKPlugConnectorInterface):
    def __init__(self, us_plug):
        self.us_plug = us_plug

    def provide_electricity(self):
        self.us_plug.give_electricity()

def main():
    us_plug = USPlugConnector()
    uk_electrical_socket = UKElectricalSocket()
    uk_adapter = UStoUKPlugAdapter(us_plug)
    uk_electrical_socket.plug_in(uk_adapter)

if __name__ == "__main__":
    main()



