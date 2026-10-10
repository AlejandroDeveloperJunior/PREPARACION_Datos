-- ======================================================================
--  DISEÑO FORMAL DE DATA WAREHOUSE: ESQUEMA ESTRELLA (STAR SCHEMA)
--  Caso de Estudio: Plataforma de Analítica Deportiva & Cuotas 2026
-- ======================================================================

-- 1. Dimensión Ligas / Torneos
CREATE TABLE IF NOT EXISTS dim_leagues (
    league_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    country VARCHAR(100) NOT NULL,
    tier VARCHAR(50) DEFAULT 'PRIMERA_DIVISION',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Dimensión Equipos / Clubes
CREATE TABLE IF NOT EXISTS dim_teams (
    team_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    league_id VARCHAR(50) NOT NULL,
    venue VARCHAR(150),
    country VARCHAR(100),
    FOREIGN KEY (league_id) REFERENCES dim_leagues(league_id)
);

-- 3. Dimensión Temporal (Date Dimension)
CREATE TABLE IF NOT EXISTS dim_date (
    date_id VARCHAR(20) PRIMARY KEY,
    full_date DATE NOT NULL,
    year INT NOT NULL,
    month INT NOT NULL,
    day INT NOT NULL,
    day_of_week VARCHAR(20) NOT NULL,
    is_weekend BOOLEAN NOT NULL
);

-- 4. Dimensión Jugadores (Opcional / Extensión Sabermétrica)
CREATE TABLE IF NOT EXISTS dim_players (
    player_id VARCHAR(50) PRIMARY KEY,
    full_name VARCHAR(150) NOT NULL,
    team_id VARCHAR(50),
    primary_position VARCHAR(50),
    nationality VARCHAR(100),
    FOREIGN KEY (team_id) REFERENCES dim_teams(team_id)
);

-- 5. TABLA DE HECHOS: FACT_FIXTURES (Partidos, Marcadores, Métricas y Cuotas)
CREATE TABLE IF NOT EXISTS fact_fixtures (
    fixture_id VARCHAR(50) PRIMARY KEY,
    date_id VARCHAR(20) NOT NULL,
    league_id VARCHAR(50) NOT NULL,
    home_team_id VARCHAR(50) NOT NULL,
    away_team_id VARCHAR(50) NOT NULL,
    home_score INT,
    away_score INT,
    odds_home DECIMAL(5,2),
    odds_draw DECIMAL(5,2),
    odds_away DECIMAL(5,2),
    status VARCHAR(50) NOT NULL,
    data_quality_verified BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (date_id) REFERENCES dim_date(date_id),
    FOREIGN KEY (league_id) REFERENCES dim_leagues(league_id),
    FOREIGN KEY (home_team_id) REFERENCES dim_teams(team_id),
    FOREIGN KEY (away_team_id) REFERENCES dim_teams(team_id)
);

-- Índices de Rendimiento para Consultas Analíticas (OLAP)
CREATE INDEX IF NOT EXISTS idx_fact_date ON fact_fixtures(date_id);
CREATE INDEX IF NOT EXISTS idx_fact_league ON fact_fixtures(league_id);
CREATE INDEX IF NOT EXISTS idx_fact_home ON fact_fixtures(home_team_id);
CREATE INDEX IF NOT EXISTS idx_fact_away ON fact_fixtures(away_team_id);
