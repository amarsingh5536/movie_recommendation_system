# movie_recommendation_system Service


# Getting Started
In the project directory, follow the given steps to run movie_recommendation_system service:

   1. Rename sample.env to .env and Configure .evn file
   2. Containerize the App with Docker
   3. Runs the app in the development mode > sudo docker-compose up
   4. Uncomment line in entrypoint.sh "# flask db upgrade" for migrate new changes in DB of migration file and run sudo docker-compose up again.
   5. Open [http://localhost:8080/recommend/movie/?description=Avatar] to Test it in your browser.
