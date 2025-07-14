-- =====================
-- 1. ELIMINAR TABLAS SI EXISTEN
-- =====================
DROP TABLE IF EXISTS profile_privileges;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS privileges;
DROP TABLE IF EXISTS profiles;

-- =====================
-- 2. CREAR TABLAS
-- =====================

CREATE TABLE profiles (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE privileges (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE profile_privileges (
    profile_id INTEGER REFERENCES profiles(id) ON DELETE CASCADE,
    privilege_id INTEGER REFERENCES privileges(id) ON DELETE CASCADE,
    PRIMARY KEY (profile_id, privilege_id)
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(100) NOT NULL UNIQUE,
    full_name VARCHAR(100) NOT NULL,
    password_hash TEXT NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    profile_id INTEGER REFERENCES profiles(id)
);

-- =====================
-- 3. INSERTAR DATOS DE PRUEBA
-- =====================

-- Perfiles
INSERT INTO profiles (name) VALUES
('Administrador'),
('Analista'),
('Operador');

-- Privilegios
INSERT INTO privileges (name) VALUES
('Usuarios y Perfiles'),
('Registro de Incidentes'),
('Clasificación de Incidentes');

-- Asignar todos los privilegios al perfil Administrador
INSERT INTO profile_privileges (profile_id, privilege_id)
SELECT 1, id FROM privileges;

-- Asignar solo algunos privilegios a Analista
INSERT INTO profile_privileges (profile_id, privilege_id)
VALUES (2, 2), (2, 3);

-- Solo clasificación para Operador
INSERT INTO profile_privileges (profile_id, privilege_id)
VALUES (3, 3);

-- =====================
-- 4. Crear usuarios de prueba
-- =====================

-- Todos con contraseña: "Admin123!"
-- Hash: $2b$12$QqnMbUvZFRUVvRyxMEsvh.4Xm/O.eWxZ4rJgHe7TLErkiWBdV5IUK

INSERT INTO users (email, full_name, password_hash, is_active, profile_id)
VALUES
('admin@admin.com', 'Admin Principal', '$2b$12$QqnMbUvZFRUVvRyxMEsvh.4Xm/O.eWxZ4rJgHe7TLErkiWBdV5IUK', TRUE, 1),
('analista@empresa.com', 'Analista Uno', '$2b$12$QqnMbUvZFRUVvRyxMEsvh.4Xm/O.eWxZ4rJgHe7TLErkiWBdV5IUK', TRUE, 2),
('operador@empresa.com', 'Operador Uno', '$2b$12$QqnMbUvZFRUVvRyxMEsvh.4Xm/O.eWxZ4rJgHe7TLErkiWBdV5IUK', TRUE, 3);
