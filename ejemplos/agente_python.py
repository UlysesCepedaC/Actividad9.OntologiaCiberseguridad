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

agente = AgenteCiberseguridad(g)

print("Controles:", agente.recomendar(ns.MalwareRamsomware))