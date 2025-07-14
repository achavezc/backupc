-- Tablas de catálogo
CREATE TABLE fase_proyecto (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE impacto (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE tipo (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

-- Tabla principal de clasificación de incidentes
CREATE TABLE clasificacion_incidente (
    id SERIAL PRIMARY KEY,
    incidente_id INTEGER REFERENCES incidente(id),
    faseproyecto_id INTEGER REFERENCES fase_proyecto(id),
    impacto_id INTEGER REFERENCES impacto(id),
    tipo_id INTEGER REFERENCES tipo(id),
    usuario_registro VARCHAR(255),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    usuario_actualizacion VARCHAR(255),
    fecha_actualizacion TIMESTAMP
);

-- Datos de prueba
INSERT INTO fase_proyecto (nombre) VALUES
('Análisis'),
('Diseño'),
('Desarrollo'),
('Pruebas');

INSERT INTO impacto (nombre) VALUES
('Bajo'),
('Medio'),
('Alto'),
('Crítico');

INSERT INTO tipo (nombre) VALUES
('Bug'),
('Mejora'),
('Soporte'),
('Cambio Requerido');

--Clasificación Incidente (usando IDs válidos desde las tablas anteriores)
INSERT INTO clasificacion_incidente (
    incidente_id, faseproyecto_id, impacto_id, tipo_id, usuario_registro
) VALUES
(1, 3, 2, 1, 'admin'),  -- Desarrollo, Impacto Medio, Tipo Funcional
(2, 4, 3, 2, 'admin'),  -- Pruebas, Impacto Alto, Tipo Técnico
(3, 2, 1, 3, 'admin');  -- Diseño, Impacto Bajo, Tipo Interfaz