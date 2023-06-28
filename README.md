<h1>Telegram Sticker Scraper</h1>

<p>
  This Python project is designed to scrape Telegram sticker links from
  <a href="https://combot.org/telegram/">https://combot.org/telegram/</a> and send the sticker links as a response in a Flask API.
</p>

<h2>Installation</h2>

<ol>
  <li>Clone the repository:</li>
</ol>

<pre><code>git clone https://github.com/TAMILVIP007/Sticker-Scraper
</code></pre>

<ol start="2">
  <li>Navigate to the project directory:</li>
</ol>

<pre><code>cd Sticker-Scraper
</code></pre>

<ol start="3">
  <li>Create and activate a virtual environment (optional but recommended):</li>
</ol>

<pre><code>python3 -m venv venv
source venv/bin/activate
</code></pre>

<ol start="4">
  <li>Install the required dependencies:</li>
</ol>

<pre><code>pip install -r requirements.txt
</code></pre>

<h2>Usage</h2>

<ol>
  <li>Start the Flask API server:</li>
</ol>

<pre><code>python app.py
</code></pre>

<ol start="2">
  <li>Once the server is running, you can send a GET request to the following endpoint to scrape the Telegram sticker links:</li>
</ol>

<pre><code>GET http://localhost:5000/stickers?q=cats
</code></pre>

<p>
  The server will respond with a JSON object containing the scraped sticker links.
</p>

<h2>Hosting the Flask API</h2>

<p>
  To host the Flask API on a production server, follow these steps:
</p>

<ol>
  <li>Deploy the code to a server or cloud platform of your choice.</li>
  <li>Set up the necessary environment variables:</li>
</ol>

<p>
  <strong>FLASK_APP:</strong> Set this variable to <code>app.py</code>.
</p>

<p>
  <strong>FLASK_ENV:</strong> Set this variable to <code>production</code>.
</p>

<ol start="3">
  <li>Install a web server such as Nginx or Apache to serve as a reverse proxy for your Flask application.</li>
  <li>Configure the web server to forward requests to your Flask application running on the specified port (e.g., 5000).</li>
  <li>Set up SSL/TLS certificates to enable HTTPS for secure communication with the API.</li>
  <li>Configure your server's firewall to allow incoming traffic on the specified port (e.g., 80 for HTTP or 443 for HTTPS).</li>
  <li>Start the Flask application using a process manager like Gunicorn or uWSGI.</li>
</ol>

<pre><code>gunicorn app:app
</code></pre>

<p>
  Access your Flask API using the domain name or IP address of your server.
</p>

<h2>License</h2>

<p>
  This project is licensed under the <a href="LICENSE">MIT License</a>. Feel free to modify and use it according to your needs.
</p>

<h2>Disclaimer</h2>

<p>
  Please note that scraping websites without permission may violate the terms of service of the website you are scraping. Ensure you have the necessary rights and permissions before scraping any website. The purpose of this project is for educational and learning purposes only.
</p>
