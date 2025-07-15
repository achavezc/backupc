-- Crear tabla Prioridad
CREATE TABLE prioridad (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

-- Crear tabla Estado
CREATE TABLE estado (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

-- Crear tabla Proyecto
CREATE TABLE proyecto (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    fecha_inicio DATE NOT NULL,
    fecha_fin DATE NOT NULL,
    prioridad_id INTEGER REFERENCES prioridad(id),
    faseproyecto_id INTEGER REFERENCES fase_proyecto(id),
    estado_id INTEGER REFERENCES estado(id),
    usuario_registro VARCHAR(100) NOT NULL,
    fecha_registro TIMESTAMP NOT NULL DEFAULT NOW(),
    usuario_actualizacion VARCHAR(100),
    fecha_actualizacion TIMESTAMP
);

-- Insertar datos de prueba en Prioridad
INSERT INTO prioridad (nombre) VALUES
('Alta'),
('Media'),
('Baja');

-- Insertar datos de prueba en Estado
INSERT INTO estado (nombre) VALUES
('Activo'),
('En Progreso'),
('Finalizado'),
('Cancelado');


-- Insertar datos de prueba en Proyecto
INSERT INTO proyecto (
    nombre, fecha_inicio, fecha_fin, prioridad_id,
    faseproyecto_id, estado_id, usuario_registro, fecha_registro
) VALUES
('Proyecto A', '2025-01-01', '2025-06-30', 1, 1, 1, 'admin', NOW()),
('Proyecto B', '2025-03-01', '2025-09-15', 2, 2, 2, 'admin', NOW()),
('Proyecto C', '2025-05-15', '2025-12-31', 3, 3, 3, 'admin', NOW());
