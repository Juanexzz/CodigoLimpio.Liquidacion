UPDATE liquidacion_empleado SET
    salario_auxilio = %s,
    salario_sin_auxilio = %s,
    salario_variable = %s,
    fecha_inicio = %s,
    fecha_fin = %s,
    dias_suspension = %s,
    dias_indemnizacion = %s
WHERE id = %s;
