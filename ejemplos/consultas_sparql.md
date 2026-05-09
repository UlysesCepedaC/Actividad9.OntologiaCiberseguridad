# Consulta SPARQL utilizada por el agente

```sparql
SELECT ?control WHERE {
?control <http://www.semanticweb.org/ulyse/ontologies/2026/4/ciberseguridadUCC#mitiga>
<http://www.semanticweb.org/ulyse/ontologies/2026/4/ciberseguridadUCC#MalwareRansomware> .

?control a
<http://www.semanticweb.org/ulyse/ontologies/2026/4/ciberseguridadUCC#Control> .
}
```

Esta consulta permite identificar los controles que mitigan una amenaza específica dentro de la ontología.
