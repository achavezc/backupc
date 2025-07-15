CREATE TABLE tipo_accion (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

CREATE TABLE frecuencia (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

INSERT INTO tipo_accion (nombre) VALUES
('Preventiva'),
('Correctiva'),
('Mitigación'),
('Mejora continua');

INSERT INTO frecuencia (nombre) VALUES
('Diaria'),
('Semanal'),
('Mensual'),
('Trimestral');

CREATE TABLE recomendacion (
    id SERIAL PRIMARY KEY,
    incidente_id INTEGER NOT NULL,
    prioridad_id INTEGER NOT NULL,
    faseproyecto_id INTEGER NOT NULL,
    tipoaccion_id INTEGER NOT NULL,
    frecuencia_id INTEGER NOT NULL,
    recomendacion TEXT NOT NULL,
    usuario_registro VARCHAR(100),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    usuario_actualizacion VARCHAR(100),
    fecha_actualizacion TIMESTAMP,

    CONSTRAINT fk_incidente FOREIGN KEY (incidente_id) REFERENCES incidente (id) ON DELETE CASCADE,
    CONSTRAINT fk_prioridad FOREIGN KEY (prioridad_id) REFERENCES prioridad (id),
    CONSTRAINT fk_faseproyecto FOREIGN KEY (faseproyecto_id) REFERENCES fase_proyecto (id),
    CONSTRAINT fk_tipoaccion FOREIGN KEY (tipoaccion_id) REFERENCES tipo_accion (id),
    CONSTRAINT fk_frecuencia FOREIGN KEY (frecuencia_id) REFERENCES frecuencia (id)
);

-- Asegúrate de tener valores en incidente, prioridad, fase_proyecto para las siguientes inserciones
INSERT INTO recomendacion (
    incidente_id, prioridad_id, faseproyecto_id,
    tipoaccion_id, frecuencia_id, recomendacion,
    usuario_registro, fecha_registro
) VALUES
(1, 1, 1, 1, 1, 'Actualizar el sistema de backup para prevenir incidentes similares.', 'admin', NOW()),
(1, 1, 1, 2, 2, 'Capacitar al personal sobre manejo de errores críticos.', 'admin', NOW());