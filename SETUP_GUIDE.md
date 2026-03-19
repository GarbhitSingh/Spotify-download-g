# SETUP_GUIDE.md

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/GarbhitSingh/Spotify-download-g.git
   cd Spotify-download-g
   ```
2. Install the required dependencies using npm:
   ```bash
   npm install
   ```
3. Create a .env file in the root directory and configure the necessary environment variables.

## Feature Overview
- **Download Functionality**: Allows downloading Spotify playlists and tracks.
- **User Authentication**: Secure login using OAuth2.
- **Database Integration**: Stores user preferences and download history.

## Database Schemas
- **Users**  
  - `id`: INT, PRIMARY KEY  
  - `username`: VARCHAR(255)  
  - `email`: VARCHAR(255)  
  - `created_at`: TIMESTAMP  

- **Downloads**  
  - `id`: INT, PRIMARY KEY  
  - `user_id`: INT, FOREIGN KEY  
  - `track_id`: VARCHAR(255)  
  - `downloaded_at`: TIMESTAMP  

## Deployment Options
1. **Docker**: You can use Docker to containerize your application for easy deployment.
   ```bash
   docker build -t spotify-download .
   docker run -d -p 3000:3000 spotify-download
   ```
2. **Heroku**: Deploy your application to Heroku by following the Heroku [deployment guide](https://devcenter.heroku.com/articles/git).

## Additional Information
- Ensure you have Node.js and npm installed.
- For any issues, refer to the [GitHub issues section](https://github.com/GarbhitSingh/Spotify-download-g/issues).