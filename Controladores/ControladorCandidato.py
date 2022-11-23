from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Candidato import Candidato
from Modelos.Partido import Partido

class ControladorCandidato():
    def __init__(self):
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioPartido = RepositorioPartido()
    def index(self):
        print("llego")
        return self.repositorioCandidato.findAll()
    def create(self,infoCandidato):
        nuevoCandidato=Candidato(infoCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)
    def show(self,Candidato):
        elCandidato=Candidato(self.repositorioCandidato.findById(Candidato))
        return elCandidato.__dict__
    def update(self,id,infoCandidato):
        def update(self, id, infoCandidato):
            print("actualizando---")
            CandidatoActual = Candidato(self.repositorioCandidato.findById(id))
            CandidatoActual.cedula = infoCandidato["cedula"]
            CandidatoActual.numero_resolucion = infoCandidato["numero_resolucion"]
            CandidatoActual.nombre = infoCandidato["nombre"]
            CandidatoActual.apellido = infoCandidato["apellido"]
            return self.repositorioCandidato.save(CandidatoActual)
    def delete(self,id):
        return self.repositorioCandidato.delete(id)
    "relacion candidato Partido"

    def asignarPartido(self, id, id_partido):
        candidatoActual = Candidato(self.repositorioCandidato.findById(id))
        partidoActual =Partido(self.repositorioPartido.findById(id_partido))
        candidatoActual.partido = partidoActual
        return self.repositorioCandidato.save(candidatoActual)
