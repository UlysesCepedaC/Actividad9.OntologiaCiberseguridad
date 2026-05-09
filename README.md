# Actividad9.OntologiaCiberseguridad

## Descripción
Ontología desarrollada en Protégé para representar amenazas, activos, controles y vulnerabilidades.

## Namespace
http://www.TuNombre.org/ciberseguridad#

## Clases principales
- Amenaza
- Activo
- Control
- Vulnerabilidad

## Relaciones
- afecta
- mitiga
- protegidoPor

## Ejemplo SPARQL
SELECT ?control WHERE {
<http://www.TuNombre.org/ciberseguridad#Phishing>
<http://www.TuNombre.org/ciberseguridad#mitiga> ?control .
}
