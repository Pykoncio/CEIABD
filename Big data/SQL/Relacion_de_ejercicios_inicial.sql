DROP DATABASE IF EXISTS INVESTIGADORES;
CREATE DATABASE INVESTIGADORES;
USE INVESTIGADORES;

DROP TABLE IF EXISTS INVESTIGADORES, RESERVA, EQUIPOS, FACULTAD;

CREATE TABLE FACULTAD (
    Codigo INT PRIMARY KEY,
    Nombre NVARCHAR(100) NOT NULL
);

CREATE TABLE INVESTIGADORES (
    DNI VARCHAR(8) PRIMARY KEY,
    NomApels NVARCHAR(255) NOT NULL,
    Facultad INT,
    FOREIGN KEY (Facultad) REFERENCES FACULTAD(Codigo)
);

CREATE TABLE EQUIPOS (
    NumSerie CHAR(4) PRIMARY KEY,
    Nombre NVARCHAR(100) NOT NULL,
    Facultad INT,
    FOREIGN KEY (Facultad) REFERENCES FACULTAD(Codigo)
);

CREATE TABLE RESERVA (
    DNI VARCHAR(8),
    NumSerie CHAR(4),
    Comienzo DATETIME NOT NULL,
    Fin DATETIME NOT NULL,
    PRIMARY KEY (DNI, NumSerie),
    FOREIGN KEY (DNI) REFERENCES INVESTIGADORES(DNI),
    FOREIGN KEY (NumSerie) REFERENCES EQUIPOS(NumSerie)
);

INSERT INTO FACULTAD (Codigo, Nombre)
VALUES 
(1, 'Facultad A'),
(2, 'Facultad B'),
(3, 'Facultad C'),
(4, 'Facultad D'),
(5, 'Facultad E'),
(6, 'Facultad F'),
(7, 'Facultad G'),
(8, 'Facultad H'),
(9, 'Facultad I'),
(10, 'Facultad J');

INSERT INTO INVESTIGADORES (DNI, NomApels, Facultad)
VALUES 
('12345678', 'Investigador A', 1),
('12345679', 'Investigador B', 1),
('12345680', 'Investigador C', 2),
('12345681', 'Investigador D', 2),
('12345682', 'Investigador E', 3),
('12345683', 'Investigador F', 3),
('12345684', 'Investigador G', 4),
('12345685', 'Investigador H', 4),
('12345686', 'Investigador I', 5),
('98765432', 'Investigador X', 8),
('97546123', 'Investigador Y', 9),
('97556123', 'Investigador Z', 1),
('12345687', 'Investigador J', 5);

INSERT INTO EQUIPOS (NumSerie, Nombre, Facultad)
VALUES 
('A001', 'Equipo A', 1),
('A002', 'Equipo B', 1),
('A003', 'Equipo C', 2),
('A004', 'Equipo D', 2),
('A005', 'Equipo E', 3),
('A006', 'Equipo F', 3),
('A007', 'Equipo G', 4),
('A008', 'Equipo H', 4),
('A009', 'Equipo I', 5),
('A010', 'Equipo J', 5),
('A011', 'Equipo H', 7);
INSERT INTO RESERVA (DNI, NumSerie, Comienzo, Fin)
VALUES 
('12345678', 'A001', '2023-10-01 10:00:00', '2023-10-01 12:00:00'),
('12345679', 'A002', '2023-10-01 10:00:00', '2023-10-01 12:00:00'),
('12345680', 'A003', '2023-10-01 10:00:00', '2023-10-01 12:00:00'),
('12345681', 'A004', '2023-10-01 10:00:00', '2023-10-01 12:00:00'),
('12345682', 'A005', '2023-10-01 10:00:00', '2023-10-01 12:00:00'),
('12345683', 'A006', '2023-10-01 10:00:00', '2023-10-01 12:00:00'),
('12345684', 'A007', '2023-10-01 10:00:00', '2023-10-01 13:00:00'),
('12345685', 'A008', '2023-10-01 10:00:00', '2023-10-01 12:00:00'),
('12345686', 'A009', '2023-10-01 10:00:00', '2023-10-01 12:00:00'),
('12345678', 'A010', '2023-10-02 10:00:00', '2023-10-01 12:00:00'),
('12345687', 'A010', '2023-10-01 10:00:00', '2023-10-01 12:00:00');

