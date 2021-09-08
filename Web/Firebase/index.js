import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";

const apikey=process.env.apiKey;
console.log(apikey);


const firebaseConfig = {
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);