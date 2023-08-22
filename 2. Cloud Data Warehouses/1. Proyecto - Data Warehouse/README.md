
# Project 2: Data Warehouse

## Quick start

#### This project handles Sparkify, a music streaming startup. Our goal consists of building an ETL pipeline (Extract, Transform, Load):
- Extract data from S3.
- Stage data into Redshift.
- Transform data into a set of dimensional tables.

## Database

####  Sparkify contains a dataset, this dataset is a set of files in JSON format stored in AWS S3 buckets:
- s3://udacity-dend/song_data.
- s3://udacity-dend/log_json_path.json.

#### Sparkify database schema has a star design. Now, we are going to explain the items that conform the Staging Tables, Fact Table, and the Dimension Tables.

### Staging Tables
- staging_events: auth, firstName, gender, itemInSession, lastName, length, level, location, method, page, registration, sessionId, song, status, ts, userAgent, userId.
- staging_songs: num_songs, artist_id, artist_latitude, artist_longitude, artist_location, artist_name, song_id, title, duration, year.

### Fact Table
- songplays: songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent.

### Dimension Tables
- users: user_id, first_name, last_name, gender, level.
- songs: song_id, title, artist_id, year, duration.
- artists: artist_id, name, location, latitude, longitude.
- time: start_time, hour, day, week, month, year, weekday. 

## Steps

### 0. Set up the Redshift cluster
- IAM user creation (testUser), and IAM role (myawsRole) with AmazonS3ReadOnlyAccess permissions.
- Redshift cluster creation (testCluster with 4x dc2.large nodes) and location US-West-2.
- S3 bucket creation. 
- Edit cwh.cfg, and copy log_data and song_data folders to my S3 bucket.

### 1. Create the Table Schemas
#### Once we added the Redshift database and the IAM role/user into dwh.cfg, and we have designed the schemas for the fact and dimension tables, it is time to edit sql_tables.py:
- SQL DROP statements.
- SQL CREATE statements.
- Staging tables copies, and final tables insertions.

### 2. Build ETL Pipeline
#### Edit etl.py:
- Loads data from S3 to staging tables on Redshift, and loads data from staging tables to analytics tables on Redshift.
- File testing after create_tables.py.
- Finally delete the Redshift cluster.