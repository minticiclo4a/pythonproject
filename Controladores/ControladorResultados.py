from Repositorios.RepositorioResultados import RepositorioResultados
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Modelos.Resultados import Resultados
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
class ControladorResultados():
    def __init__(self):
        self.repositorioResultados = RepositorioResultados()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioCandidato = RepositorioCandidato()
    def index(self):
        print("Listado de Resultado")
        return self.repositorioResultados.findAll()
    def create(self,infoResultados):
        print("Creando nueva Resultado")
        nuevoResultados=Resultados(infoResultados)
        return self.repositorioResultados.save(nuevoResultados)
    def show(self,id):
        elResultados=Resultados(self.repositorioResultados.findById(id))
        return elResultados.__dict__
    def update(self,id,infoResultados):
        ResultadosActual=Resultados(self.repositorioResultados.findById(id))
        ResultadosActual.numeroMesa=infoResultados["mesa"]
        ResultadosActual.id_partido= infoResultados["partido"]
        return self.repositorioResultados.save(ResultadosActual)
    def delete(self,id):
        return self.repositorioResultados.delete(id)

    "Resultados de mesa y candidato a Resultados"

    def createResultado(self, infoResultado, id_candidato, id_mesa):
        nuevoResutado = Resultados(infoResultado)
        elCandidato = Candidato(self.repositorioCandidato.findById(id_candidato))
        laMesa = Mesa(self.repositorioMesa.findById(id_mesa))
        nuevoResutado.candidato = elCandidato
        nuevoResutado.mesa = laMesa
        return self.repositorioResultados.save(nuevoResutado)
    def showResultado(self,id):
        elResultado=Resultados(self.repositorioResultados.findById(id))
        return elResultado.__dict__