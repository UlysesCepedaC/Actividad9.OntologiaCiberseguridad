````md
# Consultas SPARQL

## Consultar todas las amenazas

```sparql
SELECT ?amenaza WHERE {
?amenaza a <http://www.semanticweb.org/ulyse/ontologies/2026/4/ciberseguridadUCC#Amenaza> .
}
