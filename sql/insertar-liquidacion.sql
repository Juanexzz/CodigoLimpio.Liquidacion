INSERT INTO liquidacion_empleado (
    salario_auxilio, salario_sin_auxilio, salario_variable,
    fecha_inicio, fecha_fin, dias_suspension, dias_indemnizacion
) VALUES (
    %s, %s, %s, %s, %s, %s, %s
) RETURNING id;
