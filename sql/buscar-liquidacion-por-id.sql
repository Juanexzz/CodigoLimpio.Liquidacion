SELECT salario_auxilio, salario_sin_auxilio, salario_variable,
       fecha_inicio, fecha_fin, dias_suspension, dias_indemnizacion
FROM liquidacion_empleado WHERE id = %s;
