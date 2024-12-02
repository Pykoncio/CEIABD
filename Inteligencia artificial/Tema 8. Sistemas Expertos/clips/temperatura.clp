(defrule encender-calefaccion
    (temperatura ?t&:(<= ?t 20)) ;; La temperatura es menor o igual a 20
    =>
    (printout t "La temperatura es " ?t ". Encendiendo la calefacción." crlf)
    (assert (calefaccion-encendida))
)