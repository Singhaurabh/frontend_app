//Import the functions you need from the SDKs you need
import { initializeApp } from "https://www.gstatic.com/firebasejs/11.6.0/firebase-app.js";
import { getAuth, createUserWithEmailAndPassword } from "firebase/auth";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/11.6.0/firebase-analytics.js";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAqJ-FRgjYrxudJUd85VZd31PJ0NFIIPyc",
  authDomain: "fitness4me-574ee.firebaseapp.com",
  projectId: "fitness4me-574ee",
  storageBucket: "fitness4me-574ee.firebasestorage.app",
  messagingSenderId: "489218106921",
  appId: "1:489218106921:web:11299a2aa9d15099255e38",
  measurementId: "G-RVRXFTGHF5"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);


//submit button
const submit = document.getElementById("submit");
submit.addEventListener("click", function(event){
    event.preventDefault()

    
//inputs
const email = document.getElementById("email").value;
const password = document.getElementById("password").value;
    createUserWithEmailAndPassword(auth, email, password)
  .then((userCredential) => {
    // Signed up 
    const user = userCredential.user;
    alert("User created successfully!");
    // ...
  })
  .catch((error) => {
    const errorCode = error.code;
    const errorMessage = error.message;
    alert("Error: " + errorMessage);
    // ..
  });

});
