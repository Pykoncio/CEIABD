(deffacts alumnos
    (alumno "Juan" 8)
    (alumno "María" 10)
    (alumno "Pedro" 4)
)

(defrule aprobar
    (alumno ?nombre ?nota &:(>= ?nota 5))
    =>
    (printout t ?nombre " ha aprobado con un " ?nota "." crlf)
)