SELECT I.DNI, I.NomApels
FROM INVESTIGADORES I
JOIN RESERVA R ON I.DNI = R.DNI
GROUP BY I.DNI
HAVING COUNT(R.NumSerie) > 1;

SELECT I.DNI, I.NomApels, F.Nombre AS Nombre_Facultad, E.NumSerie, 
E.Nombre AS Nombre_Equipo, F.Nombre AS Nombre_Facultad, R.Comienzo, R.Fin
FROM INVESTIGADORES I JOIN RESERVA R ON I.DNI = R.DNI
JOIN EQUIPOS E ON R.NumSerie = E.NumSerie
JOIN FACULTAD F ON E.Facultad = F.Codigo
ORDER BY R.NumSerie;

SELECT I.DNI, I.NomApels 
FROM INVESTIGADORES I JOIN RESERVA R ON I.DNI = R.DNI 
JOIN EQUIPOS E ON R.NumSerie = E.NumSerie
JOIN FACULTAD F ON E.Facultad = F.Codigo
WHERE I.FACULTAD != E.FACULTAD; 

Select F.Nombre 
FROM FACULTAD F
JOIN INVESTIGADORES I ON F.Codigo = I.Facultad
WHERE F.CODIGO NOT IN (
	SELECT I.Facultad 
    FROM INVESTIGADORES I
    JOIN RESERVA R ON I.DNI = R.DNI
);

SELECT F.Nombre 
FROM FACULTAD F JOIN INVESTIGADORES I ON F.Codigo = I.Facultad
LEFT JOIN RESERVA R ON I.DNI = R.DNI -- Left toma en cuenta investigadores que pueden no tener reservas
WHERE I.DNI NOT IN (SELECT DNI FROM RESERVA);

SELECT E.NumSerie, E.Nombre 
FROM EQUIPOS E
LEFT JOIN RESERVA R ON E.NumSerie = R.NumSerie
WHERE R.NumSerie IS NULL;

SELECT I.NomApels 
FROM INVESTIGADORES I
JOIN FACULTAD F ON I.Facultad = F.Codigo
WHERE F.Nombre = "Facultad A";

SELECT F.Nombre, COUNT(E.NumSerie) AS NumEquipos -- COUNT(*) Tambien toma en cuenta valores null
FROM EQUIPOS E RIGHT JOIN FACULTAD F 
ON E.Facultad = F.Codigo
GROUP BY F.Codigo
ORDER BY NumEquipos DESC;

SELECT I.DNI, I.NomApels, I.Facultad 
FROM INVESTIGADORES I LEFT JOIN RESERVA R
ON I.DNI = R.DNI 
WHERE R.DNI IS NULL;

SELECT DISTINCT I.NomApels FROM INVESTIGADORES I 
JOIN RESERVA R ON I.DNI = R.DNI 
JOIN EQUIPOS E ON R.NumSerie = E.NumSerie
WHERE E.Nombre = "Equipo A";

SELECT I.DNI, I.NomApels, COUNT(R.DNI) AS NumReservas 
FROM INVESTIGADORES I
LEFT JOIN RESERVA R ON I.DNI = R.DNI 
GROUP BY I.DNI
ORDER BY NumReservas DESC;

SELECT I.DNI, I.NomApels, SUM(TIMESTAMPDIFF(MINUTE, R.Comienzo, R.Fin)) AS tiempoTotal
FROM INVESTIGADORES I 
JOIN RESERVA R ON I.DNI = R.DNI
GROUP BY I.DNI 	-- Para acumular el tiempo total del investigador
ORDER BY tiempoTotal DESC -- Ordenar por tiempo total acumulado de forma descendente
LIMIT 1; -- Cogemos el primer investigador de forma descendente, lo que significa que es el que mas tiempo ha reservado

SELECT DATE(R.Comienzo) AS Fecha, COUNT(*) AS NumeroReservas
FROM RESERVA R
GROUP BY Fecha
ORDER BY NumeroReservas DESC
LIMIT 1; 

