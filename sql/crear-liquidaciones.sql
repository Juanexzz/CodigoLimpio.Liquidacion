CREATE TABLE liquidacion_empleado (
    id SERIAL PRIMARY KEY,
    salario_auxilio INT NOT NULL,
    salario_sin_auxilio INT NOT NULL,
    salario_variable INT NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    dias_suspension INT NOT NULL,
    dias_indemnizacion INT NOT NULL
);