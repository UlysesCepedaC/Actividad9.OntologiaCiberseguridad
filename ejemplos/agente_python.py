from rdflib import Graph, Namespace
import ssl

url = "https://raw.githubusercontent.com/UlysesCepedaC/Actividad9.OntologiaCiberseguridad/main/Ontologia1.rdf"

g = Graph()
ssl._create_default_https_context = ssl._create_unverified_context
g.parse(url, format="xml")

ns = Namespace("http://www.semanticweb.org/ulyse/ontologies/2026/4/ciberseguridadUCC#")

class AgenteCiberseguridad:
    def __init__(self, grafo):
        self.grafo = grafo

    def recomendar(self, amenaza):
        consulta = f"""
        SELECT ?control WHERE {{
        ?control <{ns.mitiga}> <{amenaza}> .
        ?control a <{ns.Control}> .
        }}
        """
        return [str(r[0]).split("#")[-1] for r in self.grafo.query(consulta)]

    def activo_afectado(self, amenaza):
        consulta = f"""
        SELECT ?activo WHERE {{
        <{amenaza}> <{ns.afecta}> ?activo .
        }}
        """
        return [str(r[0]).split("#")[-1] for r in self.grafo.query(consulta)]

    def control_politica(self, politica):
        consulta = f"""
        SELECT ?control WHERE {{
        <{politica}> <{ns.requiere}> ?control .
        }}
        """
        return [str(r[0]).split("#")[-1] for r in self.grafo.query(consulta)]

agente = AgenteCiberseguridad(g)

print("Controles:", agente.recomendar(ns.MalwareRamsomware))
print("Activo afectado:", agente.activo_afectado(ns.MalwareRamsomware))
print("Control requerido:", agente.control_politica(ns.PoliticaSeguridadEmpresa))
