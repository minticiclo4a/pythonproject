from Repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Mesa import Mesa

class ControladorMesa():
    def __init__(self):
        self.repositorioMesa = RepositorioMesa()
    def index(self):
        print("llego")
        return self.repositorioMesa.findAll()
    def create(self,infoMesa):
        nuevoMesa=Mesa(infoMesa)
        return self.repositorioMesa.save(nuevoMesa)
    def show(self,mesa):
        elMesa=Mesa(self.repositorioMesa.findById(mesa))
        return elMesa.__dict__
    def update(self,id,infoMesa):
        def update(self, id, infoMesa):
            print("actualizando---")
            MesaActual = Mesa(self.repositorioMesa.findById(id))
            MesaActual.numero = infoMesa["numero"]
            MesaActual.cantidadInscritos = infoMesa["cantidad"]
            return self.repositorioMesa.save(MesaActual)
    def delete(self,id):
        return self.repositorioMesa.delete(id)