## Wayne's Work Flow
I have developed new models and the four endpoints in the urls.py in users folder are 
dependent on Farmer, Buyer and Supplier models.

# Jason Web Token Generation
To generate either an access or refresh token, got to your chrome browser or postman and;
1. type url `http://127.0.0.1:8000/api/token/`
2. enter `admin` as username and `123` as password
3. click Post
4. copy the refresh token and paste it in the postman token entry box after choosing Bearer Token as authorization type
4. type url `http://127.0.0.1:8000/<api endpoint>/` api endpoint ie; `/api/farmer/`
5. click send in Postman to access the api endpoint's properties

If you run into an error in Postman where the prompt is token not valid, got to your terminal and run;
    `curl \ `
    `-X POST \`
    `-H "Content-Type: application/json" \`
    `-d '{"username": "admin", "password": "123"}' \ `
    You will get the access the access and refresh token. Copy either tokens. However, the refresh token is prefferable as it expires in 24 hours.

Then run the following to prove authentication of the protected api endpoint;
    `curl \`
    `-X POST \`
    `-H "Authorization: Bearer <paste the token>" \`
    `http://127.0.0.1:8000/api/<api endpoint>/`
    If successful, you will see the fields of the api endpoint
