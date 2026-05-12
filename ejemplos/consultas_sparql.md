# Consultas SPARQL

Este archivo contiene ejemplos de consultas SPARQL utilizadas en el agente desarrollado en Python para interactuar con la ontología de ciberseguridad.

## 1. Buscar controles que mitiguen una amenaza

```sparql
SELECT ?control WHERE {
?control <http://www.semanticweb.org/ulyse/ontologies/2026/4/ciberseguridadUCC#mitiga>
<http://www.semanticweb.org/ulyse/ontologies/2026/4/ciberseguridadUCC#MalwareRamsomware> .
?control a <http://www.semanticweb.org/ulyse/ontologies/2026/4/ciberseguridadUCC#Control> .
}
```

Esta consulta permite identificar los controles que mitigan la amenaza MalwareRamsomware.

---

## 2. Buscar activo afectado por una amenaza

```sparql
SELECT ?activo WHERE {
<http://www.semanticweb.org/ulyse/ontologies/2026/4/ciberseguridadUCC#MalwareRamsomware>
<http://www.semanticweb.org/ulyse/ontologies/2026/4/ciberseguridadUCC#afecta> ?activo .
}
```

Esta consulta permite identificar el activo afectado por la amenaza seleccionada.

---

## 3. Buscar controles requeridos por una política

```sparql
SELECT ?control WHERE {
<http://www.semanticweb.org/ulyse/ontologies/2026/4/ciberseguridadUCC#PoliticaSeguridadEmpresa>
<http://www.semanticweb.org/ulyse/ontologies/2026/4/ciberseguridadUCC#requiere> ?control .
}
```

Esta consulta permite identificar qué controles son requeridos por una política de seguridad.
