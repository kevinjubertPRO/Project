CREATE SCHEMA lego;
CREATE TABLE lego.lego_movies (
	show_id text,
	type text,
	title text,
	director text,
	cast text,
	country text,
	date_added text,
	release_year int,
	rating text,
	duration int,
	genres text,
	description text
);
COPY lego.lego_movies FROM 'c:/Users/CSLTKevinJubert/OneDrive - EXTIA/Bureau/Projets/POWER BI/02 - NETFLIX/data/dataset/movies.csv' WITH CSV HEADER DELIMITER ',';

CREATE TABLE lego.lego_reference_country_localisation (
	iso_3166_alpha_2 text,
	iso_3166_alpha_3 text,
	country_netflix_code_name text,
	continent text,
	country_en text,
	country_fr text,
	capital_city text,
	capital_city_latitiude real,
	capital_city_longitude real
);
COPY lego.lego_reference_country_localisation FROM 'c:/Users/CSLTKevinJubert/OneDrive - EXTIA/Bureau/Projets/POWER BI/02 - NETFLIX/data/dataset/reference_country_localisation.csv' WITH CSV HEADER DELIMITER ',';

CREATE TABLE lego.lego_stock_market (
	Date text,
	Open real,
	High real,
	Low real,
	Close real,
	Adj Close real,
	Volume int
);
COPY lego.lego_stock_market FROM 'c:/Users/CSLTKevinJubert/OneDrive - EXTIA/Bureau/Projets/POWER BI/02 - NETFLIX/data/dataset/stock_market.csv' WITH CSV HEADER DELIMITER ',';

