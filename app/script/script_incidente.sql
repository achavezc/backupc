-- Tabla: Sistema
CREATE TABLE sistema (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
);

-- Tabla: ProyectoModulo
CREATE TABLE proyecto_modulo (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL
);

-- Tabla: Incidente
CREATE TABLE incidente (
    id SERIAL PRIMARY KEY,
    fecha DATE NOT NULL,
    hora TIME NOT NULL,
    sistema_id INTEGER REFERENCES sistema(id),
    proyectomodulo_id INTEGER REFERENCES proyecto_modulo(id),
    usuario_reportador VARCHAR(255),
    descripcion TEXT,
    tiempo_estimado INTEGER,
    fecha_solucion DATE,
    hora_solucion TIME,
    usuario_registro VARCHAR(255),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    usuario_actualizacion VARCHAR(255),
    fecha_actualizacion TIMESTAMP
);

-- Datos de prueba para Sistema
INSERT INTO sistema (nombre) VALUES
('Gestión de Usuarios'),
('Finanzas'),
('Inventario');

-- Datos de prueba para ProyectoModulo
INSERT INTO proyecto_modulo (nombre) VALUES
('Autenticación'),
('Facturación'),
('Control de Stock');

-- Datos de prueba para Incidente
INSERT INTO incidente (
    fecha, hora, sistema_id, proyectomodulo_id, usuario_reportador,
    descripcion, tiempo_estimado, fecha_solucion, hora_solucion,
    usuario_registro, fecha_registro, usuario_actualizacion, fecha_actualizacion
) VALUES
('2025-07-10', '09:30:00', 1, 1, 'juan.perez', 'Error al iniciar sesión', 10,
 '2025-07-10', '11:30:00', 'admin', NOW(), 'admin', NOW()),

('2025-07-11', '10:00:00', 2, 2, 'maria.lopez', 'Error en la generación de factura', 20,
 '2025-07-11', '13:00:00', 'admin', NOW(), 'admin', NOW()),

('2025-07-12', '08:45:00', 3, 3, 'carlos.martinez', 'Desfase en el stock de productos', 30,
 '2025-07-12', '12:45:00', 'admin', NOW(), 'admin', NOW());
